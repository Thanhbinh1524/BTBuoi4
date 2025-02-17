from collections import deque

def is_adjacent(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
        if count > 1:
            return False
    return count == 1

def shortest_path(n, s, t, words):
    words_set = set(words)
    if t not in words_set:
        return -1

    queue = deque([(s, 1)])
    visited = set([s])

    while queue:
        current_word, steps = queue.popleft()
        if current_word == t:
            return steps

        for word in words_set:
            if word not in visited and is_adjacent(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return -1

# Input number of test cases
T = int(input())
for _ in range(T):
    n, s, t = input().split()
    n = int(n)
    words = input().split()
    print(shortest_path(n, s, t, words))
