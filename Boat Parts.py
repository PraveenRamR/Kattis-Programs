#Coded by Praveen Ram R
(num_parts, count) = input().split()
num_parts = int(num_parts)
count = int(count)
parts = set()
result = -1
for day in range(1, count + 1):
    part = input()
    parts.add(part)
    if(len(parts) == num_parts and result == -1):
        result = day
if(len(parts) < num_parts):
    print('paradox avoided')
else:
    print(result)