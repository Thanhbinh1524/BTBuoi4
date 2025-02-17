def stock_span(n, prices):
    span = [0] * n
    stack = []
    
    for i in range(n):
        # Tìm các ngày có giá nhỏ hơn hoặc bằng giá ngày hiện tại
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # Nếu ngăn xếp rỗng, nghĩa là không có ngày nào trước đó có giá nhỏ hơn hoặc bằng
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]
        
        # Đẩy ngày hiện tại vào ngăn xếp
        stack.append(i)
    
    return span

def main():
    T = int(input())  # Số bộ test
    for _ in range(T):
        n = int(input())  # Số ngày
        prices = list(map(int, input().split()))  # Giá chứng khoán của các ngày
        result = stock_span(n, prices)  # Tính nhịp chứng khoán
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
