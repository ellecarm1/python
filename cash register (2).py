#ellena carmean
#11/3/22
#cash register
#create retail item objects, ask the user what they would like to buy 
#based on an integer, and display what items they bought, unit, and total cost

#constants
import string

from typing import List

#create lists for receipt
itm_list = []
desc_list = []
unit_list = []

class RetailItems:

  def __init__(self, description, units, price):
    self.description = description
    self.units = units
    self.price = price
#object descriptions
item1 = RetailItems("Pants", 366, 29.99)
item2 = RetailItems("Shirt", 643, 9.99)
item3 = RetailItems("Dress", 747, 49.99)
item4 = RetailItems("Socks", 332, 14.99)
item5 = RetailItems("Sweater", 412, 19.99)


#our menu
class CashRegister:

    print('item: ',item1.description)
    print('units available: ',item1.units)
    print('price: ',item1.price)

    print('item: ',item2.description)
    print('units available: ',item2.units)
    print('price: ',item2.price)

    print('item: ',item3.description)
    print('units available: ',item3.units)
    print('price: ',item3.price)

    print('item: ',item4.description)
    print('units available: ',item4.units)
    print('price: ',item4.price)

    print('item: ',item5.description)
    print('units available: ',item5.units)
    print('price: ',item5.price)

#ask the user what item they would like to purchase, and if so, add it to the list
def purchase_item():
    addItem = int(input("Enter the item you would like to purchase, 1-5"))
    if addItem==1:
        print( 'The item was added to the register')
        choice = input('are you ready to checkout? y/n')
        if choice == 'y':
            itm_list.append(item1.price)
            desc_list.append(item1.description)
            unit_list.append(item1.units)
    elif addItem ==2:
        print( 'The item was added to the register')
        choice = input('are you ready to checkout? y/n')
        if choice == 'y':
            itm_list.append(item2.price)
            desc_list.append(item3.description)
            unit_list.append(item2.units)
    elif addItem==3:
        print( 'The item was added to the register')
        choice = input('are you ready to checkout? y/n')
        if choice == 'y':
            itm_list.append(item3.price)
            desc_list.append(item3.description)
            unit_list.append(item3.units)
    elif addItem==4:
        print( 'The item was added to the register')
        choice = input('are you ready to checkout? y/n')
        if choice == 'y':
            itm_list.append(item4.price)
            desc_list.append(item4.description)
            unit_list.append(item4.units)
    elif addItem==5:
        print( 'The item was added to the register')
        choice = input('are you ready to checkout? y/n')
        if choice == 'y':
            itm_list.append(item5.price)
            desc_list.append(item5.description)
            unit_list.append(item3.units)

    else:
        print("Error")

purchase_item()

#the rest of our functions to display information
def get_total():
    print('get total is working')
    print('your total is: ', itm_list)
get_total()
print('the items in the cash register are: ')
def show_item():
    print('show item is working')
    print('description:', desc_list, 'units in inventory: ', unit_list, 'price: ', itm_list)
show_item()
def clear_register():
    print('the register has been cleared')

#clear lists
clear_register()
itm_list.clear
del itm_list[:]
desc_list.clear
del desc_list[:]
unit_list.clear
del unit_list[:]

    

