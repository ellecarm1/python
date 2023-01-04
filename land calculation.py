#ellena carmean
#python
#8/29/22
#this program will recieve input of sq ft from the user and calculate the number of acres

#declare variables
NUM_SQ_FT = float(input("enter the number of square feet in the tract:"))
NUM_ACRES = NUM_SQ_FT / 43560
print('the size of the tract', NUM_ACRES, 'acres')