"""Program 30: Convert Decimal to Binary Without Using bin()."""

def decimal_to_binary(number):
    """Convert a decimal integer to a binary string using repeated division by 2.
    0 returns "0"; a negative number raises ValueError.
    """
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
        
    if number == 0:
        return "0"
        
    binary_digits = []
    n = number
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
        
    # Reverse the digits since remainders are collected from least significant to most
    return "".join(reversed(binary_digits))

if __name__ == "__main__":
    num = int(input("Enter a decimal number: "))
    try:
        print("Binary:", decimal_to_binary(num))
    except ValueError as e:
        print("Error:", e)