"""Program 27: Rotate a list by K positions."""

def rotate_list(items, k):
    """Rotate a list to the right by k positions and return a new list.
    k may be larger than the list length, and a negative k rotates left.
    Empty list returns [].
    """
    if not items:
        return []
        
    n = len(items)
    # Handle k larger than list length or negative k using modulo
    k = k % n
    
    # Slice and combine to rotate the list
    return items[-k:] + items[:-k]

if __name__ == "__main__":
    items_list = [1, 2, 3, 4, 5]
    k_val = 2
    print("Rotated list:", rotate_list(items_list, k_val))