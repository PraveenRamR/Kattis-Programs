string = input()
flag = False
for index in range(len(string) - 1): 
	if(string[index] == 's' and string[index + 1] == 's'):
		print('hiss')
		flag = True
		break
if(not flag):
	print('no hiss')