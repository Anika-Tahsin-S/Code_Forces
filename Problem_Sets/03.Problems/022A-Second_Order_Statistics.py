n = int(input())

integer = set(map(int,input().split()))
sort = sorted(integer)

if len(sort) != 1:
    print(sort[1])
else:
    print("NO")