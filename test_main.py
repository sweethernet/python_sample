#!/usr/bin/env python3
"""
Test file for the Python sample application.
"""

import pytest
from main import greet


def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Python") == "Hello, Python!"


def test_greet_empty():
    """Test the greet function with empty string."""
    assert greet("") == "Hello, !"


if __name__ == "__main__":
    pytest.main([__file__])
