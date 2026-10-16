import importlib

# 1. Import the module by its file name (without .py).
module = importlib.import_module("23_sort_without_sort")

# 2. Take the required function from the module.
bubble_sort = module.bubble_sort

def test_basic_sort():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_and_single():
    assert bubble_sort([]) == []
    assert bubble_sort([42]) == [42]

def test_does_not_modify_original():
    original = [3, 1, 4]
    sorted_result = bubble_sort(original)
    assert sorted_result == [1, 3, 4]
    assert original == [3, 1, 4]  # Original list remains unchanged