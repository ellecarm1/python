#ellena carmean
#9/15/22
#List Comprehension
#This program will create lists of numbers in 4 different ways

#first list
print('the following prompts will ask you to enter\n2 integers to display a list of all numbers between\nand including those numbers')

#variables
min_num = int(input('enter your first number:'))
max_num = int(input('enter your second number:'))
#range
# create a list using list comprehension
user_list = [ x for x in range(min_num,max_num)]

print(user_list)

#second list
print('the following prompts will ask you to enter\n2 integers and display a list of the squares all\nnumbers between and including those numbers')

#variables
min_num = int(input('enter your first number:'))
max_num = int(input('enter your second number:'))

# create a list using list comprehension
squares = [min_num**2 for x in range(max_num)]

print(squares)

#third list
print('the following prompts will ask you to enter\n2 integers and display a list of all the even numbers\nbetween and including those numbers')

#variables
min_num = int(input('enter your first number:'))
max_num = int(input('enter your second number:'))

# create a list using list comprehension
even_numbers = [ x for x in range(min_num,max_num) if x % 2 == 0]

print(even_numbers)

#fourth list
print('2 integers and display a list of all the odd\nnumbers between and including those numbers')

#variables
min_num = int(input('enter your first number:'))
max_num = int(input('enter your second number:'))

# create a list using list comprehension
odd_numbers = [ x for x in range(min_num,max_num) if x % 3 == 0]

print(odd_numbers)

