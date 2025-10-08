print("Left arrow pattern")
print("------------------")
n = 5
for i in range(n):
    print(' ' * i + '*')
for i in range(n-2, -1, -1):
    print(' ' * i + '*')
