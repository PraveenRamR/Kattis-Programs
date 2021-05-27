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



### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
