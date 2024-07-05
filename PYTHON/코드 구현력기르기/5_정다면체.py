
import sys
sys.stdin = open("index.txt","rt")

'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

N과 M은 4, 6, 8, 12, 20 중의 하나
'''

N,M = map(int, input().split())
d=[]

for x in range(1,N+1):
    for y in range(1,M+1):
        d.append(x+y)

# 각 숫자 리스트에 몇 개 들어있는지 딕셔너리로 변경
di = {a:d.count(a) for a in d}

# 최댓값 초기화
max = 0 
res =[]
for k,v in di.items():
    if(max<v):
        max = v
        res.clear()
        res.append(k)
    elif(max==v):
        res.append(k)
for i in res:
    print(i , end=' ')




