#Coded by R Praveen Ram
cipher = input()
replacement = "PER"
replacementIndex = 0
count = 0
for index in range(len(cipher)):
    if(cipher[index] != replacement[replacementIndex]):
        count+=1
    replacementIndex = (replacementIndex + 1) % 3 
print(count)
