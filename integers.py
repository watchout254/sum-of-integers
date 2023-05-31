print("\t\tWelcome to Sum it up integers\n")
total = 0
digits = int(input("Enter a digit ( N/B: 0 is to quit):"))
while digits != 0:
    total += digits
    digits = int(input("Enter a digit ( N/B: 0 is to quit):"))

print("The total is:",total)
print("Thank you for trusting me.")
