from collections import Counter

def find_nearest_higher_frequency(arr):
    freq = Counter(arr)
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and freq[arr[i]] >= freq[arr[stack[-1]]]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    
    return result

# Input number of test cases
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(" ".join(map(str, find_nearest_higher_frequency(arr))))