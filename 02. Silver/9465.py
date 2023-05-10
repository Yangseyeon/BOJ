import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    col= int(sys.stdin.readline().strip())
    sticker = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

    score = [sticker[0][0], sticker[1][0], 0]
    for j in range(1, col):
        score_update = [
            sticker[0][j] + max(score[1], score[2]),
            sticker[1][j] + max(score[0], score[2]),
            max(score[0], score[1])
        ]
        score = score_update

    print(max(score))