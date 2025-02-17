def has_unique_digits_less_than_five(n):
    digits = set()
    while n > 0:
        digit = n % 10
        if digit > 5 or digit in digits:
            return False
        digits.add(digit)
        n //= 10
    return True

def count_valid_numbers(L, R):
    count = 0
    for num in range(L, R + 1):
        if has_unique_digits_less_than_five(num):
            count += 1
    return count

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    L, R = map(int, input().split())
    print(count_valid_numbers(L, R))