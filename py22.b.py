print("Right Aligned Triangle Pattern")
print("--------------------------------")
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
