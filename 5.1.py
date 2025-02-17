def is_redundant(expression):
    stack = []
    for ch in expression:
        if ch == ')':
            top = stack.pop()
            elements_inside = False
            while top != '(':
                if top in '+-*/':
                    elements_inside = True
                top = stack.pop()
            if not elements_inside:
                return True
        else:
            stack.append(ch)
    return False

def main():
    t = int(input())
    for _ in range(t):
        expr = input().strip()
        if is_redundant(expr):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
