
import sys

sys.stdin = open("index.txt","rt")

'''
회문 문자열 검사
앞뒤 문자가 같으면 yes, 아니면 no 출력
대소문자 구별x
'''

# 문제개수
N =int(input())

for _ in range(N):
    s = input().upper()
    rs =''
    for i in range(len(s)):
        rs = s[i]+rs
    if(s==rs):
        print('#'+str(_+1),'YES')
    else:
        print('#'+str(_+1),'NO')
    
        
