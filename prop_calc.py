class RentalProp():

#This object takes no arguments at instantiation, but each method not only takes the arguments but collects the data required.
#The saveResults method creates a .txt file with the results. It seemed necessary to save them somehow, so this is what I came up with.
    
    def getIncome(self):
        print("Let's calculate the projected income of the property: \n")
        self.rent = float(input("What is the projected monthly rent? "))
        self.is_other_income = input("any other projected income? [y] for Yes, [n} for No ")
        if self.is_other_income.lower() == 'y':
            self.other_income = float(input("What is the total amount of additional income? "))
        else:
            self.other_income = 0
        self.income = self.rent + self.other_income
        return self.income

    def getExpenses(self):
        print("Let's calculate the total projected Expenses: ")
        self.taxes = float(input("What is the projected monthly taxes? "))
        self.insurance = float(input("Insurance? "))
        self.is_utilities = input("Will you be paying any monthly utilities? [y] for yes. ")
        if self.is_utilities.lower() == 'y':
            self.utilities = float(input("How much will you be paying in monthly utilities? "))
        else:
            self.utilities = 0
        self.is_other_expenses = input("Any additional expenses? [y] for yes, [n] for No ")
        if self.is_other_expenses.lower() == 'y':
            self.other_expenses = float(input("What is the total of the other expenses? (HOA, Lawn/Snow, etc. "))
        else:
            self.other_expenses = 0
        self.std_vacancy = input("Okay to project 5 percent of rent for Vacancy? [n] for no. ")
        if self.std_vacancy == 'n':
            self.vacancy = (float(input("What percentage would you like to use for vacancy? ")))/100 * self.rent
        else:
            self.vacancy = self.rent * .05
        self.std_repairs_capex = input("Okay to project 5 percent of rent for repairs and Cap Ex? [n] for no. ")
        if self.std_repairs_capex.lower() == 'n':
            self.diff_repairs_capex = float(input("What amount would you like to put aside (use percentage) "))
            self.repairs_capex = (self.diff_repairs_capex/100) * self.rent
        else:
            self.repairs_capex = self.rent * .10 # If standard repairs and capex selected, this will be 10%, 5% for each
        self.prop_management = float(input("How much will you paying monthly for property management? "))
        self.mortgage = float(input("How much are you projecting for the monthly mortgage payments? "))
        self.expenses = self.taxes + self.insurance + self.utilities + self.other_expenses + self.vacancy + self.repairs_capex + self.prop_management + self.mortgage
        return self.expenses

    def getCashflow(self):
        self.cashflow = self.income - self.expenses # Could just return this statement, but I want to work with this number later
        print(f'Your projected monthly cashflow is {self.cashflow}')
        return self.cashflow

    def getROI(self):
        print("Finally, let's calculate Cash on Cash ROI: ")
        self.downpayment = float(input("How much money are you putting down on the property? "))
        self.closing = float(input("What are you projecting for closing costs? "))
        self.need_rehab = input("Will the property need any updates or rehabs? [y] for yes. ")
        if self.need_rehab.lower() == 'y':
            self.rehab = float(input("How much do you expect to invest to rehab the property? "))
        else:
            self.rehab = 0.0
        self.misc_costs = float(input("What is the amount of additional costs associated with the purchase? 0 for none. "))
        self.total_investment = self.downpayment + self.closing + self.rehab + self.misc_costs
        self.ROI = ((self.cashflow * 12) / self.total_investment) * 100
        print(f'Your Cash on Cash ROI is {self.ROI}%')
        return self.ROI
    
    def saveResults(self, prop_name):
        file_name = prop_name.replace(' ', '') + '.txt' # Don't want any whitespace in the filename
        f = open(file_name, 'w')
        f.write(f'Project name: {prop_name.title()}\n')
        f.write(f'Income: {self.income}\nExpenses: {self.expenses}\nCashflow: {self.cashflow}\nROI: {self.ROI}')
        f.close()
        return 
