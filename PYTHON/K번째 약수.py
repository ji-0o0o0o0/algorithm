

'''
K번째 약수

 어떤 자연수 p와 q 가 있을 때, 만일 p를 q로 나누었을때 나머지가 0이면 q는 p의 약수

 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K 번째 작은 수를 출력하세요
 (존재하지 않을때 -1)
 '''

N, K  = map(int,input().split())

# 나의 답변
A = []
# N의 약수
for i in range(1,N+1):
    if (N%i==0):
        A.append(i)

try:
    print(A[K-1])
except:
    print(-1)


# 답안
cnt = 0
for i in range(1,N+1):
    if (N%i==0):
        cnt+=1
    if cnt == K:
        print(i)
        break
else:
    print(-1)
