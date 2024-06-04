a =[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a))

# 아래 두개는 모두 같은 값을 반환
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in  a:
    print(x, end=' ')
print()


# 인덱스와 값 출력
#(0, 23)
#(1, 12)
#(2, 36)
#(3, 53)
#(4, 19)
for x in enumerate(a):
    print(x)

b = (1,2,3,4,5,6)
# b는 튜플구조
# b[0] = 1 이렇게 정해진 값을 변경할 수 없다
# print(b[0]) 이렇게 출력은 가


# 두 반복문 모두 같은 값 반환
# 인덱스와 반환값 구하고 싶을 때 이렇게 하면 됨
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19
for x in enumerate(a):
    print(x[0],x[1])
print()

for index,value in enumerate(a):
    print(index,value)
print()

# 응용
# all(조건) : 조건이 모두 참일때 참
if all(60>x for x in  a):
    print("Yes")
else:
    print("NO")
    
# any(조건) : 조건이 하나라도 참이라면 참
if all(11>x for x in  a):
    print("Yes")
else:
    print("NO")

# a =[23,12,36,53,19]
# all, any 조건 모두 YES
