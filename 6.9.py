from collections import deque

def bfs_min_steps(N, grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == (end[0], end[1]):
            return steps

        for dx, dy in directions:
            nx, ny = x, y

            while 0 <= nx + dx < N and 0 <= ny + dy < N and grid[nx + dx][ny + dy] != 'X':
                nx += dx
                ny += dy

                if (nx, ny) in visited:
                    continue

                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # Nếu không tìm được đường đi

def main():
    num_tests = int(input())
    
    for _ in range(num_tests):
        N = int(input())
        grid = [input().strip() for _ in range(N)]
        a, b, c, d = map(int, input().strip().split())
        
        start = (a, b)
        end = (c, d)
        
        min_steps = bfs_min_steps(N, grid, start, end)
        print(min_steps)

if __name__ == "__main__":
    main()
