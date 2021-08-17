import math

#program will ask user if they want to calculate total investment or loan amount

option = """ Choose either 'investment' or 'bond' from the menu below to proceed:\n
Investment - to calculate the amount of interest you'll earn on interest
Bond - to calculate the amount you'll have to pay on a home loan\n """

print(option)
choice = input("Enter option:\t").lower()   # lower method used to convert input to lowercase characters 

# while loop used if user doesn't enter either of the 2 options specified, program will keep asking
# user to enter correct option. if user does enter either option
#break statement will discontinue the loop and continue with the next statement

while (choice != "investment") and (choice != "bond"):
    print("Invalid option.\n")
    choice = input("Enter option:\t").lower()
    if (choice == "investment") or (choice == "bond"):
        break

# if user chooses investment, program will ask user to enter the following values:
# P- principal investment amount, r - interest rate, t -  time planned to invest in years
# and the type of interest they'd like to use. The conditional statement executed if user chooses investment,
# will calculate user's investment depending on the type of interest user chooses.
# A- total investment amount with interest. Each outcome is rounded off to 2 decimal places

if choice == "investment":
    P = float(input("Enter amount to deposit:\t"))
    r = float(input("Enter the percentage of interest rate:\t"))
    t = int(input("Enter number of years planned to invest:\t"))
    interest = input("Simple or compound interest:\t").lower()
    
    if interest == "simple":
        A = round(P*(1+r*t), 2)     #simple interest formula
        print(f"\nThe total amount of your investment with simple interest is R{A}")

    elif interest == "compound":
        A = round(P*math.pow((1+r), t), 2)      #compund interest formula
        print(f"\nThe total amount of your investment with compound interest is R{A}")

# if user chooses bond, program will ask user for the following values:
# p-present value amount, i-interest rate, n -number of months to repay bond
# x - the total bond repayment per month
#the final answer is rounded of to two decimal places and displayed

elif choice == "bond":
    bond = True
    p = float(input("Enter present value of the house:\t"))
    i = float(input("Enter the percentage of interest rate:\t"))
    if i:
        i = i/12    #interest in the bond formula is divided by 12 
    n = int(input("Enter period planned to repay the bond(in months):\t"))
    
    x = round((i*p)/(1 - math.pow((1+i), -n)), 2)       #bond formula
    print(f"\nThe total bond repayment is R{x} per month")




