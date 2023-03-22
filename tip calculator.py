print("Welcome to yhe trip calculator.")
bill = int(input("What is the total bill?: $"))
percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15%?:"))
how_people = int(input("How many people to split the bill?:"))
tip_as_percent = percentage / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / how_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay:${final_amount}")