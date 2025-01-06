UPPER_LOWER_CASE_LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def is_valid_string(s):
    for char in s:
        result = (char in UPPER_LOWER_CASE_LETTER)
        if result is False:
            return False
    return True

def main():
    input_str = input()
    is_valid = is_valid_string(input_str)

    if is_valid:
        result = "True " + str(len([char for char in input_str if char.isupper()]))
    else:
        result = "False"
    print(result)

main()