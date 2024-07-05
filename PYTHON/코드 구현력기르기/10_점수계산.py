
import sys

sys.stdin = open("index.txt","rt")

'''
점수계산
답이 맞는 처음 문제는 1점으로 계산한다. 
또한, 연속으로 문제의 답이 맞는 경우 K번째 문제는 K점으로 계산
0은 문제의 답이 틀린 경우이고, 1은 문제의 답이 맞는 경우
'''

# 문제개수
N =int(input())
d= list(map(int,input().split()))
# 전에 맞았는지 확인
sucess = 0
#전체 점수
sum = 0

for i in range(N):
    if(d[i]==1): # 맞았을때
        sucess +=1
    if(d[i]==0):
        sucess = 0
    sum+=sucess
print(sum)

