def simplify_expression(expr):
    stack = []
    sign = 1  # Dấu hiện tại, 1: dương, -1: âm
    result = []
    stack_sign = [1]  # Stack lưu dấu
    
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
    # Xóa dấu '+' không cần thiết
    for i, c in enumerate(result):
        if i == 0 and c == '+':
            continue
        if c == '+' and (i == 0 or result[i - 1] in '+-'):
            continue
        simplified.append(c)
    return ''.join(simplified)


def expressions_equal(P1, P2):
    return simplify_expression(P1) == simplify_expression(P2)


T = int(input())
for _ in range(T):
    P1 = input().strip()
    P2 = input().strip()
    print("YES" if expressions_equal(P1, P2) else "NO")
