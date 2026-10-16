"""Program 23: Sort a list without using sort() or sorted()."""

def bubble_sort(numbers):
    """Return a new sorted list in ascending order using bubble sort logic.
    Does not modify the original list.
    """
    # Create a copy so we don't alter the original list
    arr = list(numbers)
    n = len(arr)
    
    # Bubble sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in user_input.split()]
    print("Sorted list:", bubble_sort(num_list))