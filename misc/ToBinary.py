# Explanation of the process:
# For each character in the input string:
# 1. Convert the character to its Unicode code point using ord().
# 2. Format the code point as an 8-bit binary number using format() with '08b'.
# 3. Join all binary numbers into a single string, separated by spaces.

# Example:
# 'H' -> ord('H') -> 72 -> format(72, '08b') -> '01001000'
# 'i' -> ord('i') -> 105 -> format(105, '08b') -> '01101001'
# ' ' (space) -> ord(' ') -> 32 -> format(32, '08b') -> '00100000'

# Format specifier details:
# '0' - Pads the binary number with leading zeros.
# '8' - Ensures the binary number is 8 bits wide.
# 'b' - Indicates that the number should be formatted as binary.

def string_to_binary(input_string):
    # Convert each character in the string to its binary representation
    binary_string = ' '.join(format(ord(char), '08b') for char in input_string)
    return binary_string

# Example usage
input_string = input("enter a string to be converted to binary: ")
binary_representation = string_to_binary(input_string)
print("Original String:", input_string)
print("Binary Representation:", binary_representation)