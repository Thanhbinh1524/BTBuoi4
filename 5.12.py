def evaluate_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        if expression[i] in operators:
            # Pop two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            # Apply the operator and push the result back to the stack
            if expression[i] == '+':
                stack.append(operand1 + operand2)
            elif expression[i] == '-':
                stack.append(operand1 - operand2)
            elif expression[i] == '*':
                stack.append(operand1 * operand2)
            elif expression[i] == '/':
                stack.append(operand1 / operand2)
        else:
            # If the character is an operand, push it to the stack
            stack.append(int(expression[i]))
    
    # The last element on the stack will be the result
    return stack.pop()

# Input number of test cases
T = int(input())
for _ in range(T):
    prefix = input().strip()
    print(int(evaluate_prefix(prefix)))