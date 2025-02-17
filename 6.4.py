from collections import deque

def smallest_bdn_multiple(N):
    visited = set()
    queue = deque(['1'])

    while queue:
        bdn = queue.popleft()
        num = int(bdn)

        if num % N == 0:
            return num

        if bdn not in visited:
            visited.add(bdn)
            queue.append(bdn + '0')
            queue.append(bdn + '1')

    return -1

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter a number: "))
    print(smallest_bdn_multiple(N))