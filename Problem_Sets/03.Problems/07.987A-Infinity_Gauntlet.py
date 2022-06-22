infinity_gems = int(input())

gem_names = ["Power", "Time", "Space", "Soul", "Reality", "Mind"]
colors = ["purple", "green", "blue", "orange", "red", "yellow"]

missing_list = []

if infinity_gems != 0:
    for i in range(infinity_gems):
        missing_colors = input()
        missing_list.append(missing_colors)
print(6 - infinity_gems)

for i in range(6):
    if colors[i] not in missing_list:
        print(gem_names[i])