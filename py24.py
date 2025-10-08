print("Right Arrow Pattern")
print("-------------------")

n = 5
for i in range(n):
    if i <= n//2:
        print(' ' * i + '*')
    else:
        print(' ' * (n - i - 1) + '*')
