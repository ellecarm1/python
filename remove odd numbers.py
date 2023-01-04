#ellena carmean
#9/13/22
#remove even numbers
#this code will remove odd numbers from a given max value

maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))