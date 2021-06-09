#Coded by Praveen Ram R
wordSet = set()
repeatFlag = False
string = input().split() 
for word in string :
    if word in wordSet:
        print('no')
        repeatFlag = True
        break
    wordSet.add(word)
if(not repeatFlag):
    print('yes')