from itertools import combinations

def find_parentheses_pairs(expression):
    """Find indices of matching parentheses pairs."""
    stack = []
    pairs = []

    for index, char in enumerate(expression):
        if char == '(':
            stack.append(index)
        elif char == ')':
            if stack:
                opening_index = stack.pop()
                pairs.append((opening_index, index))

    return pairs

def generate_expressions(expression, pairs):
    """Generate all valid expressions by removing pairs of parentheses."""
    all_expressions = set()
    
    # Try removing at least one pair up to all pairs
    for r in range(1, len(pairs) + 1):
        for pair_combination in combinations(pairs, r):
            to_remove = set()
            for start, end in pair_combination:
                to_remove.add(start)
                to_remove.add(end)

            # Build the new expression by skipping indices in to_remove
            new_expression = ''.join(
                char for idx, char in enumerate(expression) if idx not in to_remove
            )
            all_expressions.add(new_expression)
    
    return sorted(all_expressions)

def main():
    # Input: a single line of a mathematical expression
    expression = input().strip()

    # Find all pairs of parentheses
    pairs = find_parentheses_pairs(expression)
    
    # Generate all valid expressions by removing parentheses pairs
    result_expressions = generate_expressions(expression, pairs)
    
    # Output the results in lexicographical order
    for expr in result_expressions:
        print(expr)

if __name__ == "__main__":
    main()