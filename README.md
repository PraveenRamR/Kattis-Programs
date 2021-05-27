## Welcome to GitHub Pages
This page contains the solutions for the problems in kattis. 
You can also have a look at this [GitHub Repo ](https://github.com/PraveenRamR/Kattis-Programs)


### Autori

```Autori
names = input(" Enter Name: ")
abbrev = ""

for name in names.split("-"):
abbrev = abbrev + name[0]

print(abbrev)

```

### Quality-Adjusted-Life-Year
```QUALY
print('%.3f' % sum((lambda z: float(z[0])*float(z[1]))(input().split()) for _ in range(int(input()))))
```

### R2

```R2
(r1, s) = input().split(" ")
r1 = int(r1)
s = int(s)

r2 = s * 2 - r1
print(r2)
```

### Cold-Puter Science

```CPS
num = int(input())
count = 0

for i in input().split():
	temp = int(i)
	if(temp < 0):
		count += 1

print(count)
```

### Cryptographer's Conundrum
```CC
cipher = input()
replacement = "PER"
replacementIndex = 0
count = 0
for index in range(len(cipher)):
    if(cipher[index] != replacement[replacementIndex]):
        count+=1
    replacementIndex = (replacementIndex + 1) % 3 
print(count)
```

### Hello World
```Hello World
print("Hello World!")
```

### Hissing Microphone
```HM
string = input()
flag = False
for index in range(len(string) - 1): 
	if(string[index] == 's' and string[index + 1] == 's'):
		print('hiss')
		flag = True
		break
if(not flag):
	print('no hiss')
```

### Line Them Up
```LTU
import sys
import string

input = sys.stdin.read()
line = input.split("\n")
n = line[0]
line = line[1:-1]

if sorted(line) == line:
    print ("INCREASING")
elif line == sorted(line)[::-1]:
    print ("DECREASING")
else:
    print ("NEITHER")
```

### Quadrant Selection
```QS
x = int(input())
y = int(input())
if(x > 0 and y > 0):
	print(1)
elif(x < 0 and y > 0):
	print(2)
elif(x < 0 and y < 0):
	print(3)
else:
	print(4)
```

### Struck in a time loop
```SIATL
  
n = int(input())
for i in range(1, n + 1):
	print(i , "Abracadabra")
```

### Take Two Stones
```TTS
num = int(input())

if(num %2 == 0):
    print("Bob")
else:
    print("Alice")
```


### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
