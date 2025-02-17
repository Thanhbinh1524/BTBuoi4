from collections import deque

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_neighbors(num):
    neighbors = []
    num_str = list(str(num))
    
    for i in range(4):
        original_digit = num_str[i]
        for digit in '0123456789':
            if digit == original_digit:
                continue
            num_str[i] = digit
            neighbor = int(''.join(num_str))
            if is_prime(neighbor) and 1000 <= neighbor <= 9999:
                neighbors.append(neighbor)
        num_str[i] = original_digit
    
    return neighbors

def bfs_shortest_path(S, T):
    queue = deque([(S, 0)])
    visited = set()
    visited.add(S)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == T:
            return steps
        
        for neighbor in generate_prime_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    
    return -1  # Nếu không tìm được đường đi

def main():
    T = int(input())
    
    for _ in range(T):
        S, T = map(int, input().strip().split())
        result = bfs_shortest_path(S, T)
        print(result)

if __name__ == "__main__":
    main()
