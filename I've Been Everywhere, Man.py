#Coded By Praveen Ram R
testCaseCount = int(input())
result = ""
for _ in range(testCaseCount):
    count = int(input())
    cities = set()
    for _ in range(count):
        city = input()
        cities.add(city)
    result = result + str(len(cities)) + "\n"
print(result.rstrip("\n"))