def is_operator(c):
    return c in ["+", "-", "*", "/", "^"]

def prefix_to_postfix(prefix):
    stack = []

    # iterate over the prefix expression in reverse order
    for i in range(len(prefix) - 1, -1, -1):
        if is_operator(prefix[i]):
            # pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # concatenate them in postfix notation and push back to stack
            temp = op1 + op2 + prefix[i]
            stack.append(temp)
        else:
            # if the character is an operand, push it to stack
            stack.append(prefix[i])

    # the last element on the stack will be the postfix expression
    return stack.pop()

# input number of test cases
T = int(input())
for _ in range(T):
    prefix = input().strip()
    print(prefix_to_postfix(prefix))