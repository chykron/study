print('Welcome to split the bill app')
bill = float(input('What was the bill? $'))
tip = int(input('Choose the tip - 10, 12 or 15: %'))
people = int(input('How many people will split the bill?'))
tip_percentage = tip / 100
total_tip = tip_percentage * bill
total_bill = bill + total_tip
bill_per_person = total_bill / people
final = round(bill_per_person, 2)
print(f'Each have to pay {final} $')











#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
