count = int(input())
l = []

for i in range(count):
    l.append(input())

output = []
seen = set()

for name in reversed(l):
    if name not in seen:
        output.append(name)
        seen.add(name)

for name in output:
    print(name)