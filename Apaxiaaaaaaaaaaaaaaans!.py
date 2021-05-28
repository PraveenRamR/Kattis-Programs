#Coded by R Praveen Ram
string = input()
result = string[0]

for index in range(1, len(string)):
	if(string[index] == result[-1]):
		continue
	result += string[index]

print(result)
