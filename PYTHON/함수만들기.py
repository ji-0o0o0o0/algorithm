

# 함수는 항상 위에 적어줘야 함
def isPrime(x):
	for i in range(2, x):
		if x % i == 0 :
			return False
		return True

a= [12,13,7,9,19]

for y in a:
	if isPrime(y):
		print(y, end=' ')