from collections import deque

def knight_moves(start, end):
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
    end_x, end_y = ord(end[0]) - ord('a'), int(end[1]) - 1

    if (start_x, start_y) == (end_x, end_y):
        return 0

    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                if (nx, ny) == (end_x, end_y):
                    return steps + 1
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # Nếu không tìm được đường đi

def main():
    T = int(input())
    
    for _ in range(T):
        start, end = input().strip().split()
        result = knight_moves(start, end)
        print(result)

if __name__ == "__main__":
    main()
