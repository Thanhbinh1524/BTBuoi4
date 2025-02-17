def longest_valid_parentheses(s):
    # Stack lưu các chỉ số của '(' và dấu ngăn cách
    stack = [-1]
    max_len = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
    
    return max_len

def main():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        result = longest_valid_parentheses(s)
        print(result)

if __name__ == "__main__":
    main()
