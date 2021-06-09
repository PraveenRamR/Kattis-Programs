#Coded by Praveen Ram R
def findOddOneOut(guests) :
    guestSet = set()
    for guest in guests:
        if guest in guestSet:
            guestSet.remove(guest)
        else:
            guestSet.add(guest)
    return guestSet.pop()
count = int(input())
result = ""
for i in range(1, count + 1):
    number = int(input())
    guests = input().split()
    result = result + "Case #" + str(i) + ": " + str(findOddOneOut(guests)) + "\n"
print(result.rstrip("\n"))