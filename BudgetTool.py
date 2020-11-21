import os
class Budget(object):
    def __init__(self):
        os.system('cls')
        self.budget = float(input('How much is your budget?\n'))
        self.spending = self.budget * 0.5
        os.system('cls')
        self.main()
        
    def main(self):
        print('This calculator uses 5:3:2 rule of spending by default.')
        print('\nYour budget: $', '{:.2f}'.format(self.budget))
        main_option = int(input('\nWhat do you want to do?\n1) View Budget Plan\n2) View Spending Budget\n3) Exit\n'))
        if main_option == 1:
            self.budget_plan()
        elif main_option == 2:
            self.spending_budget()
        else:
            quit

    def budget_plan(self):
        os.system('cls')
        option = int(input('How much do you want to save?\n1) 20%\n2) 30%\n'))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            print('Please select only 1 or 2')
        self.final_saving = self.budget * self.saving
        self.extra = self.budget-self.spending-(self.budget*self.saving)
        print('\nSpending: $', '{:.2f}'.format(self.spending), '\nTo Save: $', '{:.2f}'.format(self.final_saving), '\nExtra: $', '{:.2f}'.format(self.extra))
        os.system('pause')
        os.system('cls')
        self.main()

    def spending_budget(self):
        os.system('cls')
        print('Spending Budget: $', '{:.2f}'.format(self.spending))
        rent = float(input('\nHow much is your rent/mortgage?\n'))
        bills = float(input('\nHow much are your monthly bills?\n'))
        food = self.spending - rent - bills
        print('\nEXPENSES:\nRent: $','{:.2f}'.format(rent),'\nBills: $','{:.2f}'.format(bills),'\nFood: $','{:.2f}'.format(food))
        os.system('pause')
        os.system('cls')
        self.main()

Budget()