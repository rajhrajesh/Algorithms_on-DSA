arr = [2,3,7,8,10]

for multiplier in arr:
    row = [multiplier * num for num in arr]
    print(f"Mul by {multiplier}: {row}")

