# Issues:
# Loop iterates up to n, but only needs to go to sqrt(n)
# This is inefficient (O(n) instead of O(√n))


rows = int(input("Enter rows: "))

# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2*i - 1))

# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2*i - 1))


