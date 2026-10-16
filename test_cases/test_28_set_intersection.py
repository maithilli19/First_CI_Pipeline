import importlib

# 1. Import the module by its file name (without .py)
module = importlib.import_module("28_set_intersection")

# 2. Take the required function from the module
set_intersection = module.set_intersection

def test_basic_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

def test_no_intersection():
    assert set_intersection({1, 2}, {3, 4}) == set()

def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}

def test_empty_sets():
    assert set_intersection(set(), {1, 2}) == set()
    assert set_intersection({1, 2}, set()) == set()