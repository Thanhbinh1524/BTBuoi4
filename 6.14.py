def generate_lucky_numbers(n):
    if n == 0:
        return []
    if n == 1:
        return ['6', '8']
    
    smaller_numbers = generate_lucky_numbers(n - 1)
    result = []
    for num in smaller_numbers:
        result.append('6' + num)
        result.append('8' + num)
    return result

def get_lucky_numbers_up_to_n_digits(n):
    result = []
    for i in range(1, n + 1):
        result.extend(generate_lucky_numbers(i))
    return sorted(result, reverse=True)

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter a number: "))
    lucky_numbers = get_lucky_numbers_up_to_n_digits(N)
    print(len(lucky_numbers))
    print(" ".join(lucky_numbers))