# Write your solution here
freq = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much do money do you spend on groceries in a week?"))

daily = (freq * price + groceries) / 7.0
weekly = freq * price + groceries

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")