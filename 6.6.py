from collections import deque

def min_operations_to_one(N):
    if N < 1:
        return -1  # Invalid input

    queue = deque([(N, 0)])
    visited = set()

    while queue:
        current, steps = queue.popleft()

        if current == 1:
            return steps

        # Operation (a)
        if current - 1 not in visited:
            visited.add(current - 1)
            queue.append((current - 1, steps + 1))

        # Operation (b)
        for i in range(2, int(current ** 0.5) + 1):
            if current % i == 0:
                max_factor = max(i, current // i)
                if max_factor not in visited:
                    visited.add(max_factor)
                    queue.append((max_factor, steps + 1))

    return -1

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter a number: "))
    print(min_operations_to_one(N))