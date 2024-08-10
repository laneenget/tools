# A recursive functions accepts an argument and includes
# a condition to check whether it matches the base case.
def recursive_countdown(value):

    if value <= 0:
        print("done")
    else:
        print(value)
        recursive_countdown(value - 1)

# Pattern search iterates over each character in a text
# and then counts the following number of matching
# characters to find the pattern.
def pattern_search(text, pattern):

    for index in range(len(text)):
        
        match_count = 0

        for char in range(len(pattern)):
            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break
        
        if match_count == len(pattern):
            print(pattern, "found at index", index)

# A brute force algorithm solves a problem through
# exhaustion: it goes through all possible choices until
# a solution is found. The time complexity of a brute
# force algorithm is usually proportional to the input
# size. Brute force algorithms are simple and constant,
# but very slow.
def print_divisors(n):

    index = n

    while index != 0:

        if n % index == 0:
            print(index)

        index -= 1

# DFS is an exhaustive search algorithm for searching
# tree data structures that can be implemented with a
# recursive approach or an iterative one
def dfs(root, target, path=()):

    path = path + (root,)

    if root.value == target:
        return path
    
    for child in root.children:

        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found
        
    return None