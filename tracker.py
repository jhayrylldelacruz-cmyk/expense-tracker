# ==========================================
# EXPENSE TRACKER - Installment 4
# ==========================================

# Landing Page
print("==========================================")
print("             EXPENSE TRACKER              ")
print("        Know where your money goes.       ")
print("==========================================")
print()
print("MAIN MENU")
print("[1] Add an expense           (coming soon)")
print("[2] View all expenses        (coming soon)")
print("[3] Show total spent         (coming soon)")
print("[4] Exit                     (coming soon)")
print()

# Greeting & Inputs
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

subtotal = 0  # Initialize subtotal

# First expense
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

# Size message for expense 1
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Second expense
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

# Size message for expense 2
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Check for two big expenses (> 100)
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

# Financial calculations
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget

print("-" * 42)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

# Budget verdict logic (ensures no negative values are shown)
if over_budget:
    over_amount = total - budget
    print(f"Over budget by ${over_amount}!")
elif total > (0.9 * budget):
    left_amount = budget - total
    print(f"Careful: only ${left_amount} left.")
else:
    left_amount = budget - total
    print(f"Within budget. ${left_amount} left.")

print("-" * 42)
print(f"Made by: {name} \t| \tInstallment 4")