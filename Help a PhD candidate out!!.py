x = int(input())
for i in range(x):
  s = input()
  if s == "P=NP":
    print("skipped")
  else:
    n1, n2 = s.split("+")
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)