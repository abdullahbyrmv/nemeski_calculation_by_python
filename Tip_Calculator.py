print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? Type any number such as 10,15, etc \n"))
people = int(input("How many people to split the bill? : \n"))

total_bill = bill * (tip/100) +bill

bill_per_person = total_bill/people

final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")
