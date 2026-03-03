total = 0
count = 0

while True:
    amount = input("Enter amount (or done): ")
    
    if amount == "done":
        break

    amount = float(amount)
    total += amount
    count += 1

    if amount > 10000:
        print("Large transaction!")

print("Total Transactions:", count)
print("Final Balance:", total)