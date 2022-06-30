n = int(input())

l = []

for i in range(n):
    name = input()
    l.append(name)

l.reverse()
output = []
seen = set()

for name in l:
    if name not in seen:
        output.append(name)
        seen.add(name)

for name in output:
    print(name)