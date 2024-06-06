
'''
람다 함수
- 내장함수의 인자로 쓸때 용이
- 단독으로 사용시에는 변수값 필요 
'''

def plus_one(x):
	return x+1
	

a = [1,2,3]
print (list(map(plus_one,a)))
print (list(map(lambda x : x+1,a)))

# plus_one 함수와 lambda x : x+1 값은 값 출력
