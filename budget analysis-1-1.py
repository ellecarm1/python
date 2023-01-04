#ellena carmean
#9/8/22
#day of the week
#this code will ask the user to input their revenue minus expenses   
#to determine if theyre over or under their budget

total = 0
expenses = 0
gross_profit = 0

#ask the user for their budget
budget = (int(input('Enter the amount budgeted for the month: ')))
currency = "${:,.2f}".format(budget)
print(currency)

a = 1
while a !=0:
    a = float(input("Enter an expense (enter 0 to quit): $"))
    total += float(a)

amount = total

currency = "${:,.2f}".format(amount)
print('total expenses: ', currency)

gross_profit = budget-total
#determine if the user is over or under budget
#print(gross_profit)
if total > budget:
    print('you\'re', "${:,.2f}".format(gross_profit), 'over budget oh noo')
if total < budget:
    print('you\'re', "${:,.2f}".format(gross_profit), 'under your budget yayy')
    
    
