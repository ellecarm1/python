#ellena carmean
#computer programming
#10/21/22
#this program will create retailItems classes and objects, 
#and will include accessors and mutators for those objects 
#then print the data given using the __str__ method

#class retailItems:

#initialize our class
#accessors and mutators for retailItems data

from typing import ItemsView


class RetailItems:
    def __init__(self, price, units, description): 
        self.price = price
        self.units = units
        self.description = description

    def __str__(self):
        string = str(self.description)
        string += ": $" + str(self.price)
        string += " Units:" + str(self.units)
        return string
#menu
    print(print('1). Item 1\n2). Item 2\n3). Item 3\n4). Item 4\n5). Item 5'))
    #using the __str__ method, accept input from the user to obtain our data
print('please enter employee information')
name = input ('Enter Employee Name: ')
number = input ('Enter Employee Number: ')
shift = int(input('Enter Shift Number: '))
pay = float(input('Enter Pay Rate: '))


class CashRegister(RetailItems):
#if 1, if 2, if 3, if 4, if 5
    itemPurchase= int(input('Enter the menu number of the item you would like to purchase:'))

    if itemPurchase == 1:
    #insert return for retail items here
        print('Pants')
    elif itemPurchase == 2:
       print('Shirt')
    elif itemPurchase == 3:
       print('Dress')
    elif itemPurchase == 4:
       print('Socks')
    elif itemPurchase == 5:
       print('Sweater')
    else:
       print('Huh?')

checkOut = input('The item was added to the cash register. Are you ready to check out (Y/N)?').lower()
if checkOut == 'y':

    itm = ItemsView(name,number,shift,pay)

    print('production worker info')
    print ('Name: ',itm.get_itm_name())
    print ('itmloyee Number: ',itm.get_itm_number())
    print ('Shift Number: ',itm.get_shift_num())
    currency_string = "${:,.2f}".format(pay)
    print(currency_string)
    print ('Pay Rate: ',itm.get_pay_rates())
else:
    print('nooo')

currency_string = "${:,.2f}".format(pay)
print(currency_string)