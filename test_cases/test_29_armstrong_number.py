import importlib

# 1. Import the module by its file name (without .py)
module = importlib.import_module("29_armstrong_number")

# 2. Take the required function from the module
is_armstrong = module.is_armstrong

def test_armstrong_true():
    assert is_armstrong(153) is True

def test_armstrong_false():
    assert is_armstrong(123) is False

def test_negative_number():
    assert is_armstrong(-153) is False

def test_single_digit():
    assert is_armstrong(5) is True