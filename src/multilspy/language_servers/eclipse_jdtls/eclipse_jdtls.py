"""
Provides Java specific instantiation of the LanguageServer class. Contains various configurations and settings specific to Java.
"""

import asyncio
import copy
import dataclasses
import logging
import os
import pathlib
import shutil
import uuid
from contextlib import asynccontextmanager
from typing import AsyncIterator

from multilspy.multilspy_logger import MultilspyLogger
from multilspy.language_server import LanguageServer
from multilspy.lsp_protocol_handler.server import ProcessLaunchInfo
from multilspy.lsp_protocol_handler.lsp_types import InitializeParams
from multilspy.multilspy_config import MultilspyConfig
from multilspy.multilspy_settings import MultilspySettings
from pathlib import PurePath

from multilspy.language_servers.eclipse_jdtls.initialize_params import initialize_parameters


@dataclasses.dataclass
class RuntimeDependencyPaths:
    """
    Stores the paths to the runtime dependencies of EclipseJDTLS
    """

    gradle_path: str
    lombok_jar_path: str
    jre_path: str
    jre_home_path: str
    jdtls_launcher_jar_path: str
    jdtls_readonly_config_path: str


class EclipseJDTLS(LanguageServer):
    """
    The EclipseJDTLS class provides a Java specific implementation of the LanguageServer class
    """

    def __init__(self, config: MultilspyConfig, logger: MultilspyLogger, repository_root_path: str):
        """
        Creates a new EclipseJDTLS instance initializing the language server settings appropriately.
        This class is not meant to be instantiated directly. Use LanguageServer.create() instead.
        """

        runtime_dependency_paths = self.setupRuntimeDependencies(logger, config)
        self.runtime_dependency_paths = runtime_dependency_paths
        self.is_standalone_mode = config.java_server_config.is_standalone_mode

        # ws_dir is the workspace directory for the EclipseJDTLS server
        ws_dir = str(
            PurePath(
                MultilspySettings.get_language_server_directory(),
                "EclipseJDTLS",
                "workspaces",
                uuid.uuid4().hex,
            )
        )

        # shared_cache_location is the global cache used by Eclipse JDTLS across all workspaces
        shared_cache_location = str(
            PurePath(MultilspySettings.get_global_cache_directory(), "lsp", "EclipseJDTLS", "sharedIndex")
        )

        jre_path = self.runtime_dependency_paths.jre_path
        lombok_jar_path = self.runtime_dependency_paths.lombok_jar_path

        jdtls_launcher_jar = self.runtime_dependency_paths.jdtls_launcher_jar_path

        os.makedirs(ws_dir, exist_ok=True)

        data_dir = str(PurePath(ws_dir, "data_dir"))
        jdtls_config_path = str(PurePath(ws_dir, "config_path"))

        jdtls_readonly_config_path = self.runtime_dependency_paths.jdtls_readonly_config_path

        if not os.path.exists(jdtls_config_path):
            shutil.copytree(jdtls_readonly_config_path, jdtls_config_path)

        for static_path in [
            jre_path,
            lombok_jar_path,
            jdtls_launcher_jar,
            jdtls_config_path,
            jdtls_readonly_config_path,
        ]:
            assert os.path.exists(static_path), static_path

        # TODO: Add "self.runtime_dependency_paths.jre_home_path"/bin to $PATH as well
        proc_env = {"syntaxserver": "false", "JAVA_HOME": self.runtime_dependency_paths.jre_home_path}
        proc_cwd = repository_root_path
        cmd = " ".join(
            [
                jre_path,
                "--add-modules=ALL-SYSTEM",
                "--add-opens",
                "java.base/java.util=ALL-UNNAMED",
                "--add-opens",
                "java.base/java.lang=ALL-UNNAMED",
                "--add-opens",
                "java.base/sun.nio.fs=ALL-UNNAMED",
                "-Declipse.application=org.eclipse.jdt.ls.core.id1",
                "-Dosgi.bundles.defaultStartLevel=4",
                "-Declipse.product=org.eclipse.jdt.ls.core.product",
                "-Djava.import.generatesMetadataFilesAtProjectRoot=false",
                "-Dfile.encoding=utf8",
                "-noverify",
                "-XX:+UseParallelGC",
                "-XX:GCTimeRatio=4",
                "-XX:AdaptiveSizePolicyWeight=90",
                "-Dsun.zip.disableMemoryMapping=true",
                "-Djava.lsp.joinOnCompletion=true",
                "-Xmx8G",
                "-Xms2G",
                "-Xlog:disable",
                "-Dlog.level=ALL",
                f"-javaagent:{lombok_jar_path}",
                f"-Djdt.core.sharedIndexLocation={shared_cache_location}",
                "-jar",
                jdtls_launcher_jar,
                "-configuration",
                jdtls_config_path,
                "-data",
                data_dir,
            ]
        )

        self.service_ready_event = asyncio.Event()
        self.initialize_searcher_command_available = asyncio.Event()

        super().__init__(config, logger, repository_root_path, ProcessLaunchInfo(cmd, proc_env, proc_cwd), "java")

    def setupRuntimeDependencies(self, logger: MultilspyLogger, config: MultilspyConfig) -> RuntimeDependencyPaths:
        """
        Setup runtime dependencies for EclipseJDTLS.
        """
        gradle_path = config.java_server_config.gradle_path
        assert os.path.exists(gradle_path)

        jre_home_path = config.java_server_config.jre_home_path
        jre_path = config.java_server_config.jre_path
        lombok_jar_path = config.java_server_config.lombok_jar_path
        jdtls_launcher_jar_path = config.java_server_config.jdtls_jar_path
        jdtls_readonly_config_path = config.java_server_config.jdtls_config_path

        assert os.path.exists(jre_home_path)
        assert os.path.exists(jre_path)
        assert os.path.exists(lombok_jar_path)
        assert os.path.exists(jdtls_launcher_jar_path)
        assert os.path.exists(jdtls_readonly_config_path)

        #os.chmod(jre_path, stat.S_IEXEC)

        #jspawnhelper_path = str(PurePath(jre_home_path, "lib/jspawnhelper"))
        #if os.path.exists(jspawnhelper_path):
            #os.chmod(jspawnhelper_path, stat.S_IEXEC)
        #else:
            #logger.log(f"jspawnhelper not found at {jspawnhelper_path}", logging.INFO)

        return RuntimeDependencyPaths(
            gradle_path=gradle_path,
            lombok_jar_path=lombok_jar_path,
            jre_path=jre_path,
            jre_home_path=jre_home_path,
            jdtls_launcher_jar_path=jdtls_launcher_jar_path,
            jdtls_readonly_config_path=jdtls_readonly_config_path,
        )

    def _get_initialize_params(self, repository_absolute_path: str, is_standalone_mode: bool) -> InitializeParams:
        """
        Returns the initialize parameters for the EclipseJDTLS server.
        """
        # Look into https://github.com/eclipse/eclipse.jdt.ls/blob/master/org.eclipse.jdt.ls.core/src/org/eclipse/jdt/ls/core/internal/preferences/Preferences.java to understand all the options available
        d = copy.deepcopy(initialize_parameters)
        del d["_description"]

        if not os.path.isabs(repository_absolute_path):
            repository_absolute_path = os.path.abspath(repository_absolute_path)

        assert d["processId"] == "os.getpid()"
        d["processId"] = os.getpid()

        assert d["rootPath"] == "repository_absolute_path"
        d["rootPath"] = repository_absolute_path

        assert d["rootUri"] == "pathlib.Path(repository_absolute_path).as_uri()"
        d["rootUri"] = pathlib.Path(repository_absolute_path).as_uri()

        assert d["initializationOptions"]["workspaceFolders"] == "[pathlib.Path(repository_absolute_path).as_uri()]"
        d["initializationOptions"]["workspaceFolders"] = [pathlib.Path(repository_absolute_path).as_uri()]

        assert (
            d["workspaceFolders"]
            == '[\n            {\n                "uri": pathlib.Path(repository_absolute_path).as_uri(),\n                "name": os.path.basename(repository_absolute_path),\n            }\n        ]'
        )
        d["workspaceFolders"] = [
            {
                "uri": pathlib.Path(repository_absolute_path).as_uri(),
                "name": os.path.basename(repository_absolute_path),
            }
        ]

        assert d["initializationOptions"]["settings"]["java"]["configuration"]["runtimes"] == [
            {"name": "JavaSE-17", "path": "static/vscode-java/extension/jre/17.0.8.1-linux-x86_64", "default": True}
        ]
        d["initializationOptions"]["settings"]["java"]["configuration"]["runtimes"] = [
            {"name": "JavaSE-21", "path": self.runtime_dependency_paths.jre_home_path}
        ]

        for runtime in d["initializationOptions"]["settings"]["java"]["configuration"]["runtimes"]:
            assert "name" in runtime
            assert "path" in runtime
            assert os.path.exists(
                runtime["path"]
            ), f"Runtime required for eclipse_jdtls at path {runtime['path']} does not exist"

        assert d["initializationOptions"]["settings"]["java"]["import"]["gradle"]["home"] == "abs(static/gradle-7.3.3)"
        d["initializationOptions"]["settings"]["java"]["import"]["gradle"][
            "home"
        ] = self.runtime_dependency_paths.gradle_path

        d["initializationOptions"]["settings"]["java"]["import"]["gradle"]["java"][
            "home"
        ] = self.runtime_dependency_paths.jre_path

        if is_standalone_mode:
            d["initializationOptions"]["settings"]["java"]["project"]["importOnFirstTimeStartup"] = "disabled"
        else:
            d["initializationOptions"]["settings"]["java"]["project"]["importOnFirstTimeStartup"] = "automatic"

        return d

    @asynccontextmanager
    async def start_server(self) -> AsyncIterator["EclipseJDTLS"]:
        """
        Starts the Eclipse JDTLS Language Server, waits for the server to be ready and yields the LanguageServer instance.

        Usage:
        ```
        async with lsp.start_server():
            # LanguageServer has been initialized and ready to serve requests
            await lsp.request_definition(...)
            await lsp.request_references(...)
            # Shutdown the LanguageServer on exit from scope
        # LanguageServer has been shutdown
        ```
        """

        async def register_capability_handler(params):
            assert "registrations" in params
            for registration in params["registrations"]:
                if registration["method"] == "textDocument/completion":
                    assert registration["registerOptions"]["resolveProvider"] == True
                    assert registration["registerOptions"]["triggerCharacters"] == [
                        ".",
                        "@",
                        "#",
                        "*",
                        " ",
                    ]
                    self.completions_available.set()
            return

        async def lang_status_handler(params):
            # TODO: Should we wait for
            # server -> client: {'jsonrpc': '2.0', 'method': 'language/status', 'params': {'type': 'ProjectStatus', 'message': 'OK'}}
            # Before proceeding?
            if params["type"] == "ServiceReady" and params["message"] == "ServiceReady":
                self.service_ready_event.set()

        async def execute_client_command_handler(params):
            assert params["command"] == "_java.reloadBundles.command"
            assert params["arguments"] == []
            return []

        async def window_log_message(msg):
            self.logger.log(f"LSP: window/logMessage: {msg}", logging.INFO)

        async def do_nothing(params):
            return

        self.server.on_request("client/registerCapability", register_capability_handler)
        self.server.on_notification("language/status", lang_status_handler)
        self.server.on_notification("window/logMessage", window_log_message)
        self.server.on_request("workspace/executeClientCommand", execute_client_command_handler)
        self.server.on_notification("$/progress", do_nothing)
        self.server.on_notification("textDocument/publishDiagnostics", do_nothing)
        self.server.on_notification("language/actionableNotification", do_nothing)

        async with super().start_server():
            self.logger.log("Starting EclipseJDTLS server process", logging.INFO)
            await self.server.start()
            initialize_params = self._get_initialize_params(self.repository_root_path, self.is_standalone_mode)

            self.logger.log(
                "Sending initialize request from LSP client to LSP server and awaiting response",
                logging.INFO,
            )
            init_response = await self.server.send.initialize(initialize_params)
            assert init_response["capabilities"]["textDocumentSync"]["change"] == 2
            assert "completionProvider" not in init_response["capabilities"]
            assert "executeCommandProvider" not in init_response["capabilities"]

            self.server.notify.initialized({})

            self.server.notify.workspace_did_change_configuration(
                {"settings": initialize_params["initializationOptions"]["settings"]}
            )

            # TODO: Add comments about why we wait here, and how this can be optimized
            await self.service_ready_event.wait()

            yield self

            await self.server.shutdown()
            await self.server.stop()
