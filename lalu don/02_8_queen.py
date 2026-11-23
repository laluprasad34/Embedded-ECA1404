# 8-Queen using backtracking
N = 8
board = [-1] * N

def safe(row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(row):
    if row == N:
        return True
    for col in range(N):
        if safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
    return False

solve(0)
for row in range(N):
    print(" ".join("Q" if board[row] == col else "." for col in range(N)))
