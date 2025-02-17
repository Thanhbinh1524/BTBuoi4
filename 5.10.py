def is_operator(c):
    return c in ["+", "-", "*", "/"]

def postfix_to_infix(postfix):
    stack = []

    for char in postfix:
        if not is_operator(char):
            # If the character is an operand, push it to the stack
            stack.append(char)
        else:
            # If the character is an operator, pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Create a string "(op2 op1 operator)" and push it back to the stack
            stack.append(f"({op2}{char}{op1})")

    # The last element on the stack will be the infix expression
    return stack.pop()

# Input number of test cases
T = int(input())
for _ in range(T):
    postfix = input().strip()
    print(postfix_to_infix(postfix))