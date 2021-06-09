#Coded by Praveen Ram R
count = int(input())
output = ""
for _ in range(count):
    string = input()
    if string.startswith('Simon says'):
        output = output + string[10:] + "\n"
print(output.rstrip("\n"))