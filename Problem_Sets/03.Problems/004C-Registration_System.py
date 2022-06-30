dictt = {}

for i in range(0, int(input())):
    string = input()
    if string not in dictt:
        print("OK")
        dictt[string] = 1
    else:
        ans = string + str(dictt[string])
        print(ans)
        dictt[string] += 1