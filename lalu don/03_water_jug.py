# Water Jug Problem: 4-litre and 3-litre jugs, get 2 litres
from collections import deque

start = (0, 0)
queue = deque([start])
parent = {start: None}

while queue:
    a, b = queue.popleft()
    if a == 2 or b == 2:
        goal = (a, b)
        break

    states = [
        (4, b), (a, 3), (0, b), (a, 0),
        (a - min(a, 3-b), b + min(a, 3-b)),
        (a + min(b, 4-a), b - min(b, 4-a))
    ]
    for state in states:
        if state not in parent:
            parent[state] = (a, b)
            queue.append(state)

path = []
state = goal
while state is not None:
    path.append(state)
    state = parent[state]
for state in reversed(path):
    print("Jug A:", state[0], "Jug B:", state[1])
