#Coded by R Praveen Ram
num = int(input())
count = 0

for i in input().split():
	temp = int(i)
	if(temp < 0):
		count += 1

print(count)
