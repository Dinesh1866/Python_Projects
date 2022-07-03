#Tip Calculator

'''get the total bill and what percrntage would like to give tip
10 or 12 or 15 after giving one it should ask how many people to split bill with
and user gives the input and return how much amout should each pay'''


print("'Welcome to the Tip Calculator'")
total_bill = float(input("what was the total bill?\nin $ or Rs:"))
tip_percent = int(input("What percentage tip would you like to give? \nmost common chooises 10, 12 ,15 or your own? \n"))
number_of_split =int(input("How many people to split the bill? \n"))
tip_amount = total_bill*(tip_percent/100)
each_pay = (total_bill + tip_amount)/number_of_split
print("Each person should pay: %.2f"%(each_pay))