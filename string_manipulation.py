#ellena carmean
#python
#10/17/22
#this program accepts a string as an argument and returns a copy for
#the string in the following formats

#loop to exit
User_Str = input('Enter a string:')
if User_Str.isalpha() == False:
        print('Please enter a alphabetical name')
else:
    print('Original String: ' + User_Str)
#the first character of each sentence capitalized
    print('first char capitalized: ' + User_Str.capitalize())
#the entire string in all caps
    print('entire str in all caps: ' + User_Str.upper())
#the entire string in all lowercase
    print('entire str in all lowercase: ' + User_Str.lower())
#the entire string in title case
    print('entire str in title case: ' + User_Str.title())
exit(0)
