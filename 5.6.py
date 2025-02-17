# Define operator precedence and associativity
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
right_associative = {'^'}

def infix_to_postfix(expression):
    """Convert infix expression to postfix using Shunting Yard algorithm."""
    stack = []
    output = []

    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':  # Left Parenthesis
            stack.append(char)
        elif char == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        else:  # Operator
            while (stack and stack[-1] != '(' and 
                   (precedence[stack[-1]] > precedence[char] or 
                   (precedence[stack[-1]] == precedence[char] and char not in right_associative))):
                output.append(stack.pop())
            stack.append(char)

    # Pop remaining operators in the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

def main():
    T = int(input().strip())  # Number of test cases
    results = []

    for _ in range(T):
        exp = input().strip()
        result = infix_to_postfix(exp)
        results.append(result)

    # Output all results, each on a new line
    for result in results:
        print(result)

if __name__ == "__main__":
    main()