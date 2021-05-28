#Coded by R Praveen Ram
(x, y) = input().split()
revX = ""
revY = ""
for char in x:
	revX = char + revX
for char in y:
	revY = char + revY
if(revX > revY):
	print(revX)
else:
	print(revY)
