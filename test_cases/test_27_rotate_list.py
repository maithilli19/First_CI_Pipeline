import importlib

# 1. Import the module by its file name (without .py)
module = importlib.import_module("27_rotate_list")

# 2. Take the required function from the module
rotate_list = module.rotate_list

def test_basic_rotate():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_empty_list():
    assert rotate_list([], 3) == []

def test_negative_k():
    assert rotate_list([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]

def test_k_larger_than_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]