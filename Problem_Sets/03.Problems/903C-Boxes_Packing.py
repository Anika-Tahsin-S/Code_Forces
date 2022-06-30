n = int(input())
a = [int(i) for i in input().split()]
checklist = []

for i in a:
    checklist.append(a.count(i))
    checklist.sort()
print(checklist[-1])
