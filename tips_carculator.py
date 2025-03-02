print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? "))
tips = float(input("How much tip wold you like to give? 10, 20, or 15? "))

tip_percentage = total_bill * (tips / 100)
people = int(input("How many people to split the bill?"))
pay = round((tip_percentage + total_bill) / people, 2)

print(f"Each person should pay: {pay}")
