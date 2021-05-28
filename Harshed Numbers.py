#Coded by R Praveen Ram
num = int(input())
while(True):
	copy = num
	digitSum = 0
	while(copy != 0):
		digit = copy % 10
		digitSum += digit
		copy = copy // 10
	if(num % digitSum == 0):
		break
	num += 1
print(num)
