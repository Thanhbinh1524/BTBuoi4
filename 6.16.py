from collections import deque

def min_steps_to_reach_end(M, N, matrix):
    directions = [(0, 1), (1, 0)]  # Right and Down movements
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = [[False] * N for _ in range(M)]
    visited[0][0] = True

    while queue:
        x, y, steps = queue.popleft()

        if x == M - 1 and y == N - 1:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx * matrix[x][y], y + dy * matrix[x][y]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

    return -1

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    M, N = map(int, input("Enter M and N: ").split())
    matrix = [list(map(int, input().split())) for _ in range(M)]
    print(min_steps_to_reach_end(M, N, matrix))