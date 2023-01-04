#ellena carmean
#9/15/22
#Prime Number Generator
#Write a program that asks how many tickets for each section were sold, 
#then display the amount of income generated from the ticket sales. 

#constants
A_TIX_PRICE = 25
B_TIX_PRICE = 20
C_TIX_PRICE = 15
D_TIX_PRICE = 10

#function 1
def printTix():
    #constants
    A_TIX_PRICE = 25
    B_TIX_PRICE = 20
    C_TIX_PRICE = 15
    D_TIX_PRICE = 10

print('tickets for ea section listed below')
print('a',"${:,.2f}".format(A_TIX_PRICE))
print('b',"${:,.2f}".format(B_TIX_PRICE))
print('c',"${:,.2f}".format(C_TIX_PRICE))
print('d',"${:,.2f}".format(D_TIX_PRICE))

printTix()

#function 2
def printIncome():

    A_TIX_SOLD = int(input('how many tix were sold in section a? '))
    B_TIX_SOLD = int(input('how many tix were sold in section b? '))
    C_TIX_SOLD = int(input('how many tix were sold in section c? '))
    D_TIX_SOLD = int(input('how many tix were sold in section d? '))

    TOTAL_INCOME_A = A_TIX_PRICE*A_TIX_SOLD
    TOTAL_INCOME_B = B_TIX_PRICE*B_TIX_SOLD
    TOTAL_INCOME_C = C_TIX_PRICE*C_TIX_SOLD
    TOTAL_INCOME_D = D_TIX_PRICE*D_TIX_SOLD
    total_sales = TOTAL_INCOME_A + TOTAL_INCOME_B + TOTAL_INCOME_C + TOTAL_INCOME_D

    print('total tix sold equals', A_TIX_SOLD + B_TIX_SOLD + C_TIX_SOLD + D_TIX_SOLD)

    section_opt = input('which section would you like to display tix sales for?' + '' + '\n type a for section a ' + '' + '\n type b for section b ' + '' + '\n type c for section c ' + '' + '\n type d for section d ')
    if section_opt == 'a':
        print('total sales for a: ',"${:,.2f}".format(TOTAL_INCOME_A))
    elif section_opt == 'b':
        print('total sales for b: ',"${:,.2f}".format(TOTAL_INCOME_B))
    elif section_opt == 'c':
        print('total sales for c: ',"${:,.2f}".format(TOTAL_INCOME_C))
    elif section_opt == 'd':
        print('total sales for d: ', "${:,.2f}".format(TOTAL_INCOME_D))

    print('total sales overall: ',"${:,.2f}".format(total_sales))

printIncome()

