#ellena carmean
#11/3/22
#cash register
#create retail item objects, ask the user what they would like to buy 
#based on an integer, and display what items they bought, unit, and total cost

from xml.dom.minicompat import EmptyNodeList


class IceCream:

  def __init__(self, flavor_, scoops_, servingStyle_):
    self._flavor = flavor_
    self._num_scoops = scoops_
    self._style = servingStyle_

    #set flavor
    def set_iceCream_flav(self,flavor_):
        self._flavor = flavor_
    #set scoops
    def set__num_of_scoops(self,scoops_):
        self._num_scoops = scoops_
    #set style
    def set_serving_style(self,servingStyle_):
        self._style = servingStyle_
    #get flavor
    def get_iceCream_flav(self):
        return self._flavor
    #get scoops
    def get__num_of_scoops(self):
        return self._num_scoops
    #get style
    def get_serving_style(self):
        return self._style

    #using the __str__ method, accept input from the user to obtain our data
        print('please enter employee information')
    flav_ = input ('Enter Employee Name: ')
    scoo_ = input ('Enter Employee Number: ')
    serv_ = int(input('Enter Shift Number: '))

    ice = IceCream(flav_, scoo_, serv_)

    print ('your information which will be stored in a database and be able to be updated later')
    print ('Name: ',ice.get_iceCream_flav())
    print ('Employee Number: ',ice.get__num_of_scoops())
    print ('Shift Number: ',ice.get_serving_style())

    if flav_ != 'vanilla' 'chocolate' 'strawberry' 'mint' 'pistachio':
            raise Exception('item not on the menu')
    else:
            print ('thank you for your purchase')
