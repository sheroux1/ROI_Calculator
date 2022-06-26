import prop_calc

quit = False
while quit == False: 
    prop_name = input("Time to analyze a potential property investment. What would you like to name this property? ")
    prop = prop_calc.RentalProp()

    prop.getIncome()
    prop.getExpenses()
    prop.getCashflow()
    prop.getROI()
    prop.saveResults(prop_name)

    another = input("Would you like to analyze another property? [q] to exit. ")
    if another.lower() == 'q':
        quit = True