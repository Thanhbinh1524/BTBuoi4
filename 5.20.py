def decode_string(encoded_str):
    stack = []
    current_num = 0
    current_str = ""

    for char in encoded_str:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append(current_str)
            stack.append(current_num)
            current_str = ""
            current_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str

# Input number of test cases
T = int(input())
for _ in range(T):
    encoded_str = input().strip()
    print(decode_string(encoded_str))