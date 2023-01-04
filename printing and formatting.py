#ellena carmean
#python
#10/17/22
#this program accepts a string as an argument and returns a copy for
#the string in the following formats

from tkinter import N

#print on new lines
print('the quick brown fox\njumps over\nthe lazy dog')

#print currency
amount = 1123456.75

currency = "${:,.2f}".format(amount)

print('I just made ' + currency + 'in the lottery!')

#print string using \ to allow apostrophe
print('I\'ve seen it all and i\'m still in shock!')

print('1). Item 1\n2). Item 2\n3). Item 3')

print('Programming', 'Essentials', 'in...python', sep = '***' , end = '')
