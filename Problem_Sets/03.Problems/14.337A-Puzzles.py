n, _ = [int(x) for x in input().split()]
n -= 1

puzzles_sold = [int(x) for x in input().split()]
puzzles_sold.sort()

min_difference = None
for slices in range(len(puzzles_sold) - n):
    slice_count = puzzles_sold[slices + n] - puzzles_sold[slices]
    if min_difference == None or min_difference > (slice_count):
        min_difference = slice_count

print(min_difference)