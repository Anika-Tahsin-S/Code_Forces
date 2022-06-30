a, b, c, d = [int(i) for i in input().split()]
    
misha = max( (3 * a) / 10, a - a / 250 * c)
vasya = max( (3 * b) / 10, b - b / 250 * d)
    
if misha > vasya:
    print("Misha")
if misha < vasya:
    print("Vasya")
if misha == vasya:
    print("Tie")