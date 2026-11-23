# 8-Puzzle using simple BFS
from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = deque([start])
parent = {start: None}

while queue:
    state = queue.popleft()
    if state == goal:
        break

    zero = state.index(0)
    for move in [-3, 3, -1, 1]:
        new_pos = zero + move
        if new_pos < 0 or new_pos >= 9:
            continue
        if move == -1 and zero % 3 == 0:
            continue
        if move == 1 and zero % 3 == 2:
            continue

        new_state = list(state)
        new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
        new_state = tuple(new_state)
        if new_state not in parent:
            parent[new_state] = state
            queue.append(new_state)

if goal in parent:
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parent[state]
    for state in reversed(path):
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution")
