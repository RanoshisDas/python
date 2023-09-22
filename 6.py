def recursive(x, y):
	if y == 0:
		return x
	else:
		return recursive(x + 1, y - 1)
 
num1 = 1
num2 = 2
result = recursive(num1, num2)
print("The sum of", num1, "and", num2, "is", result)
