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


### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
