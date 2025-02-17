from collections import deque

def count_bdns_less_than_n(N):
    queue = deque(['1'])
    count = 0

    while queue:
        current = queue.popleft()
        num = int(current)

        if num >= N:
            break

        count += 1
        queue.append(current + '0')
        queue.append(current + '1')

    return count

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter a number: "))
    print(count_bdns_less_than_n(N))
