#ellena carmean
#11/3/22
#cash register
#create retail item objects, ask the user what they would like to buy 
#based on an integer, and display what items they bought, unit, and total cost

class IceCream:
#create our object
  def __init__(self, flavor, scoops, style):
    self.flavor = flavor
    self.scoops = scoops
    self.style = style
    
#here is where our data is stored
    #get flavor
    def iceCream_flav(self):
        return self._flavor
    #get scoops
    def num_of_scoops(self):
        return self._num_scoops
    #get style
    def serving_style(self):
        return self._style

def main():

    #using the __str__ method, accept input from the user to obtain our data
        print('please enter your order 1) vanilla, 2) chocolate 3) strawberry 4) mint 5) pistachio')
        flav_ = input('please enter flavor: ')
        if flav_ == '1':
            print('you chose vanilla')
        elif flav_ == '2':
            print('you chose chocolate')
        elif flav_ == '3':
            print('you chose strawberry')
        elif flav_ == '4':
            print('you chose mint')
        elif flav_ == '5':
            print('you chose pistachio')
        elif flav_ == '6':
            print('you chose spumoni')    
        else:
               raise Exception('item not on the menu') 

        scoo_ = input('please enter number of scoops: ')
        if scoo_ == '1':
                print('1 scoop!')
        elif scoo_ == '2':
                print('2 scoops!')
        elif scoo_ == '3':
                print('3 scoops!')   
        else:
                raise Exception('please choose 1,2 or 3 scoops')

        serv_ = input('would you like bowl or cone: ')
        if serv_ == 'bowl':
            print('you chose a bowl')
        elif serv_ == 'cone':
            print('you chose a cone')
        else:
                raise Exception('please enter bowl or cone')

#create an instance of our object using our stored data
        ice = IceCream(flavor=flav_, scoops = scoo_, style=serv_)

#printing our menu items
        print('menu item: ', ice.flavor)
        print('menu item:', ice.scoops)
        print('in a', ice.style)
main()


