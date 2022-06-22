n = int(input())

repeat_exercise = [int(i) for i in input().split()]
attempt = [0] * 3

for i in range(n):
    attempt[i % 3] += repeat_exercise[i]

if attempt[0] > attempt[1] and attempt[0] > attempt[2]:
    print("chest")
elif attempt[1] > attempt[2] and attempt[1] > attempt[0]:
    print("biceps")
else:
    print("back")