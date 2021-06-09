def getResult(count):
	if(count == 0):
		return ""
	data = input()
	if(data == "P=NP"):
		return ('skipped\n') + getResult(count - 1)
	else:
		(a, b) = data.split("+")
		a = int(a)
		b = int(b)
		return str(a + b) + "\n" + getResult(count - 1)
count = int(input())
print(getResult(count).rstrip("\n"))