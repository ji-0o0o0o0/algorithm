
import sys
#sys.stdin = open("input.txt","rt")


'''
대표값
N명의 수학점수
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력

 ▣ 입력예제 1                                   
 10
 45 73 66 87 92 67 75 79 75 80
 ▣ 출력예제 1
 74 7

'''
n = int(input())
math = list(map(int,input().split()))

# 평균, 소숫점 첫번째 자리에서 반올림
# av = round(sum(math)/n)
# ** 반올림 할때 round는 round_half_even 방식 즉, 정확하게 하프일때 짝수 쪽으로 근사값을 출력해 준다
#    하여 round 쓰면 틀리는 경우 발생할 수 도 있음
# 0.5 더해서 int 형으로 소수점 없애는 방법으로 진행
av = sum(math)/n+0.5
av = int(av)


#x = 0
#a = []

#for i in range(n):

#    if i == 0:
#        x = abs(math[i]-av)

#    elif x >= abs(math[i]-av): # 같을때는 큰 수
#        x = abs(math[i]-av)
#        a.append(math[i])

#print(av,math.index(max(a))+1)
## 40점

min = 214700000 #정수 최댓값
for idx, x in enumerate(math):
     tmp = abs(x-av)
     if tmp < min : # 최솟값일때 해당 점수, 위치 저장
         min = tmp
         score = x
         res = idx+1
     elif tmp == min: # 최솟값 같을 경우 점수가 더 클때 점수, 위치 저장
         if x>score:
            score = x
            res = idx+1
print(av, res)









