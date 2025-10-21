# Python Sample Project

This is a sample Python project with a configured development environment.

## Project Structure

```
.
├── .venv/                 # Python virtual environment
├── .zed/                  # Zed editor configuration
├── main.py                # Main application file
├── test_main.py           # Test file
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Virtual Environment Setup

A Python virtual environment has been created in the `.venv` directory. This environment contains:

- `black` - Code formatter
- `flake8` - Linter
- `pytest` - Testing framework
- `mypy` - Type checker

## Zed Configuration

The `.zed/settings.json` file is configured to use the virtual environment's Python interpreter at `.venv/bin/python`. This ensures that:

- Language features work correctly with the project's dependencies
- Auto-completion and linting use the correct Python environment
- Type checking is properly configured

## Usage

To use this project in Zed:

1. Open the project in Zed
2. The editor should automatically detect and use the virtual environment
3. You can run tests with `pytest test_main.py`
4. Format code with `black .`
5. Lint code with `flake8 .`
6. Type check with `mypy .`

## Development Commands

```bash
# Run tests
pytest test_main.py

# Format code
black .

# Lint code
flake8 .

# Type check
mypy .

# Install new dependencies
.venv/bin/pip install <package-name>
```
