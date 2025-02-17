def solve():
    s = input()
    n = len(s)
    
    # Check for odd length (invalid case)
    if n % 2 != 0:
        print(-1)  # Or handle as needed
        return

    balance = 0
    res = 0
    
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            res += 1  # Need to flip ')' to '('
            balance = 0  # Reset balance since we virtually flipped
        elif balance > n // 2:
            res += 1  # Need to flip '(' to ')'
            balance = n // 2  # Cap balance since we virtually flipped

    print(res + abs(balance) // 2)  # Remaining imbalance needs flips


t = int(input())
for _ in range(t):
    solve()