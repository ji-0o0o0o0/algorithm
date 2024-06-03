
import random as r

a = list(range(1,6))
print(a)

a.append(7)
print(a)

a.insert(3,7)
print(a)

a.pop()
print(a)

a.pop(2)
# 2번째 자리에 있는 3 제외
print(a)

a.remove(4)
#해당 숫자 제외
print(a)

print(a.index(5))
# 5가 3번째 자리에 있으므로 3 출력

a= list(range(1,11))
print(a)

print(sum(a))
print(max(a))
print(min(a))

r.shuffle(a)
print(a)

#오름차
a.sort()
print(a)

#내림차순
a.sort(reverse=True)
print(a)

a.clear()
print(a)

