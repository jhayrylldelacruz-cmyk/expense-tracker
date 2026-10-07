#Installment
print("-" * 40)
print("          EXPENSE TRACKER")
print("    Know where your money goes.")
print("-" * 40)

print("\nWelcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("[1] Add an expense           (coming soon)")
print("[2] View all expenses        (coming soon)")
print("[3] Show total spent         (coming soon)")
print("[4] Exit                     (coming soon)\n")

#Inputs
name = input("What's your name? ")
print("Welcome,", name, "! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

#Calcu
total = amount1 + amount2
average = total / 2

#Sum
print("-" * 40)
print("SUMMARY")
print("    -", item1, ":  $", amount1)
print("    -", item2, ":  $", amount2)
print("Total spent:  $", total)
print("Average:      $", average)
print("-" * 40)
print("Made by: Jhayryll  |  Installment 2")