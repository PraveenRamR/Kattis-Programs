def getFactorial(num):
	if(num == 0):
		return 1
	return num * getFactorial(num - 1)
count = int(input())
result = ""
for _ in range(count):
	num = int(input())
	fact = getFactorial(num)
	digit = fact % 10
	result = result + str(digit) + "\n"
print(result.rstrip("\n"))