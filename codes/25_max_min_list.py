"""Program 25: Find Maximum and Minimum in a List without max() or min()."""

def find_max_min(numbers):
    """Return a tuple (maximum, minimum) from the list.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")
        
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
    return (maximum, minimum)

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in user_input.split()]
    try:
        print("Max and Min:", find_max_min(num_list))
    except ValueError as e:
        print("Error:", e)
        