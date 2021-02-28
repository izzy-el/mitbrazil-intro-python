import string

def caesar_cipher(original_string, shift):
    result = ''
    shift_number = shift
    lower_case_string = original_string.lower()
    
    if shift > 25 or shift < 0:
        shift %= 26
    if shift_number > 9:
        shift_number % 10

    for char in lower_case_string:
        if char in string.ascii_lowercase:
            result += string.ascii_lowercase[(string.ascii_lowercase.find(char) + shift) % 26]
        elif char in string.digits:
            result += string.digits[(string.digits.find(char) + shift_number) % 10]
        else:
            result += char

    return result