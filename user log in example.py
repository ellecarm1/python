user_list = [['usr1','vanilla'],['usr2','chocolate'],['usr3','mint']]

flav = input("Please enter a flavor: ")

while True:
     if flav == '':
          flav = input("Please enter a flavor: ")
     else:
          for user in user_list:
               if flav in [lst[1] for lst in user_list]:
                    break # break out for loop
                
          else:
                #this is where our custom exception will be
               flav = input ('we do not have that flavor, press enter to continue')
               raise Exception('item not on the menu')
               continue # continue the while loop
          break # break out while loop
scoops = input ('please enter number of scoops: ')
style = input('please enter serving style, bowl or cone?')
print("here is your receipt",flav, scoops, style)