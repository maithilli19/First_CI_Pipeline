"""Program 26: Find the sum of elements in a list without using sum()."""

def sum_of_list(numbers):
    """Return the sum of all elements in the list using a loop.
    An empty list returns 0.
    """
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in user_input.split()]
    print("Sum:", sum_of_list(num_list))