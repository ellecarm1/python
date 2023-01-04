#ellena carmean
#computer programming
#10/21/22
#this program will create IceCream classes and objects, 
#and will include accessors and mutators for those objects 
#then print the data given using the __str__ method

user_list = [['usr1','vanilla'],['usr2','chocolate'],['usr3','mint']]

class IceCream:

#initialize our class
#accessors and mutators for IceCream flavor data



#initialize our class
#accessors and mutators for IceCream data
    def __init__(self,flavor,scoop_num,serving_style):
        self.__scoop_num = scoop_num
        self.__serving_style = serving_style

    def set_scoop_num(self,scoop_num):
        self.__scoop_num = scoop_num

    def set_serving_style(self,serving_style):
        self.__serving_style = serving_style

    def get_scoop_num(self):
        return self.__scoop_num

    def get_serving_styles(self):
        return self.__serving_style

    def set_icecream_Flav(self,flavor):
        self.iceFlavor = flavor

    def get_icecream_Flav(self):
        return self.iceFlavor

def main():
    x = 1
    
    while x != 4:
        flav = input("Please enter a flavor: ")
        if flav != 'vanilla':
            raise Exception('item not on the menu')
        scoops = input ('please enter number of scoops: ')
        if scoops != '3':
            raise Exception('item not on the menu')
        style = input('please enter serving style, bowl or cone?')
        if style != 'bowl':
            raise Exception('item not on the menu')

        ice = (flav, scoops, style)
        print(ice.get_icecream_Flav, ice.get_scoop_num, ice.get_serving_styles  )
        x += 1

main()