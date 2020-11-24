def square(n):
	return n*n
a=square(9)
print(a)

# # 1. The def statement is executed, so define a function before it is used
# # 2. Body of the function should be indented consistently

def add(a, b):
	return a+b

result = add(1, 2)
print(result)

# # 3. The function could be assigned another name: square2 = square

plus = add
result2 = plus(2, 3)
print(result2)


# # 4. Function names can be stored in a list: list1 = [square, square2]

list1 = [add, plus]
for i in list1:
 	print(i(2,3))

# 5. Can put a def statement inside an if statement, etc.

Mode = input('please select a mode (0-subtraction/1-addition):')

if Mode == '1':
    def f(x):
        return x + 5
else:
    def f(x):
        return x - 5

print (f(10))

# # 6. Arguments are optional and separated by commas

def addition1():
	return 1 + 1

def addition2(a, b):
	return a + b

print(addition1())
print(addition2(1, 1))

# # # 7. If there is no return statement, then None is returned

def addition(a, b):
	result = a + b
	return result
c = addition(10, 10)
print(c)
# # 8. Arguments could be any type (typeless)

def meanscore(a):
	result = 0
	for number in a:
		result = result + number # result += number
	mean = result/len(a)
	return mean
scores = [95, 92, 81, 74, 100]
print(meanscore(scores))



