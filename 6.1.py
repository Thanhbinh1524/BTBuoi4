# Nhập số lượng test cases
T = int(input())

# Xử lý từng test case
for _ in range(T):
    # Nhập số n
    n = int(input())
    
    # In tất cả các số nhị phân từ 1 đến n
    for i in range(1, n + 1):
        print(bin(i)[2:])
