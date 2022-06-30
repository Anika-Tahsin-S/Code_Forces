t = int(input())

for i in range(t):
    n = int(input())
    total = (n * (n + 1)) // 2
    power = 1
    #print(total)

    while power <= n:
        total -= 2 * power # 10 - (2*1), 8 - (2*2), 4 - (4*2)
        #print(total) # 8, 8 - 4 = 4, 4 - 8 = -4
        power = 2 * power # 2, 4

    print(total)