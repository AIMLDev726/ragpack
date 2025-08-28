# Contributing to ragpackai

We welcome contributions to ragpackai! This document provides guidelines for contributing to the project.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/AIMLDev726/ragpackai.git
   cd ragpackai
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

### Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **MyPy**: Type checking

Run these tools before submitting:
```bash
black ragpackai tests examples
flake8 ragpackai tests examples
mypy ragpackai
```

### Testing

Run the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=ragpackai --cov-report=html
```

### Adding New Features

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Implement your changes
3. Add tests for new functionality
4. Update documentation if needed
5. Ensure all tests pass
6. Submit a pull request

### Adding New Providers

To add support for a new embedding or LLM provider:

1. Create wrapper classes in `ragpackai/embeddings/` or `ragpackai/llms/`
2. Update the provider configuration in `ragpackai/providers.py`
3. Add the provider to optional dependencies in `pyproject.toml`
4. Add tests and examples
5. Update documentation

## Pull Request Process

1. Ensure your code follows the style guidelines
2. Add or update tests as appropriate
3. Update documentation for any new features
4. Ensure all tests pass
5. Update CHANGELOG.md with your changes
6. Submit a pull request with a clear description

### Pull Request Guidelines

- Use a clear and descriptive title
- Describe what changes you made and why
- Reference any related issues
- Include screenshots for UI changes
- Keep pull requests focused and atomic

## Issue Reporting

When reporting issues:

1. Use the issue templates when available
2. Provide a clear description of the problem
3. Include steps to reproduce the issue
4. Provide system information (OS, Python version, etc.)
5. Include relevant error messages and stack traces

## Code of Conduct

This project follows a Code of Conduct. By participating, you agree to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other community members

## Questions?

If you have questions about contributing, feel free to:

- Open an issue for discussion
- Reach out to the maintainers
- Join our community discussions

Thank you for contributing to ragpackai!