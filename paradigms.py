#object oriented programming
class  Customer:
    # Constructor used for setting data
    def __init__(self, name, type):
        self.name = name
        self.type = type

        if(type == "senior"):
            self.interest = 7.5
        else:
            self.interest = 6
    # Function here on
    def get_interest_on_deposit(self, principal, years):
        interest_amount = principal*years*self.interest/100
        return interest_amount
    
customer1 = Customer("Sriram", "normal")
customer2 = Customer("Sameer", "senior")

print(customer1.interest, customer2.interest)

print(customer1.get_interest_on_deposit(100000, 5))
print(customer2.get_interest_on_deposit(100000, 7))

