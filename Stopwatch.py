#Coded by Praveen Ram R
count = int(input())
times = []
for i in range(count):
    times.append(int(input()))
result = 0
if count % 2 != 0 :
    print('still running')
else:
    for i in range(1, len(times), 2):
        result += (times[i] - times[i - 1])
    print(result)