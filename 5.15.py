def next_greater_element(arr, n):
    nge = [-1] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            nge[i] = arr[stack[-1]]
        stack.append(i)
    
    return nge

def next_smaller_element(arr, n):
    nse = [-1] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            nse[i] = arr[stack[-1]]
        stack.append(i)
    
    return nse

def process_test_case(n, arr):
    # Find Next Greater Element
    nge = next_greater_element(arr, n)
    
    # Find Next Smaller Element
    nse = next_smaller_element(arr, n)
    
    # Result array
    result = []
    
    # For each element, find the Next Greater Element and its corresponding Next Smaller Element
    for i in range(n):
        if nge[i] == -1:
            result.append(-1)
        else:
            next_smaller = nse[arr.index(nge[i])] if nge[i] != -1 else -1
            result.append(next_smaller)
    
    return result

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        result = process_test_case(n, arr)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
