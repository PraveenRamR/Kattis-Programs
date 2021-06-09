#Coded by Praveen Ram R
points = list()
maxSum = 0
winner = -1
for index in range(1, 6):
    total = 0
    points = input().split()
    for point in points:
        total += int(point)
    if(total > maxSum):
        maxSum = total
        winner = index
print(winner , " " , maxSum)
