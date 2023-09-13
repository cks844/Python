""" Python code for replacing the vowels in a string with 3"""

def replace_vowels_with_3(input_str):
    vowels = "AEIOUaeiou"
    result = ""
    for char in input_str:
        if char in vowels:
            result += '3'
        else:
            result += char
    return result
