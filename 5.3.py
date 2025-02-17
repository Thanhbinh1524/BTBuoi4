def simplify_expression(expr):
    stack = []
    result = []
    sign = 1  # 1: dấu dương, -1: dấu âm
    current_sign = [1]  # stack lưu dấu hiệu hiện tại
    
    for char in expr:
        if char == '+':
            result.append('+' if sign == 1 else '-')
        elif char == '-':
            result.append('-' if sign == 1 else '+')
        elif char == '(':
            stack.append(sign)
        elif char == ')':
            stack.pop()
        else:
            result.append(char)
        
        if char in '+-':
            sign = stack[-1] if stack else 1

    simplified = []
    # Xử lý dấu để loại bỏ dấu '+'' không cần thiết
    for i, c in enumerate(result):
        if i == 0 and c == '+':
            continue
        if c == '+' and (i == 0 or result[i - 1] in '+-'):
            continue
        simplified.append(c)
    return ''.join(simplified)


t = int(input())
for _ in range(t):
    expr = input().strip()
    # Thay thế các dấu '-' và '+'
    expr = expr.replace(' ', '')
    stack = []
    sign = 1
    res = []
    for char in expr:
        if char == '(':
            stack.append(sign)
        elif char == ')':
            stack.pop()
        elif char == '-':
            sign = -sign
            res.append('-' if sign == 1 else '+')
        elif char == '+':
            res.append('+')
        else:
            res.append(char)
    # Xóa dấu '+' dư thừa đầu chuỗi
    ans = ''.join(res)
    if ans.startswith('+'):
        ans = ans[1:]
    print(ans)
