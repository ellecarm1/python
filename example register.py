class RetailItem:
    def __init__(self, price, units, description): 
        self.price = price
        self.units = units
        self.description = description

    def __str__(self):
        string = str(self.description)
        string += ": $" + str(self.price)
        string += " Units:" + str(self.units)
        return string


class CashRegister:
    def __int__(self,RetailItem):
        self.total= ()
        Duck = RetailItem()
        Duck.description = "Large plush duck"
        Duck.units = 3
        Duck.price = 6.99

        Porcupine = RetailItem()
        Porcupine.description = "Pink plush porcupine"
        Porcupine.units = 5
        Porcupine.price = 9.99

        Bunny = RetailItem()
        Bunny.description = "small white plush bunny"
        Bunny.unitsininv = 7
        Bunny.price = 4.99

        print("Welcome to The Toy Store.\n Selection:\n 1.Bunny \n 2.Porcupine \n 3.Duck")
        choice = int(input("What would you like to buy? "))
        if choice==1:
            item = Bunny
        elif choice == 2:
            item = Porcupine
        elif choice==3:
            item = Duck
        else:
            print("Error")