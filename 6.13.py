def generate_loc_phat_numbers(n):
    if n <= 0:
        return []
    
    from itertools import product

    loc_phat_numbers = []
    for i in range(1, n + 1):
        for combination in product('68', repeat=i):
            loc_phat_numbers.append(int(''.join(combination)))
    
    return sorted(loc_phat_numbers)

def main():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        loc_phat_numbers = generate_loc_phat_numbers(N)
        print(len(loc_phat_numbers))
        print(' '.join(map(str, loc_phat_numbers)))

if __name__ == "__main__":
    main()
