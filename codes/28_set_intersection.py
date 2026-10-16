"""Program 28: Find the Intersection of Two Sets."""

def set_intersection(first, second):
    """Return a set with only the elements present in both sets."""
    return set(first) & set(second)

if __name__ == "__main__":
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print("Intersection:", set_intersection(s1, s2))