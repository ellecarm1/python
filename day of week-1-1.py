#ellena carmean
#9/8/22
#day of the week
#this code will ask the user to select a number between 1 and 7 and depending on the  
#number this program will display a message to the user what day of the week it is

while True:
    weekday= int(input('please enter the day of the week, 1-7?'))

    if weekday == 1:
       print('Monday')
    elif weekday == 2:
       print('Tuesday')
    elif weekday == 3:
       print('Wednesday')
    elif weekday == 4:
       print('Thursday')
    elif weekday == 5:
       print('Friday')
    elif weekday == 6:
       print('Saturday')
    elif weekday == 7:
       print('Sunday')
    else:
       print('Huh?')