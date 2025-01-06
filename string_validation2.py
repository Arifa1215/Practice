UPPERCASE_LETTER = "abcdefghijklmnopqrstuvwxyz"

def is_valid_string(s):
    for char in s:
        result = (char in UPPERCASE_LETTER) or (char == "_")
        if result is False:
            return False
    return True

def main():
    input_str = input()
    is_valid = is_valid_string(input_str)

    if is_valid:
        result = "True " + str(len(input_str.split("_")))
    else:
        result = "False"
    print(result)

main()