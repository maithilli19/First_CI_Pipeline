"""Program 29: Check Armstrong Number."""

def is_armstrong(number):
    """Return True if the number is an Armstrong number, False otherwise.
    Negative numbers return False.
    """
    if number < 0:
        return False
        
    num_str = str(number)
    num_digits = len(num_str)
    
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    print("Is Armstrong?", is_armstrong(num))