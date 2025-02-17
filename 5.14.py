def find_min_number(pattern):
    result = []
    stack = []

    for i in range(len(pattern) + 1):
        stack.append(str(i + 1))

        if i == len(pattern) or pattern[i] == 'I':
            while stack:
                result.append(stack.pop())

    return ''.join(result)

# Input number of test cases
T = int(input())
for _ in range(T):
    pattern = input().strip()
    print(find_min_number(pattern))