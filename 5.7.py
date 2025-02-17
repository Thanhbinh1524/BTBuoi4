def is_operator(c):
    return c in ['+', '-', '*', '/']

def prefix_to_infix(exp):
    stack = []
    # Duyệt ngược chuỗi biểu thức
    for ch in exp[::-1]:
        if not is_operator(ch):
            stack.append(ch)
        else:
            # Lấy 2 phần tử trên cùng của stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Gộp lại thành biểu thức trung tố và đẩy vào stack
            stack.append(f'({op1}{ch}{op2})')
    return stack[-1]

t = int(input())
for _ in range(t):
    exp = input().strip()
    print(prefix_to_infix(exp))
