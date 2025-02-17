def longest_valid_parentheses(s):
    stack = [-1]  # Ngăn xếp để lưu chỉ số, bắt đầu với -1 để tính các biểu thức đúng từ đầu
    total_length = 0  # Biến để lưu tổng độ dài của các biểu thức đúng
    
    for i in range(len(s)):
        if s[i] == '(':  # Nếu là dấu '(' thì đẩy chỉ số vào ngăn xếp
            stack.append(i)
        else:  # Nếu là dấu ')'
            stack.pop()  # Pop phần tử đầu tiên trong ngăn xếp (dấu '(' trước đó)
            if stack:
                # Nếu ngăn xếp không rỗng, tính độ dài biểu thức đúng
                total_length += (i - stack[-1])
            else:
                # Nếu ngăn xếp rỗng, đẩy chỉ số của ')' vào ngăn xếp để bắt đầu một chuỗi mới
                stack.append(i)
    
    return total_length

def main():
    T = int(input())  # Số bộ test
    for _ in range(T):
        P = input().strip()  # Biểu thức P
        result = longest_valid_parentheses(P)
        print(result)

if __name__ == "__main__":
    main()
