from collections import deque

def smallest_multiple_of_n(N):
    visited = set()
    queue = deque(['9'])

    while queue:
        s = queue.popleft()
        num = int(s)

        if num % N == 0:
            return num

        if num not in visited:
            visited.add(num)
            queue.append(s + '0')
            queue.append(s + '9')

    return -1

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter a number: "))
    print(smallest_multiple_of_n(N))