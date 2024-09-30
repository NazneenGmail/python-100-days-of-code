print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much percent tip would you like to give? 10, 12 or 15?\n"))
ppl = int(input("How many people to split the bill?\n"))

share = round((total_bill + (total_bill * tip / 100))/ppl, 2)
print(f"Each person should pay ${share:.2f}")
