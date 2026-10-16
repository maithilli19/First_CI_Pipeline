import importlib

# Import the module by its file name (without .py) using importlib
module = importlib.import_module("22_anagram_strings")

# Get the required function from the module
is_anagram = module.is_anagram

def test_basic_anagram():
    assert is_anagram("listen", "silent") is True

def test_not_anagram():
    assert is_anagram("hello", "world") is False

def test_ignores_case_and_spaces():
    assert is_anagram("Astronomer", "Moon starer") is True

def test_different_lengths():
    assert is_anagram("python", "pythons") is False