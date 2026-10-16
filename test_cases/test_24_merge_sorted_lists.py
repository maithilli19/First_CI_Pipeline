import importlib

# 1. Import the module by its file name (without .py)
module = importlib.import_module("24_merge_sorted_lists")

# 2. Take the required function from the module
merge_sorted_lists = module.merge_sorted_lists

def test_basic_merge():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]

def test_empty_lists():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([], []) == []

def test_different_lengths():
    assert merge_sorted_lists([1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]