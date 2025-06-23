"""
Configuration parameters for Multilspy.
"""
import inspect
from enum import Enum
from dataclasses import dataclass

class Language(str, Enum):
    """
    Possible languages with Multilspy.
    """

    CSHARP = "csharp"
    PYTHON = "python"
    RUST = "rust"
    JAVA = "java"
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"

    def __str__(self) -> str:
        return self.value

@dataclass
class JavaServerConfig:
    """
    Configuration parameters for Java language server
    """
    jre_home_path: str
    jre_path: str
    jdtls_jar_path: str
    jdtls_config_path: str
    lombok_jar_path: str
    gradle_path: str
    is_standalone_mode: bool = False


    @classmethod
    def from_dict(cls, env: dict):
        """
        Create a JavaServerConfig instance from a dictionary
        """
        processed_env = {}
        for k, v in env.items():
            if k in inspect.signature(cls).parameters:
                processed_env[k] = v
        return cls(**processed_env)


@dataclass
class MultilspyConfig:
    """
    Configuration parameters
    """
    code_language: Language
    trace_lsp_communication: bool = False
    java_server_config: JavaServerConfig = None

    @classmethod
    def from_dict(cls, env: dict):
        """
        Create a MultilspyConfig instance from a dictionary
        """
        processed_env = {}
        for k, v in env.items():
            if k in inspect.signature(cls).parameters:
                # Handle the nested JavaServerConfig dictionary
                if k == "java_server_config" and isinstance(v, dict):
                    processed_env[k] = JavaServerConfig.from_dict(v)
                else:
                    processed_env[k] = v
        return cls(**processed_env)