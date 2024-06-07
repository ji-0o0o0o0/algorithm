
import sys
sys.stdin = open("index.txt","rt")

'''
K번째 수
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
'''


# 테스트 케이스
T = int(input())

for _ in range(T):
	# N,s,e,k
	N,s,e,k = map(int, input().split())

	# N 개
	a = list(map(int, input().split()))
	# a= a[s-1:e] 로 슬라이싱 해도 됨
	b =[]
	# s부터 e까지
	for i in range(s-1,e):
		b.append(a[i])

	# 오름차순
	b.sort();
	# k 순번인 번호 출력
	print("#%d %d" %(_+1, b[k-1]))
