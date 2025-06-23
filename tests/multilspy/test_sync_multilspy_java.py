"""
This file contains tests for running the Java Language Server: Eclipse JDT.LS
"""

from pathlib import PurePath, Path
from multilspy import SyncLanguageServer
from multilspy.multilspy_config import Language
from tests.test_utils import create_test_context

java_server_path = Path(__file__).parent.parent.parent /"src"/ "multilspy" / "language_servers" / "eclipse_jdtls" / "static"
java_server_config = {"java_server_config": {
    "jre_home_path": str(PurePath(java_server_path,"vscode-java/extension/jre/21.0.5-macosx-aarch64")),
    "jre_path": str(PurePath(java_server_path,"vscode-java/extension/jre/21.0.5-macosx-aarch64/bin/java")),
    "lombok_jar_path": str(PurePath(java_server_path,"vscode-java/extension/lombok/lombok-1.18.34.jar")),
    "jdtls_jar_path": str(PurePath(java_server_path,"vscode-java/extension/server/plugins/org.eclipse.equinox.launcher_1.6.900.v20240613-2009.jar")),
    "jdtls_config_path": str(PurePath(java_server_path,"vscode-java/extension/server/config_mac_arm")),
    "gradle_path": str(PurePath(java_server_path,"gradle-8.5"))
}}

def test_multilspy_java_clickhouse_highlevel_sinker() -> None:
    """
    Test the working of multilspy with Java repository - clickhouse-highlevel-sinker
    """
    code_language = Language.JAVA

    params = {
        "code_language": code_language,
        "repo_url": "https://github.com/Index103000/clickhouse-highlevel-sinker/",
        "repo_commit": "ee31d278918fe5e64669a6840c4d8fb53889e573",
        "java_server_config": java_server_config["java_server_config"]
    }

    with create_test_context(params) as context:
        lsp = SyncLanguageServer.create(context.config, context.logger, context.source_directory)

        # All the communication with the language server must be performed inside the context manager
        # The server process is started when the context manager is entered and is terminated when the context manager is exited.
        with lsp.start_server():
            filepath = str(PurePath("src/main/java/com/xlvchao/clickhouse/component/ClickHouseSinkManager.java"))
            result = lsp.request_definition(filepath, 44, 59)

            assert isinstance(result, list)
            assert len(result) == 1
            item = result[0]
            assert item["relativePath"] == str(
                PurePath("src/main/java/com/xlvchao/clickhouse/component/ScheduledCheckerAndCleaner.java")
            )
            assert item["range"] == {
                "start": {"line": 22, "character": 11},
                "end": {"line": 22, "character": 37},
            }

            # TODO: The following test is running flaky on Windows. Investigate and fix.
            # On Windows, it returns the correct result sometimes and sometimes it returns the following:
            # incorrect_output = [
            #     {
            #         "range": {"end": {"character": 86, "line": 24}, "start": {"character": 65, "line": 24}},
            #         "relativePath": "src\\main\\java\\com\\xlvchao\\clickhouse\\component\\ClickHouseSinkManager.java",
            #     },
            #     {
            #         "range": {"end": {"character": 61, "line": 2}, "start": {"character": 7, "line": 2}},
            #         "relativePath": "src\\test\\java\\com\\xlvchao\\clickhouse\\SpringbootDemo.java",
            #     },
            #     {
            #         "range": {"end": {"character": 29, "line": 28}, "start": {"character": 8, "line": 28}},
            #         "relativePath": "src\\test\\java\\com\\xlvchao\\clickhouse\\SpringbootDemo.java",
            #     },
            #     {
            #         "range": {"end": {"character": 69, "line": 28}, "start": {"character": 48, "line": 28}},
            #         "relativePath": "src\\test\\java\\com\\xlvchao\\clickhouse\\SpringbootDemo.java",
            #     },
            # ]

            result = lsp.request_references(filepath, 82, 27)

            assert isinstance(result, list)
            assert len(result) == 2

            for item in result:
                del item["uri"]
                del item["absolutePath"]

            assert result == [
                {
                    "relativePath": str(
                        PurePath("src/main/java/com/xlvchao/clickhouse/component/ClickHouseSinkManager.java")
                    ),
                    "range": {
                        "start": {"line": 75, "character": 66},
                        "end": {"line": 75, "character": 85},
                    },
                },
                {
                    "relativePath": str(
                        PurePath("src/main/java/com/xlvchao/clickhouse/component/ClickHouseSinkManager.java")
                    ),
                    "range": {
                        "start": {"line": 71, "character": 12},
                        "end": {"line": 71, "character": 31},
                    },
                },
            ]
