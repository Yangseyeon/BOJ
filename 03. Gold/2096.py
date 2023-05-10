import sys
n = int(sys.stdin.readline().strip())
score_max = list(map(int, sys.stdin.readline().strip().split()))
score_min = score_max
for _ in range(n - 1):
    next_score = list(map(int, sys.stdin.readline().strip().split()))
    score_max = [next_score[0] + max(score_max[0:2]),
                next_score[1] + max(score_max),
                next_score[2] + max(score_max[1:3])]
    
    score_min = [next_score[0] + min(score_min[0:2]),
                next_score[1] + min(score_min),
                next_score[2] + min(score_min[1:3])]

print(max(score_max), min(score_min))
