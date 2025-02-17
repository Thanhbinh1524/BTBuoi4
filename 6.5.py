from collections import deque

def min_steps(S, T):
    # Duyệt qua tất cả các giá trị của S từ 1 đến T
    queue = deque([(S, 0)])  # (giá trị S, bước)
    visited = [False] * 10000  # Mảng để theo dõi các giá trị đã thăm
    visited[S] = True
    
    while queue:
        current, steps = queue.popleft()
        
        # Nếu đã đạt đến T, trả về số bước
        if current == T:
            return steps
        
        # Thao tác (a): Trừ đi 1
        if current - 1 >= 0 and not visited[current - 1]:
            visited[current - 1] = True
            queue.append((current - 1, steps + 1))
        
        # Thao tác (b): Nhân với 2
        if current * 2 < 10000 and not visited[current * 2]:
            visited[current * 2] = True
            queue.append((current * 2, steps + 1))
    
    return -1  # Nếu không thể chuyển từ S sang T, trả về -1

def main():
    T = int(input())  # Số lượng test
    for _ in range(T):
        S, T = map(int, input().split())
        print(min_steps(S, T))

if __name__ == "__main__":
    main()
