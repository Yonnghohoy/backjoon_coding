N = int(input())
score_lst = list(map(int,input().split()))
max_score = max(score_lst)
length = len(score_lst)
total_cost = 0
for elem in score_lst:
    total_cost += elem/max_score*100
print(total_cost/length)