# Test 1: No adjacent mines
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
rows = 5
columns = 5
print(count_adjacent_mines(2, 2))  # Expected output: 0

# Test 2: One adjacent mine
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
rows = 5
columns = 5
print(count_adjacent_mines(2, 2))  # Expected output: 1

# Test 3: Multiple adjacent mines
grid = [
    [0, 0, 0, 0, 0],
    [0, 9, 9, 0, 0],
    [0, 9, 0, 9, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
rows = 5
columns = 5
print(count_adjacent_mines(2, 2))  # Expected output: 4

# Test 4: Edge case (top-left corner)
grid = [
    [9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
rows = 5
columns = 5
print(count_adjacent_mines(0, 0))  # Expected output: 0

# Test 5: Edge case (bottom-right corner)
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9]
]
rows = 5
columns = 5
print(count_adjacent_mines(4, 4))  # Expected output: 0