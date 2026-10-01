# Indian Rupee Money Counter

denominations = [10, 20, 50, 100, 200, 500, 2000]

total = 0

print("=== Indian Rupee Money Counter ===")

for note in denominations:
    while True:
        try:
            quantity = int(input(f"How many ₹{note} notes? "))
            if quantity < 0:
                print("Please enter 0 or a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    amount = note * quantity
    total += amount

    print(f"₹{note} × {quantity} = ₹{amount}")

print("----------------------------")
print(f"Total amount = ₹{total}")
print("----------------------------")
