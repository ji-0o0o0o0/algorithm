
import sys
sys.stdin = open("index.txt","rt")

'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 
꼭 작성해서 프로그래밍 하세요.
'''

# 각 자연수 자릿수 합
def digit_sum(x):
    x = str(x)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    return sum

N = int(input())
d = list(map(int,input().split()))
max = 0

for i in range(N):
    a = digit_sum(d[i])
    if(max<a):
        max =a
        res = d[i]
else:
    print(res)
