class RentalProperty():
    def __init__(self, street_address, city, state, purchase_price):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.purchase_price = purchase_price

class RentalCalc():
    def __init__(self):
        self.rental = {}

    def add(self, street_address, city, state,purchase_price):
        new_rental = RentalProperty(street_address, city, state, purchase_price)
        self.rental[street_address] = new_rental

    def show(self):
        print('~' * 25)
        print("THIS IS YOUR PROPERTY:")
        for key, val in self.rental.items():
            print(f"Address: {val.street_address}, {val.city}, {val.state}\nPurchase Price: {val.purchase_price}")
            print('~' * 25)


    def income_from_property(self,rent,laundry, storage, misc):
        self.rent= rent
        self.income = rent + laundry + storage + misc
        print('~' * 25)
        print(f'Your income from this property is: {self.income}')
        print('~' * 25)

    def property_expenses(self, tax, insurance, utility, hoa, lawn_care, mortgage, any_other_exp):
        vacancy = self.rent * 5 /100 
        repairs = self.rent * 10 / 100
        property_manage = self.rent * 10 /100
        self.expenses = tax + insurance + utility + hoa +lawn_care + mortgage + vacancy + repairs + property_manage + any_other_exp
        print('~' * 25)
        print(f'Total monthly expenses for this property is: {self.expenses}')
        print('~' * 25)

    def property_cash_flow(self):
        self.cash_flow = self.income - self.expenses
        print('~' * 25)
        print(f'Monthly cash flow on this property is {self.cash_flow}')
        print('~' * 25)

    def cash_on_cash (self, down_pay, closing_cost, repair_bgt, misc_exp):
        self.total_invest = down_pay + closing_cost + repair_bgt + misc_exp
        self.annual_cash_flow = self.cash_flow * 12
        self.roi = self.annual_cash_flow * 100 / self.total_invest
        print('~' * 25)
        print(f"Your cash on cash ROI is: {self.roi:.3f}%")
        print('~' * 25)


class Calculator():
    def __init__(self):
        self.calc = RentalCalc()

    def main(self):
        try:
            while True:
                user_choice = int(input('Choose 1 or 2 :-\n1.Calculate ROI\n2.Quit\nEnter your choice: '))
                if user_choice == 1:
                    street_address= input('Enter street address: ')
                    city = input('Enter city: ')
                    state = input('Enter state: ')
                    purchase_price = float(input('Enter purchase price: '))

                    self.calc.add(street_address, city, state,purchase_price)
                    self.calc.show()

                    print('Lets calculate your income from this property:-')
                    print('Enter monthly income from following:=')
                    rent = float(input('Rent collection: '))
                    laundry = float(input('Laundry services (If not available enter zero): '))
                    storage = float(input('Storage unit(If not available enter zero): '))
                    misc = float(input('Any other services: '))

                    self.calc.income_from_property(rent,laundry, storage, misc)

                    print('Now its time to calculate total monthly expenses:-')
                    print('Enter monthly expense for following:=')
                    tax = float(input('Property taxes: '))
                    insurance =float(input('Insurance paid: '))
                    utility = float(input('Total utility bills payment: '))
                    hoa = float(input('HOA fee if any, else Enter zero: '))
                    lawn_care = float(input('Lawn care charges: '))
                    mortgage =float(input('Mortgage payment: '))
                    any_other_exp = float(input('Sum of other expenses not mentioned above: '))

                    self.calc.property_expenses(tax, insurance, utility, hoa, lawn_care, mortgage, any_other_exp)
                    self.calc.property_cash_flow()

                    print("Let's find out Return on your Investment (ROI):-  ")
                    down_pay =  float(input('Down payment for this property: '))
                    closing_cost = float(input('Payment towards closing cost: '))
                    repair_bgt = float(input('Rehab/Repair budget: '))
                    misc_exp = float(input('Any other expenses: '))

                    self.calc.cash_on_cash (down_pay, closing_cost, repair_bgt, misc_exp)

                elif user_choice == 2:
                    break
                else:
                    print('Invalid option, please try again.')
        except ValueError as v:
            print(f'Wrong Input. Error: {v}')
        except Exception as e:
            print(f'Error: {e}')

