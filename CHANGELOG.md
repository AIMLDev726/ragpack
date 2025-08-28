# Changelog

All notable changes to ragpackai will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2025-08-28

### Added
- Initial release of ragpackai
- Core ragpackai class with `from_files`, `save`, `load`, `query`, and `ask` methods
- Support for multiple embedding providers (OpenAI, HuggingFace, Google)
- Support for multiple LLM providers (OpenAI, Google, Groq, Cerebras)
- Portable .rag file format with zip-based storage
- Optional AES-GCM encryption for sensitive data
- Runtime provider overrides without rebuilding packs
- Command-line interface for pack management
- Support for PDF, TXT, and MD document formats
- Lazy loading of optional dependencies
- Comprehensive examples and documentation

### Features
- **Portable RAG Packs**: Bundle documents, embeddings, and vectorstores into single .rag files
- **Provider Flexibility**: Easy switching between different embedding and LLM providers
- **Encryption Support**: Secure your sensitive data with password-based encryption
- **Runtime Overrides**: Change providers without rebuilding your packs
- **CLI Tools**: Command-line interface for creating, querying, and managing packs
- **Multiple Formats**: Support for various document formats including PDF processing

### Supported Providers
- **Embeddings**: OpenAI (text-embedding-3-small/large), HuggingFace (offline models), Google (textembedding-gecko)
- **LLMs**: OpenAI (GPT-4o, GPT-3.5-turbo), Google (Gemini), Groq (Mixtral, Llama), Cerebras (Llama models)

### Dependencies
- Core: langchain, chromadb, openai, sentence-transformers, faiss-cpu
- Optional: Provider-specific packages installed as extras