"""Program 24: Merge two sorted lists into one sorted list."""

def merge_sorted_lists(list1, list2):
    """Merge two already sorted lists into a single sorted list."""
    merged = []
    i = 0
    j = 0
    
    # Compare elements from both lists and append the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            
    # Append any remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

if __name__ == "__main__":
    l1 = [1, 3, 5]
    l2 = [2, 4]
    print("Merged list:", merge_sorted_lists(l1, l2))