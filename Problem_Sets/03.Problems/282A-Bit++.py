num_operations = int(input())
value = 0
    
for i in range(num_operations):
    operation = input()
    if operation[1] == '+':
        value += 1
    else:
        value -= 1
print(value)