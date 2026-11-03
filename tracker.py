# ==========================================
# EXPENSE TRACKER - Installment 5
# ==========================================

# Landing Page (Printed once at the start)
print("==========================================")
print("             EXPENSE TRACKER              ")
print("        Know where your money goes.       ")
print("==========================================")
print()

# Setup questions (Asked once per run)
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")
print()

# Initialize tracking variables
subtotal = 0
count = 0

# Main loop to keep the menu alive
while True:
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses        (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    
    choice = input("Choose 1-4: ")
    print()

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal = subtotal + amount
        count = count + 1

        # Size message logic
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
        print()

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
        print()

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget

        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")

        # Budget verdict logic
        if over_budget:
            over_amount = total - budget
            print(f"Over budget by ${over_amount}!")
        elif total > (0.9 * budget):
            left_amount = budget - total
            print(f"Careful: only ${left_amount} left.")
        else:
            left_amount = budget - total
            print(f"Within budget. ${left_amount} left.")
        print()

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 42)
        print(f"Made by: {name} \t| \tInstallment 5")
        print("==========================================")
        break

    else:
        print("Please choose 1, 2, 3 or 4.")
        print()