#  최솟값 구하기

arr =[5,3,7,9,2,5,2,6]
arrMin = float('inf')
# float('inf') 는 파이썬에서 제일 큰 값

for x in range (len(arr)):
    if arr[x] < arrMin: # arrMin의 default 값을 무한대 값으로 해놓은 이유
        arrMin = arr[x]

print(arrMin)

# 이렇게 해도 되고 처음부터 arrMin = arr[0] 으로 해도됨
# 또는 아래도 값은 같
for x in arr:
    if x < arrMin: # arrMin의 default 값을 무한대 값으로 해놓은 이유
        arrMin = x
