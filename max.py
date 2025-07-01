a = [1, 2, 3, 7, 4, 6,9,8,5]
max_val = a[0]

for i in range(len(a)):
    if a[i] > max_val:
        max_val = a[i]

print("Maximum value:", max_val)
