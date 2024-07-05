
import sys
import math

sys.stdin = open("index.txt","rt")

'''
뒤집은 소수
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다..'''

# 갯수
N = int(input())
# N개의 자연수
d= list(map(int,input().split()))

# 뒤집는 함수
def reverse(x):
    x = str(x)
    cnt =len(x)
    a = ""
    #for i in range(len(str(x))):
    while(cnt > 0):
        cnt-=1
        a+=x[cnt]
        

    return int(a)


# 소수인지 확인하는 함수
def isPrime(x):
    if x==1 :return False # 소수는 1일때는 제외해야함
    for i in range(2,int(math.sqrt(x))+1):
        if(x % i ==0):
            return False
    return True

for x in range(N):
    r = reverse(d[x])
    if(isPrime(r) ):#소수인지 확인
        print(r, end=" ")
