#Coded by R Praveen Ram
moves = input()
position = 1
for move in moves:
	if move == 'A':
		if position == 1:
			position = 2
		elif position == 2:
			position = 1
	if move == 'B':
		if position == 2:
			position = 3
		elif position == 3:
			position = 2
	if move == 'C':
		if position == 1:
			position = 3
		elif position == 3:
			position = 1
print(position)
