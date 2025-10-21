#!/usr/bin/env python3
"""
Sample Python application to test the development environment setup.
"""


def greet(name: str) -> str:
    """Greet a person by name.

    Args:
        name: The name of the person to greet

    Returns:
        A greeting message
    """
    return f"Hello, {name}!"


def main() -> None:
    """Main function to run the application."""
    print(greet("World"))
    print("Python environment is set up correctly!")


if __name__ == "__main__":
    main()
