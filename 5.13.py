def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operator(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 // operand2  # Phép chia lấy phần nguyên

def infix_to_postfix(expression):
    stack = []  # Ngăn xếp chứa các toán tử
    output = []  # Kết quả dưới dạng hậu tố
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        if char.isdigit():
            num = 0
            # Xử lý số nhiều chữ số
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            output.append(num)
            continue
        
        elif char == '(':
            stack.append(char)
        
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Xóa dấu '(' khỏi stack
        
        else:  # Nếu là toán tử
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
        
        i += 1
    
    while stack:
        output.append(stack.pop())
    
    return output

def evaluate_postfix(postfix):
    stack = []
    
    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, token)
            stack.append(result)
    
    return stack[-1]

def main():
    T = int(input())
    for _ in range(T):
        expression = input().strip()
        postfix = infix_to_postfix(expression)
        result = evaluate_postfix(postfix)
        print(result)

if __name__ == "__main__":
    main()
