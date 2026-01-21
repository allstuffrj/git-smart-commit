# Contributing to git-smart-commit

First off, thank you for considering contributing! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include:

- **Clear title** describing the issue
- **Steps to reproduce** the behavior
- **Expected behavior** 
- **Actual behavior**
- **Your environment** (OS, Python version, Git version)
- **Screenshots** if applicable

### Suggesting Features

Feature suggestions are welcome! Please:

- **Use a clear title** for the suggestion
- **Provide detailed description** of the feature
- **Explain why it would be useful** to most users
- **List alternatives** you've considered

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Write clear commit messages (use git-smart-commit! 😉)
6. Update documentation as needed

## Development Setup

```bash
# Clone your fork
git clone https://github.com/allstuffrj/git-smart-commit.git
cd git-smart-commit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Comment complex logic

## Testing

```bash
# Run tests (when implemented)
python -m pytest

# Run with coverage
python -m pytest --cov=git_smart_commit
```

## Questions?

Feel free to open an issue with your question!
