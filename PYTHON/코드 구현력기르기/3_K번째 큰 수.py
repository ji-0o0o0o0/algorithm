
import sys
#sys.stdin = open("input.txt","rt")


'''
K번째 큰 수
1부터 100사이의 자연수가 적힌 N장의 카드를 3번 뽑아 더한 값 중 k번째로 큰 값
 '''

N, K = map(int, input().split())
a = list(map(int,input().split()))

#중복 제거 위함
res = set()
for x in range(N):
    for y in range(x+1,N):
        for z in range(y+1,N):
                res.add(a[x]+a[y]+a[z])
# 정렬을 하기 위해 list로 변환
res = list(res)
res.sort(reverse=True)
#print(res)
print(res[K-1])
