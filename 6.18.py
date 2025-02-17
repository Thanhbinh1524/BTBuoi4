from collections import deque

def rotate_left(state):
    return [state[3], state[0], state[2], state[4], state[1], state[5]]

def rotate_right(state):
    return [state[0], state[4], state[1], state[3], state[5], state[2]]

def min_moves(start, target):
    if start == target:
        return 0
    
    visited = set()
    queue = deque([(start, 0)])
    visited.add(tuple(start))
    
    while queue:
        current_state, moves = queue.popleft()
        
        left_rotated = rotate_left(current_state)
        if left_rotated == target:
            return moves + 1
        
        right_rotated = rotate_right(current_state)
        if right_rotated == target:
            return moves + 1
        
        if tuple(left_rotated) not in visited:
            visited.add(tuple(left_rotated))
            queue.append((left_rotated, moves + 1))
        
        if tuple(right_rotated) not in visited:
            visited.add(tuple(right_rotated))
            queue.append((right_rotated, moves + 1))
    
    return -1

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    start = list(map(int, input("Enter start state: ").split()))
    target = list(map(int, input("Enter target state: ").split()))
    print(min_moves(start, target))
