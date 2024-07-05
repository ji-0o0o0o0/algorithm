
import sys

sys.stdin = open("index.txt","rt")

'''
주사위 게임
규칙
- 1~6까지 눈을 가진 주사위 3개를 던져
1) 3개 같을때
 - 10,000원+(같은 눈)*1,000원
2) 2개 같을때
 -  1,000원+(같은 눈)*100원
3) 모두 다를때 
 -  (그 중 가장 큰 눈)*100원

 N명 참가시 받은 돈 중 가장 큰 돈은?
'''

N = int(input());
max = 0
for i in range(N):
    d = list(map(int,input().split()))
    di = {x:d.count(x) for x in d}
    for k,v in di.items():
        if(v == 3):
            sum =10000+k*1000
        elif(v==2):
            sum =1000+k*100
        else:
            sum =k*100
    if(max<sum):
        max = sum
print(max)
