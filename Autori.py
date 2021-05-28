#Coded by R Praveen Ram
names = input(" Enter Name: ")
abbrev = ""

for name in names.split("-"):
abbrev = abbrev + name[0]

print(abbrev)
