initialize_parameters = {
    "_description": "The parameters sent by the client when initializing the language server with the \"initialize\" request. More details at https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#initialize",
    "processId": "os.getpid()",
    "clientInfo": {
        "name": "Visual Studio Code - Insiders",
        "version": "1.77.0-insider"
    },
    "locale": "en",
    "rootPath": "repository_absolute_path",
    "rootUri": "pathlib.Path(repository_absolute_path).as_uri()",
    "capabilities": {
        "workspace": {
            "applyEdit": True,
            "workspaceEdit": {
                "documentChanges": True,
                "resourceOperations": [
                    "create",
                    "rename",
                    "delete"
                ],
                "failureHandling": "textOnlyTransactional",
                "normalizesLineEndings": True,
                "changeAnnotationSupport": {
                    "groupsOnLabel": True
                }
            },
            "didChangeConfiguration": {
                "dynamicRegistration": True
            },
            "didChangeWatchedFiles": {
                "dynamicRegistration": True,
                "relativePatternSupport": True
            },
            "symbol": {
                "dynamicRegistration": True,
                "symbolKind": {
                    "valueSet": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                        26
                    ]
                },
                "tagSupport": {
                    "valueSet": [
                        1
                    ]
                },
                "resolveSupport": {
                    "properties": [
                        "location.range"
                    ]
                }
            },
            "codeLens": {
                "refreshSupport": True
            },
            "executeCommand": {
                "dynamicRegistration": True
            },
            "configuration": True,
            "workspaceFolders": True,
            "semanticTokens": {
                "refreshSupport": True
            },
            "fileOperations": {
                "dynamicRegistration": True,
                "didCreate": True,
                "didRename": True,
                "didDelete": True,
                "willCreate": True,
                "willRename": True,
                "willDelete": True
            },
            "inlineValue": {
                "refreshSupport": True
            },
            "inlayHint": {
                "refreshSupport": True
            },
            "diagnostics": {
                "refreshSupport": True
            }
        },
        "textDocument": {
            "publishDiagnostics": {
                "relatedInformation": True,
                "versionSupport": False,
                "tagSupport": {
                    "valueSet": [
                        1,
                        2
                    ]
                },
                "codeDescriptionSupport": True,
                "dataSupport": True
            },
            "synchronization": {
                "dynamicRegistration": True,
                "willSave": True,
                "willSaveWaitUntil": True,
                "didSave": True
            },
            "completion": {
                "dynamicRegistration": True,
                "contextSupport": True,
                "completionItem": {
                    "snippetSupport": False,
                    "commitCharactersSupport": True,
                    "documentationFormat": [
                        "markdown",
                        "plaintext"
                    ],
                    "deprecatedSupport": True,
                    "preselectSupport": True,
                    "tagSupport": {
                        "valueSet": [
                            1
                        ]
                    },
                    "insertReplaceSupport": False,
                    "resolveSupport": {
                        "properties": [
                            "documentation",
                            "detail",
                            "additionalTextEdits"
                        ]
                    },
                    "insertTextModeSupport": {
                        "valueSet": [
                            1,
                            2
                        ]
                    },
                    "labelDetailsSupport": True
                },
                "insertTextMode": 2,
                "completionItemKind": {
                    "valueSet": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25
                    ]
                },
                "completionList": {
                    "itemDefaults": [
                        "commitCharacters",
                        "editRange",
                        "insertTextFormat",
                        "insertTextMode"
                    ]
                }
            },
            "hover": {
                "dynamicRegistration": True,
                "contentFormat": [
                    "markdown",
                    "plaintext"
                ]
            },
            "signatureHelp": {
                "dynamicRegistration": True,
                "signatureInformation": {
                    "documentationFormat": [
                        "markdown",
                        "plaintext"
                    ],
                    "parameterInformation": {
                        "labelOffsetSupport": True
                    },
                    "activeParameterSupport": True
                },
                "contextSupport": True
            },
            "definition": {
                "dynamicRegistration": True,
                "linkSupport": True
            },
            "references": {
                "dynamicRegistration": True
            },
            "documentHighlight": {
                "dynamicRegistration": True
            },
            "documentSymbol": {
                "dynamicRegistration": True,
                "symbolKind": {
                    "valueSet": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                        26
                    ]
                },
                "hierarchicalDocumentSymbolSupport": True,
                "tagSupport": {
                    "valueSet": [
                        1
                    ]
                },
                "labelSupport": True
            },
            "codeAction": {
                "dynamicRegistration": True,
                "isPreferredSupport": True,
                "disabledSupport": True,
                "dataSupport": True,
                "resolveSupport": {
                    "properties": [
                        "edit"
                    ]
                },
                "codeActionLiteralSupport": {
                    "codeActionKind": {
                        "valueSet": [
                            "",
                            "quickfix",
                            "refactor",
                            "refactor.extract",
                            "refactor.inline",
                            "refactor.rewrite",
                            "source",
                            "source.organizeImports"
                        ]
                    }
                },
                "honorsChangeAnnotations": False
            },
            "codeLens": {
                "dynamicRegistration": True
            },
            "formatting": {
                "dynamicRegistration": True
            },
            "rangeFormatting": {
                "dynamicRegistration": True
            },
            "onTypeFormatting": {
                "dynamicRegistration": True
            },
            "rename": {
                "dynamicRegistration": True,
                "prepareSupport": True,
                "prepareSupportDefaultBehavior": 1,
                "honorsChangeAnnotations": True
            },
            "documentLink": {
                "dynamicRegistration": True,
                "tooltipSupport": True
            },
            "typeDefinition": {
                "dynamicRegistration": True,
                "linkSupport": True
            },
            "implementation": {
                "dynamicRegistration": True,
                "linkSupport": True
            },
            "colorProvider": {
                "dynamicRegistration": True
            },
            "foldingRange": {
                "dynamicRegistration": True,
                "rangeLimit": 5000,
                "lineFoldingOnly": True,
                "foldingRangeKind": {
                    "valueSet": [
                        "comment",
                        "imports",
                        "region"
                    ]
                },
                "foldingRange": {
                    "collapsedText": False
                }
            },
            "declaration": {
                "dynamicRegistration": True,
                "linkSupport": True
            },
            "selectionRange": {
                "dynamicRegistration": True
            },
            "callHierarchy": {
                "dynamicRegistration": True
            },
            "semanticTokens": {
                "dynamicRegistration": True,
                "tokenTypes": [
                    "namespace",
                    "type",
                    "class",
                    "enum",
                    "interface",
                    "struct",
                    "typeParameter",
                    "parameter",
                    "variable",
                    "property",
                    "enumMember",
                    "event",
                    "function",
                    "method",
                    "macro",
                    "keyword",
                    "modifier",
                    "comment",
                    "string",
                    "number",
                    "regexp",
                    "operator",
                    "decorator"
                ],
                "tokenModifiers": [
                    "declaration",
                    "definition",
                    "readonly",
                    "static",
                    "deprecated",
                    "abstract",
                    "async",
                    "modification",
                    "documentation",
                    "defaultLibrary"
                ],
                "formats": [
                    "relative"
                ],
                "requests": {
                    "range": True,
                    "full": {
                        "delta": True
                    }
                },
                "multilineTokenSupport": False,
                "overlappingTokenSupport": False,
                "serverCancelSupport": True,
                "augmentsSyntaxTokens": True
            },
            "linkedEditingRange": {
                "dynamicRegistration": True
            },
            "typeHierarchy": {
                "dynamicRegistration": True
            },
            "inlineValue": {
                "dynamicRegistration": True
            },
            "inlayHint": {
                "dynamicRegistration": True,
                "resolveSupport": {
                    "properties": [
                        "tooltip",
                        "textEdits",
                        "label.tooltip",
                        "label.location",
                        "label.command"
                    ]
                }
            },
            "diagnostic": {
                "dynamicRegistration": True,
                "relatedDocumentSupport": False
            }
        },
        "window": {
            "showMessage": {
                "messageActionItem": {
                    "additionalPropertiesSupport": True
                }
            },
            "showDocument": {
                "support": True
            },
            "workDoneProgress": True
        },
        "general": {
            "staleRequestSupport": {
                "cancel": True,
                "retryOnContentModified": [
                    "textDocument/semanticTokens/full",
                    "textDocument/semanticTokens/range",
                    "textDocument/semanticTokens/full/delta"
                ]
            },
            "regularExpressions": {
                "engine": "ECMAScript",
                "version": "ES2020"
            },
            "markdown": {
                "parser": "marked",
                "version": "1.1.0"
            },
            "positionEncodings": [
                "utf-16"
            ]
        },
        "notebookDocument": {
            "synchronization": {
                "dynamicRegistration": True,
                "executionSummarySupport": True
            }
        }
    },
    "initializationOptions": {
        "workspaceFolders": "[pathlib.Path(repository_absolute_path).as_uri()]",
        "settings": {
            "java": {
                "home": None,
                "jdt": {
                    "ls": {
                        "java": {
                            "home": None
                        },
                        "vmargs": "-XX:+UseParallelGC -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90 -Dsun.zip.disableMemoryMapping=True -Xmx8G -Xms2G -Xlog:disable",
                        "lombokSupport": {
                            "enabled": True
                        },
                        "protobufSupport": {
                            "enabled": True
                        },
                        "androidSupport": {
                            "enabled": True
                        }
                    }
                },
                "errors": {
                    "incompleteClasspath": {
                        "severity": "error"
                    }
                },
                "configuration": {
                    "checkProjectSettingsExclusions": False,
                    "updateBuildConfiguration": "interactive",
                    "maven": {
                        "userSettings": None,
                        "globalSettings": None,
                        "notCoveredPluginExecutionSeverity": "warning",
                        "defaultMojoExecutionAction": "ignore"
                    },
                    "workspaceCacheLimit": 90,
                    "runtimes": [
                        {
                            "name": "JavaSE-17",
                            "path": "static/vscode-java/extension/jre/17.0.8.1-linux-x86_64",
                            "default": True
                        }
                    ]
                },
                "trace": {
                    "server": "verbose"
                },
                "import": {
                    "maven": {
                        "enabled": True,
                        "offline": {
                            "enabled": False
                        },
                        "disableTestClasspathFlag": False
                    },
                    "gradle": {
                        "enabled": True,
                        "wrapper": {
                            "enabled": True
                        },
                        "version": None,
                        "home": "abs(static/gradle-7.3.3)",
                        "java": {
                            "home": "abs(static/launch_jres/17.0.6-linux-x86_64)"
                        },
                        "offline": {
                            "enabled": False
                        },
                        "arguments": None,
                        "jvmArguments": None,
                        "user": {
                            "home": None
                        },
                        "annotationProcessing": {
                            "enabled": True
                        }
                    },
                    "exclusions": [
                        "**/node_modules/**",
                        "**/.metadata/**",
                        "**/archetype-resources/**",
                        "**/META-INF/maven/**"
                    ],
                    "generatesMetadataFilesAtProjectRoot": False
                },
                "maven": {
                    "downloadSources": True,
                    "updateSnapshots": True
                },
                "eclipse": {
                    "downloadSources": True
                },
                "referencesCodeLens": {
                    "enabled": True
                },
                "signatureHelp": {
                    "enabled": True,
                    "description": {
                        "enabled": True
                    }
                },
                "implementationsCodeLens": {
                    "enabled": True
                },
                "format": {
                    "enabled": True,
                    "settings": {
                        "url": None,
                        "profile": None
                    },
                    "comments": {
                        "enabled": True
                    },
                    "onType": {
                        "enabled": True
                    },
                    "insertSpaces": True,
                    "tabSize": 4
                },
                "saveActions": {
                    "organizeImports": False
                },
                "project": {
                    "referencedLibraries": [
                        "lib/**/*.jar"
                    ],
                    "importOnFirstTimeStartup": "automatic",
                    "importHint": True,
                    "resourceFilters": [
                        "node_modules",
                        "\\.git"
                    ],
                    "encoding": "ignore",
                    "exportJar": {
                        "targetPath": "${workspaceFolder}/${workspaceFolderBasename}.jar"
                    }
                },
                "contentProvider": {
                    "preferred": None
                },
                "autobuild": {
                    "enabled": True
                },
                "maxConcurrentBuilds": 1,
                "recommendations": {
                    "dependency": {
                        "analytics": {
                            "show": True
                        }
                    }
                },
                "completion": {
                    "maxResults": 0,
                    "enabled": True,
                    "guessMethodArguments": True,
                    "favoriteStaticMembers": [
                        "org.junit.Assert.*",
                        "org.junit.Assume.*",
                        "org.junit.jupiter.api.Assertions.*",
                        "org.junit.jupiter.api.Assumptions.*",
                        "org.junit.jupiter.api.DynamicContainer.*",
                        "org.junit.jupiter.api.DynamicTest.*",
                        "org.mockito.Mockito.*",
                        "org.mockito.ArgumentMatchers.*",
                        "org.mockito.Answers.*"
                    ],
                    "filteredTypes": [
                        "java.awt.*",
                        "com.sun.*",
                        "sun.*",
                        "jdk.*",
                        "org.graalvm.*",
                        "io.micrometer.shaded.*"
                    ],
                    "importOrder": [
                        "#",
                        "java",
                        "javax",
                        "org",
                        "com",
                        ""
                    ],
                    "postfix": {
                        "enabled": False
                    },
                    "matchCase": "off"
                },
                "foldingRange": {
                    "enabled": True
                },
                "progressReports": {
                    "enabled": False
                },
                "codeGeneration": {
                    "hashCodeEquals": {
                        "useJava7Objects": False,
                        "useInstanceof": False
                    },
                    "useBlocks": False,
                    "generateComments": False,
                    "toString": {
                        "template": "${object.className} [${member.name()}=${member.value}, ${otherMembers}]",
                        "codeStyle": "STRING_CONCATENATION",
                        "skipNullValues": False,
                        "listArrayContents": True,
                        "limitElements": 0
                    },
                    "insertionLocation": "afterCursor"
                },
                "selectionRange": {
                    "enabled": True
                },
                "showBuildStatusOnStart": {
                    "enabled": "notification"
                },
                "server": {
                    "launchMode": "Standard"
                },
                "sources": {
                    "organizeImports": {
                        "starThreshold": 99,
                        "staticStarThreshold": 99
                    }
                },
                "imports": {
                    "gradle": {
                        "wrapper": {
                            "checksums": []
                        }
                    }
                },
                "templates": {
                    "fileHeader": [],
                    "typeComment": []
                },
                "references": {
                    "includeAccessors": True,
                    "includeDecompiledSources": True
                },
                "typeHierarchy": {
                    "lazyLoad": False
                },
                "settings": {
                    "url": None
                },
                "symbols": {
                    "includeSourceMethodDeclarations": False
                },
                "quickfix": {
                    "showAt": "line"
                },
                "inlayHints": {
                    "parameterNames": {
                        "enabled": "literals",
                        "exclusions": []
                    }
                },
                "codeAction": {
                    "sortMembers": {
                        "avoidVolatileChanges": True
                    }
                },
                "compile": {
                    "nullAnalysis": {
                        "nonnull": [
                            "javax.annotation.Nonnull",
                            "org.eclipse.jdt.annotation.NonNull",
                            "org.springframework.lang.NonNull"
                        ],
                        "nullable": [
                            "javax.annotation.Nullable",
                            "org.eclipse.jdt.annotation.Nullable",
                            "org.springframework.lang.Nullable"
                        ],
                        "mode": "automatic"
                    }
                },
                "cleanup": {
                    "actionsOnSave": []
                },
                "sharedIndexes": {
                    "enabled": "auto",
                    "location": ""
                },
                "refactoring": {
                    "extract": {
                        "interface": {
                            "replace": True
                        }
                    }
                },
                "debug": {
                    "logLevel": "verbose",
                    "settings": {
                        "showHex": False,
                        "showStaticVariables": False,
                        "showQualifiedNames": False,
                        "showLogicalStructure": True,
                        "showToString": True,
                        "maxStringLength": 0,
                        "numericPrecision": 0,
                        "hotCodeReplace": "manual",
                        "enableRunDebugCodeLens": True,
                        "forceBuildBeforeLaunch": True,
                        "onBuildFailureProceed": False,
                        "console": "integratedTerminal",
                        "exceptionBreakpoint": {
                            "skipClasses": []
                        },
                        "stepping": {
                            "skipClasses": [],
                            "skipSynthetics": False,
                            "skipStaticInitializers": False,
                            "skipConstructors": False
                        },
                        "jdwp": {
                            "limitOfVariablesPerJdwpRequest": 100,
                            "requestTimeout": 3000,
                            "async": "auto"
                        },
                        "vmArgs": ""
                    }
                },
                "silentNotification": False,
                "dependency": {
                    "showMembers": False,
                    "syncWithFolderExplorer": True,
                    "autoRefresh": True,
                    "refreshDelay": 2000,
                    "packagePresentation": "flat"
                },
                "help": {
                    "firstView": "auto",
                    "showReleaseNotes": True,
                    "collectErrorLog": False
                },
                "test": {
                    "defaultConfig": "",
                    "config": {}
                }
            }
        },
        "extendedClientCapabilities": {
            "progressReportProvider": False,
            "classFileContentsSupport": True,
            "overrideMethodsPromptSupport": True,
            "hashCodeEqualsPromptSupport": True,
            "advancedOrganizeImportsSupport": True,
            "generateToStringPromptSupport": True,
            "advancedGenerateAccessorsSupport": True,
            "generateConstructorsPromptSupport": True,
            "generateDelegateMethodsPromptSupport": True,
            "advancedExtractRefactoringSupport": True,
            "inferSelectionSupport": [
                "extractMethod",
                "extractVariable",
                "extractField"
            ],
            "moveRefactoringSupport": True,
            "clientHoverProvider": True,
            "clientDocumentSymbolProvider": True,
            "gradleChecksumWrapperPromptSupport": True,
            "resolveAdditionalTextEditsSupport": True,
            "advancedIntroduceParameterRefactoringSupport": True,
            "actionableRuntimeNotificationSupport": True,
            "shouldLanguageServerExitOnShutdown": True,
            "onCompletionItemSelectedCommand": "editor.action.triggerParameterHints",
            "extractInterfaceSupport": True,
            "advancedUpgradeGradleSupport": True
        },
        "triggerFiles": []
    },
    "trace": "verbose",
    "workspaceFolders": "[\n            {\n                \"uri\": pathlib.Path(repository_absolute_path).as_uri(),\n                \"name\": os.path.basename(repository_absolute_path),\n            }\n        ]"
}