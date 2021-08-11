from typing import Counter


A=int(input())
B=int(input())
C=int(input())
D=str(A*B*C)

for i in range(10):
    num = D.count(str(i))
    print(num)