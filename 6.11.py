from collections import deque

def bfs_shortest_path(A, B, C, grid, start, end):
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    queue = deque([(start[0], start[1], start[2], 0)])
    visited = set()
    visited.add((start[0], start[1], start[2]))

    while queue:
        x, y, z, steps = queue.popleft()

        if (x, y, z) == end:
            return steps

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz

            if 0 <= nx < A and 0 <= ny < B and 0 <= nz < C and grid[nx][ny][nz] != '#' and (nx, ny, nz) not in visited:
                visited.add((nx, ny, nz))
                queue.append((nx, ny, nz, steps + 1))

    return -1  # Nếu không tìm được đường đi

def main():
    T = int(input())
    
    for _ in range(T):
        A, B, C = map(int, input().strip().split())
        grid = []
        
        for _ in range(A):
            layer = []
            for _ in range(B):
                layer.append(list(input().strip()))
            grid.append(layer)
            if _ < A - 1:
                input()  # Bỏ qua dòng trống giữa các lớp

        start = None
        end = None
        
        for i in range(A):
            for j in range(B):
                for k in range(C):
                    if grid[i][j][k] == 'S':
                        start = (i, j, k)
                    elif grid[i][j][k] == 'E':
                        end = (i, j, k)
        
        if start and end:
            min_steps = bfs_shortest_path(A, B, C, grid, start, end)
            print(min_steps)
        else:
            print(-1)

if __name__ == "__main__":
    main()
