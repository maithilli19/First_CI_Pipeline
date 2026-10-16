import importlib
import pytest

# 1. Import the module by its file name (without .py)
module = importlib.import_module("25_max_min_list")

# 2. Take the required function from the module
find_max_min = module.find_max_min

def test_basic_max_min():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)

def test_single_element():
    assert find_max_min([42]) == (42, 42)

def test_negative_numbers():
    assert find_max_min([-5, -1, -10, -3]) == (-1, -10)

def test_empty_list_raises_error():
    with pytest.raises(ValueError):
        find_max_min([])