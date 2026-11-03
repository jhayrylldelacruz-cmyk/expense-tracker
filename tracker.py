# ==========================================
# EXPENSE TRACKER - Installment 3
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
subtotal = subtotal + amount1  # Add right after reading

# Second expense
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2  # Add right after reading

# Financial calculations
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total  # Note: Expected format can result in negative values like $-4.0

print("-" * 42)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?:\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 42)
print(f"Made by: {name} \t| \tInstallment 3")