c = int(input())

for start_case in range(c):
    N = list(map(int,input().split()))
    result = sum(N[1:])/N[0]
    cnt=0
    for score in N[1:]:
        if score > result:
            cnt +=1
    rate=cnt/N[0]*100
    print(f'{rate:.3f}%')
