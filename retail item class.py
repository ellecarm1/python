#ellena carmean
#computer programming
#10/19/22
#this program will create retail item classes and display them

#create class
class RetailItem:

#the init method or constructor
    def __init__(self, desc, units, price):
#instance attributes
        self.desc = desc
        self.units = units
        self.price = price
#create instance of object
jacket = RetailItem(desc = 'jacket', units = '12', price = '59.95')
jeans = RetailItem(desc = 'jeans', units = '40', price = '34.95')
price = RetailItem(desc = 'price', units = '20', price = '24.95')
# displayEmployee method of class RetailItem
print(jacket.desc, jacket.units, jacket.price)
print(jeans.desc, jeans.units, jeans.price)
print(price.desc, price.units, price.price)