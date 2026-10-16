import importlib

# 1. Import the module by its file name (without .py)
module = importlib.import_module("26_sum_of_list")

# 2. Take the required function from the module
sum_of_list = module.sum_of_list

def test_basic_sum():
    assert sum_of_list([1, 2, 3, 4]) == 10

def test_empty_list():
    assert sum_of_list([]) == 0

def test_single_element():
    assert sum_of_list([42]) == 42

def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6