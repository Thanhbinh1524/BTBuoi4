from collections import deque

def min_days_to_sprout(R, C, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    total_seeds = 0
    sprouted_seeds = 0
    days = 0

    # Initialize the queue with the positions of the young plants and count total seeds
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            if grid[i][j] == 1:
                total_seeds += 1

    # BFS to spread the nutrients
    while queue:
        x, y, day = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                grid[nx][ny] = 2
                queue.append((nx, ny, day + 1))
                sprouted_seeds += 1
                days = day + 1

    # Check if all seeds have sprouted
    if sprouted_seeds == total_seeds:
        return days
    else:
        return -1

# Input number of test cases
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    print(min_days_to_sprout(R, C, grid))