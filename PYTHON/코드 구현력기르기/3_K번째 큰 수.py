import sys
sys.stdin = open("input.txt","rt")


'''
K번째 큰 수
1부터 100사이의 자연수가 적힌 N장의 카드를 3번 뽑아 더한 값 중 k번째로 큰 값
 '''

N, K = map(int, input().split())
a = list(map(int,input().split()))
b = []
for x in a:
    for y in a:
        for z in a:
            if x+y+z not in b:
                b.append(x+y+z)


b.sort(reverse=True)
print(b)
print(b[K-1])
