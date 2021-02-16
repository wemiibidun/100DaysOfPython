'''
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Format the result to 2 decimal places = 33.60
'''

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = (percentage_tip/100)*total_bill
new_total_bill = total_bill + tip
pay_amount = round(new_total_bill/people,2)

print(f"Each person will pay: ${pay_amount}")
