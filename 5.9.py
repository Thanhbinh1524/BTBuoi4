def is_operator(c):
    return c in ['+', '-', '*', '/']

def postfix_to_prefix(exp):
    stack = []
    # Duyệt từ trái sang phải
    for ch in exp:
        if not is_operator(ch):
            stack.append(ch)
        else:
            # Lấy 2 toán hạng từ stack
            op2 = stack.pop()
            op1 = stack.pop()
            # Ghép lại thành biểu thức tiền tố
            stack.append(ch + op1 + op2)
    return stack[-1]

t = int(input())
for _ in range(t):
    exp = input().strip()
    print(postfix_to_prefix(exp))
