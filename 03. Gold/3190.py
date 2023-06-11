import sys
from collections import deque

def next_move(a, b, sec):
    if sec in turn.keys():
        if a == 0:
            return [b, 0] if turn[sec] == "D" else [-b, 0]

        return [0, -a] if turn[sec] == "D" else [0, a] 

    return [a, b]


def move_snake():
    snake = deque()
    sec = 0
    snake.append([0, 0])
    board[0][0] = 1
    a = 0
    b = 1

    while True:

        h_i, h_j = snake.popleft()
        a, b = next_move(a, b, sec)
        next = [h_i + a, h_j + b]

        sec += 1
        if (next[0] >= n or next[0] < 0) or (next[1] >= n or next[1] < 0):
            break
    
        if board[next[0]][next[1]] == 1:
            break

        elif board[next[0]][next[1]] == 2:
            snake.appendleft([h_i, h_j])

        elif board[next[0]][next[1]] == 0:
            if snake:
                t_i, t_j = snake.pop()
                snake.appendleft([h_i, h_j])
            else:
                t_i, t_j = h_i, h_j
            board[t_i][t_j] = 0
        
        board[next[0]][next[1]] = 1
        snake.appendleft([next[0], next[1]])

    print(sec)


n = int(sys.stdin.readline().strip())
board = [[0 for _ in range(n)] for _ in range(n)]
turn = dict()

for _ in range(int(sys.stdin.readline().strip())):
    i, j = map(int, sys.stdin.readline().strip().split())
    board[i - 1][j - 1] = 2
for _ in range(int(sys.stdin.readline().strip())):
    i, j = sys.stdin.readline().strip().split()
    turn[int(i)] = j

move_snake()