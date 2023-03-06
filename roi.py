#Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
#Our client's name is Brandon from a company called "Bigger Pockets". 
#Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
#Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming,
#create a program that will calculate the Return on Investment(ROI) for a rental property.
#This project will be completed individually, though you can feel free to share ideas with your fellow students.
#Once completed, commit the project to github and submit the link to this assignment.

#1. Create a class to figure out RIO. 
#2. Inside of class, create varios methods to calculate each "square"
#3. Create a function, to run each methods of the class. 

class RentalInvestmentRoi():
    def __init__(self):
        self.total_monthly_income = 0
        self.toal_monthly_expenses = 0
        self.annual_cashflow = 0
        self.total_investment = 0
        self.name = ''

    def introduction(self,):
        
        print("\n\nWelcome to your one and only Rental Property Calculator")
        name = input("What's your name? Please type your name here: ")
        self.name = name
        response1 = input(f"Hello {name.title()}, if you wish to calculate your Rental Property ROI please press 'enter'. "
        "\nOtherwise, if you want exit the calculator press 'exit': ")

        while response1.lower() not in ('exit', 'enter'):
            response1 = input("***COMMAND INVALID*** \nPLease press 'enter' or 'cancel': ")
        if response1 == 'enter':
            print("\nGreat! When answering the following questions please:"
                  "\n1.)Refrain from using capital letters."
                  "\n2.)Don't use punctuation marks or symbols when typing dollar amounts."
                  "\n3.)Round up to your nearest dollar.\n"
                  )
        elif response1 == 'cancel':
            print("\nThanks for checking us out! When you're ready to calculate you're ROI please come back.")
                

    def monthly_income(self):
        rent_income, laundry, storage, miscellaneous, = 0, 0, 0, 0,
        
        print(f"{self.name.title()}, first we need to figure out your monthly income from the rental properties."
              "\nPlease answer the following questions. " 
              #"\n*If you want to exit the calculator at anytime please type 'exit'. "
              )
        rent_income = input("\nWhat is your monthly income, just from rent: ")

        while True:
            response2 = input(f"Your rent income is ${rent_income}. Is this correct?"
                          " Please type 'yes or 'no': ")
            while response2 not in ('yes', 'no'):
                response2 = input("***COMMAND INVALID*** PLease type 'yes' or 'no': ")
            if response2 == 'no':
                rent_income = input("Please type your monthly rent income: ")
                continue
            elif response2 == 'yes':
                break

        response2 = input(
                          "\nIs that your only source of income?"
                         " Please type 'yes' or 'no': "
                         )
        while response2 not in ('yes', 'no'):
            response2 = input("***COMMAND INVALID*** PLease type 'yes' or 'no': ")
        if response2 == 'no':
            while True:
                response2 = input(
                                "\nPlease examine the options provided below and select the ones that are relevant to you."
                                "\n1.Laundry"
                                "\n2.Storage"
                                "\n3.Miscellaneous"
                                "\n4.No more sources of income."
                                "\nPLease select a number: "
                                )
                
                while response2 not in ('1','2', '3', '4'):
                    response2 = input("***COMMAND INVALID*** \nPLease type a number from 1 through 3.")

                if response2 == '1': 
                    laundry = input("\nHow much income do you recive from laundry services monthly: ")
                    while True:
                        print(f"Your monthly laundry income is ${laundry}. Is this correct?")
                        response2 = input("Please type 'yes or 'no'")
                        while response2 not in ('yes', 'no'):
                            response2 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                        if response2 == 'no':
                            laundry = input("Please type your monthly laundry income: ")
                            continue
                        elif response2 == 'yes':
                            return laundry

                elif response2 == '2': 
                    storage = input(f"How much income do you recive from storage services monthly: ")
                    while True:
                        print(f"Your monthly storage income is ${storage}. Is this correct?")
                        response2 = input("Please type 'yes or 'no'")
                        while response2 not in ('yes', 'no'):
                            response2 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                        if response2 == 'no':
                            storage = input("Please type your monthly storage income: ")
                            continue
                        elif response2 == 'yes':
                            return storage

                elif response2 == '3': 
                    miscellaneous = input(f"How much income do you recive from miscellaneous services monthly: ")
                    while True:
                        print(f"Your monthly miscellaneous income is ${miscellaneous}. Is this correct?")
                        response2 = input("Please type 'yes or 'no'")
                        while response2 not in ('yes', 'no'):
                            response2 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                        if response2 == 'no':
                            storage = input("Please type your monthly miscellaneous income: ")
                            continue
                        elif response2 == 'yes':
                            return miscellaneous

                elif response2 == '4':
                    response2 = input("Are you done adding aditional sources of income: ")
                    while response2 not in ('yes', 'no'):
                            response2 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response2 == 'no':
                        continue
                    if response2 == 'yes':
                        break

        self.total_monthly_income = (int(rent_income) + int(laundry) + int(storage) + int(miscellaneous))
                 



        print(
            f"\nHere is your montlhy income from all your rental sources: \n"
            f"\nRent : ${rent_income}"
            f"\nLaundry : ${laundry}"
            f"\nStorage : ${storage}"
            f"\nMiscellaneous : ${miscellaneous}\n"
            f"\nTotal montly income: ${self.total_monthly_income}"
            )
        
              

    def monthly_expense(self):
        print(f"\nNow that we have calculated your total monthly income (${self.total_monthly_income}), " 
              "we need to determine your total monthly expense.\n"
              #"\n*If you want to exit the calculator at anytime please type 'exit'. "
              )
        mortgage, insurance, taxes, hoa, utilities, lawn_snow, vacancy, repairs, property_man = 0, 0, 0, 0, 0, 0, 0, 0, 0
        
        while True:
            response3 = input(
                            "Please examine the options provided below and select the ones that are relevant to you."
                            "\n1.Mortgage"
                            "\n2.Insurance"
                            "\n3.HOA"
                            "\n4.Taxes"
                            "\n5.Utilities"
                            "\n6.Lawn/Snow"
                            "\n7.Vacancy"
                            "\n8.Repairs"
                            "\n9.Property Management"
                            "\n10.Finished providing income sources.\n"
                            "\nPLease select a number: "
                            )
            
            while response3 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
                    response3 = input("***COMMAND INVALID*** \nPLease type a number from 1 through 9: ")

            if response3 == '1': 
                mortgage = input(f"\nWhat is your monthly mortgage payment: ")
                while True:
                    print(f"Your monthly morgage expense is ${mortgage}. Is this correct? ")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        mortgage = input("Please type your monthly mortgage payment: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '2': 
                insurance = input(f"\nWhat is your monthly insurance payment: ")
                while True:
                    print(f"Your monthly insurance expense is ${insurance}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no':  ")
                    if response3 == 'no':
                        insurance = input("Please type your monthly insurance payment: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '3': 
                hoa = input(f"\nWhat is your monthly HOA payment: ")
                while True:
                    print(f"Your monthly HOA expense is ${hoa}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        hoa = input("Please type your monthly HOA payment: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '4': 
                taxes = input(f"\nWhat is your monthly property tax payment: ")
                while True:
                    print(f"Your monthly tax expense is ${taxes}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        taxes = input("Please type your monthly property tax payment: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '5': 
                utilities = input(f"\nHow much do you pay each month for utilities: ")
                while True:
                    print(f"\nYour monthly utilities expense is ${utilities}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        utilities = input("Please type your monthly utilities expense: ")
                        continue
                    elif response3 == 'yes':
                        break 

            if response3 == '6': 
                lawn_snow = input(f"\nHow much do you pay for snow/lawn maintance: ")
                while True:
                    print(f"Your monthly snow/lawn maintance expense is ${lawn_snow}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        lawn_snow = input("Please type your snow/lawn maintance expense: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '7': 
                vacancy = input(f"\nWhat is your monthly vacancy expense: ")
                while True:
                    print(f"Your monthly vacancy expense is ${vacancy}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        vacancy = input("Please type your monthly vacancy expense: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '8': 
                repairs = input(f"\nWhat is your monthly repairs expense: ")
                while True:
                    print(f"Your monthly repairs expense is ${repairs}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        repairs = input("Please type your monthly repairs expense: ")
                        continue
                    elif response3 == 'yes':
                        break

            if response3 == '9': 
                property_man = input(f"\nWhat is your monthly property management expense: ")
                while True:
                    print(f"Your monthly management expense is ${property_man}. Is this correct?")
                    response3 = input("Please type 'yes or 'no': ")
                    while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response3 == 'no':
                        property_man = input("Please type your management expense: ")
                        continue
                    elif response3 == 'yes':
                        break
       
            elif response3 == '10':
                response3 = input("\nAre you finished documenting all of your expenses? Please type 'yes' or 'no': ")
                while response3 not in ('yes', 'no'):
                        response3 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                if response3 == 'no':
                    continue
                if response3 == 'yes':
                    break
        
        self.total_monthly_expenses = (int(mortgage) + int(taxes) + int(insurance) + int(utilities) + int(hoa) + int(vacancy) + int(lawn_snow) + int(property_man) + int(repairs))

        print(f"Here are your montlhy expenses:\n"
              
            f"\nMortgage : ${mortgage}"
            f"\nInsurance : ${insurance}"
            f"\nTaxes : ${taxes}"
            f"\nHOA : ${hoa}"
            f"\nUtilities : ${utilities}"
            f"\nLawn_snow : ${lawn_snow}"
            f"\nVacancy : ${vacancy}"
            f"\nRepairs : ${repairs}"
            f"\nProperty_man : ${property_man}\n"

            f"\nTotal monthly expense: ${self.total_monthly_expenses}"

            )
    

    def investment_ammount(self):
        print(f"\nNow we need to calculate your total investment." 
              #"\n*If you want to exit the calculator at anytime please type 'exit'. "
            )
        down_payment, closing_costs, rehab, miscellaneous = 0, 0, 0, 0

        while True:
            response4 = input(
                        "\nPlease examine the options provided below and select the ones that are relevant to you."
                        "\n1.Down payment"
                        "\n2.Clossing costs"
                        "\n3.Rehab"
                        "\n4.Miscellaneous"
                        "\n5.Finished providing investment sources."
                        "\nPlease select a number: "
                        )
            while response4 not in ('1', '2', '3', '4', '5'):
                response4 = input("***COMMAND INVALID*** \nPLease type a number from 1 through 5: ")

            if response4 == '1': 
                down_payment = input(f"\nWhat is the down payment: ")
                while True:
                    print(f"Your down paymet is ${down_payment}. Is this correct? ")
                    response4 = input("Please type 'yes or 'no': ")
                    while response4 not in ('yes', 'no'):
                        response4 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response4 == 'no':
                        down_payment = input("Please type your down payment: ")
                        continue
                    elif response4 == 'yes':
                        break

            if response4 == '2': 
                closing_costs = input(f"\nWhat are your closing costs: ")
                while True:
                    print(f"Your closing costs are ${closing_costs}. Is this correct? ")
                    response4 = input("Please type 'yes or 'no': ")
                    while response4 not in ('yes', 'no'):
                        response4 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response4 == 'no':
                        closing_costs = input("Please type your closing costs: ")
                        continue
                    elif response4 == 'yes':
                        break

            if response4 == '3': 
                rehab = input(f"\nWhat are your rehab costs: ")
                while True:
                    print(f"Your rehab costs are ${rehab}. Is this correct? ")
                    response4 = input("Please type 'yes or 'no': ")
                    while response4 not in ('yes', 'no'):
                        response4 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response4 == 'no':
                        rehab = input("Please type your rehab costs: ")
                        continue
                    elif response4 == 'yes':
                        break

            if response4 == '4': 
                miscellaneous = input(f"\nAdditional costs/investments: ")
                while True:
                    print(f"Your additional costs/investments are ${miscellaneous}. Is this correct? ")
                    response4 = input("Please type 'yes or 'no': ")
                    while response4 not in ('yes', 'no'):
                        response4 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                    if response4 == 'no':
                        miscellaneous = input("Please type your additional costs/investments: ")
                        continue
                    elif response4 == 'yes':
                        break

            elif response4 == '5':
                response4 = input("\nAre you finished documenting your intial investment? Please type 'yes' or 'no': ")
                while response4 not in ('yes', 'no'):
                    response4 = input("***COMMAND INVALID*** \nPLease type 'yes' or 'no': ")
                if response4 == 'no':
                    continue
                if response4 == 'yes':
                    break

        self.total_investment = (int(down_payment) + int(closing_costs) + int(rehab) + int(miscellaneous))

        print(
            f"Here are your total investment/costs:\n"
            f"\nDown payment: ${down_payment}"
            f"\nClosing costs: ${closing_costs}"
            f"\nRehab: ${rehab}"
            f"\nMiscellaneous: ${miscellaneous}"

            f"\nTotal investment: ${self.total_investment}"
            )
        
    def calculate_roi(self):
        yearly_income = (self.total_monthly_income* 12)
        yearly_expense = (self.total_monthly_expenses * 12)
        annual_cashflow = (yearly_income - yearly_expense)

        roi = str(((annual_cashflow / self.total_investment) * 100)) + '%'

        print(
            f"\nYour rental property(s) generate an annual income of ${yearly_income}."
            f"\nYour yearly expenses are are ${yearly_expense}."
            f"\nYour annual cashflow is ${annual_cashflow}.\n"
            f"\nThe rate of return on your property investment is {roi}."

            "\nThaks for using our property investment calculator. See you soon!\n"
            )
        

#ex1 = RentalInvestmentRoi()
#ex1.introduction()
#ex1.monthly_income()
#ex1.monthly_expense()
#ex1.investment_ammount()
#ex1.calculate_roi()



def rental_calculator():
    ex = RentalInvestmentRoi()
    ex.introduction()
    ex.monthly_income()
    ex.monthly_expense()
    ex.investment_ammount()
    ex.calculate_roi()

rental_calculator()