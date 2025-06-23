[![PyPI - Version](https://img.shields.io/pypi/v/multilspy)](https://pypi.org/project/multilspy/)
# Multilspy: LSP client library in Python to build applications around language servers

## Introduction
This repository hosts `multilspy`, a library developed as part of research conducted for NeruIPS 2023 paper titled ["Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context"](https://neurips.cc/virtual/2023/poster/70362) (["Guiding Language Models of Code with Global Context using Monitors"](https://arxiv.org/abs/2306.10763) on Arxiv). The paper introduces Monitor-Guided Decoding (MGD) for code generation using Language Models, where a monitor uses static analysis to guide the decoding, ensuring that the generated code follows various correctness properties, like absence of hallucinated symbol names, valid order of method calls, etc. For further details about Monitor-Guided Decoding, please refer to the paper and GitHub repository [microsoft/monitors4codegen](https://github.com/microsoft/monitors4codegen).

`multilspy` is a cross-platform library designed to simplify the process of creating language server clients to query and obtain results of various static analyses from a wide variety of language servers that communicate over the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/). It is easily extensible to support any [language that has a Language Server](https://microsoft.github.io/language-server-protocol/implementors/servers/) and currently supports Java, Rust, C# and Python. We aim to continuously add support for more language servers and languages.

[Language servers]((https://microsoft.github.io/language-server-protocol/overviews/lsp/overview/)) are tools that perform a variety of static analyses on code repositories and provide useful information such as type-directed code completion suggestions, symbol definition locations, symbol references, etc., over the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/overviews/lsp/overview/). Since LSP is language-agnostic, `multilspy` can provide the results for static analyses of code in different languages over a common interface.

`multilspy` intends to ease the process of using language servers, by handling various steps in using a language server:
* Automatically handling the download of platform-specific server binaries, and setup/teardown of language servers
* Handling JSON-RPC based communication between the client and the server
* Maintaining and passing hand-tuned server and language specific configuration parameters
* Providing a simple API to the user, while executing all steps of server-specific protocol steps to execute the query/request.

Some of the analysis results that `multilspy` can provide are:
- Finding the definition of a function or a class ([textDocument/definition](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition))
- Finding the callers of a function or the instantiations of a class ([textDocument/references](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references))
- Providing type-based dereference completions ([textDocument/completion](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_completion))
- Getting information displayed when hovering over symbols, like method signature ([textDocument/hover](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_hover))
- Getting list/tree of all symbols defined in a given file, along with symbol type like class, method, etc. ([textDocument/documentSymbol](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol))
- Please create an issue/PR to add any other LSP request not listed above

## Installation
It is ideal to create a new virtual environment with `python>=3.10`. To create a virtual environment using conda and activate it:
```
conda create -n multilspy_env python=3.10
conda activate multilspy_env
```
Further details and instructions on creation of Python virtual environments can be found in the [official documentation](https://docs.python.org/3/library/venv.html). Further, we also refer users to [Miniconda](https://docs.conda.io/en/latest/miniconda.html), as an alternative to the above steps for creation of the virtual environment.

To install `multilspy` using pip, execute the following command:
```
pip install multilspy
```

## Usage
Example usage:
```python
from multilspy import SyncLanguageServer
from multilspy.multilspy_config import MultilspyConfig
from multilspy.multilspy_logger import MultilspyLogger
...
config = MultilspyConfig.from_dict({"code_language": "java"}) # Also supports "python", "rust", "csharp"
logger = MultilspyLogger()
lsp = SyncLanguageServer.create(config, logger, "/abs/path/to/project/root/")
with lsp.start_server():
    result = lsp.request_definition(
        "relative/path/to/code_file.java", # Filename of location where request is being made
        163, # line number of symbol for which request is being made
        4 # column number of symbol for which request is being made
    )
    result2 = lsp.request_completions(
        ...
    )
    result3 = lsp.request_references(
        ...
    )
    result4 = lsp.request_document_symbols(
        ...
    )
    result5 = lsp.request_hover(
        ...
    )
    ...
```

`multilspy` also provides an asyncio based API which can be used in async contexts. Example usage (asyncio):
```python
from multilspy import LanguageServer
...
lsp = LanguageServer.create(...)
async with lsp.start_server():
    result = await lsp.request_definition(
        ...
    )
    ...
```

The file [src/multilspy/language_server.py](src/multilspy/language_server.py) provides the `multilspy` API. Several tests for `multilspy` present under [tests/multilspy/](tests/multilspy/) provide detailed usage examples for `multilspy`. The tests can be executed by running:
```bash
pytest tests/multilspy
```

## Fork Notice

This repository is a fork and modified version of the original [`multilspy`](https://github.com/microsoft/multilspy) repository. It contains changes and enhancements that may not be present in the upstream version.

