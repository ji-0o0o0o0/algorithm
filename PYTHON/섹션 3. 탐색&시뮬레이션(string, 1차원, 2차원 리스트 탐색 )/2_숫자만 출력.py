
import sys

#sys.stdin = open("index.txt","rt")

'''
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듬
만들어진 자연수와 그 자연수의 약수 개수를 출력
'''

s = input()
num = ''
# 문자열 확인
for i in range(len(s)):
    if(not s[i].isalpha()):
        num+=s[i]
num = int(num)
print(num)

# 약수의 개수
cnt =0
for i in range(1,num+1):
    if(num%i==0):
        cnt+=1
print(cnt)
