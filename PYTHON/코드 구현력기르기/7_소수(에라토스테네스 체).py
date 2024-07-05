
import sys
import math

sys.stdin = open("index.txt","rt")

'''
소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.'''

#1)
#def primenumber(x):
#    for i in range(2,x):
#        if(x%i==0): #1,본인을 제외한 수가 있을때
#            return False
#    else:
#        return True
# Case #01 : Success
#Case #02 : Time Limit Exceeded
#Case #03 : Time Limit Exceeded
#Case #04 : Time Limit Exceeded
#Case #05 : Time Limit Exceeded

#점수 결과 : 20

# 2)에라토스테네스의 체
# 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다는 뜻
def primenumber(x):
    for i in range(2,int(math.sqrt(x)+1)):# 2부터 x의 제곱근까지의 숫자
        if x % i ==0:
            return False
    return True

## N의 소수의 개수
N = int(input())
cnt = 0
for i in range(2, N+1):
    if(primenumber(i)):
        cnt+=1
print(cnt)





