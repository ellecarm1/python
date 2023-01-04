#ellena carmean
#python
#10/17/22
#This program will accept a string from a user and compare it to a stored password in the file.  
#after 3 tries the user will be locked out of their acct

p = input('enter your password: ')
#first try
p1 = input('repeat your password: ')
if p != p1:
    for x in range(3):
        p1 = input('enter your password: ')
        if p1 == p:
            print('welcome')
            break
    else:
        print('user has exceeded potential tries, acct now locked, please contact IT admin for support')
else:
    print('welcome')