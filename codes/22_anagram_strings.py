def is_anagram(first, second):
    """Return True if first and second are anagrams, False otherwise.
    Ignores spaces and case sensitivity.
    """
    # Remove spaces and convert both strings to lowercase
    clean_first = "".join(first.lower().split())
    clean_second = "".join(second.lower().split())
    
    # Compare sorted characters
    return sorted(clean_first) == sorted(clean_second)

if __name__ == "__main__":
    f_str = input("Enter first string: ")
    s_str = input("Enter second string: ")
    print("Are they anagrams?", is_anagram(f_str, s_str))