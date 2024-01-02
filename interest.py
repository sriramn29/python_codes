principal = float(input("Enter principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
num_of_years = float(input("Enter the number of years: "))

choice = int(input("\nWhat interest you want?\n1. Simple Interest\n2. Compound Interest\n"))

#Branching
if choice == 1:
    #Calculating Simple Interest
    simple_interest_amount = (principal * rate_of_interest * num_of_years)/100
    print("Simple Interest: ",simple_interest_amount)

elif choice == 2:
    #Calculating Compund Interest
    compound_interest_amount = principal * (1 + rate_of_interest/100) ** num_of_years - principal
    print("Compound interest: ",compound_interest_amount)
else:
    print("Read the instructions properly! Try again next time")