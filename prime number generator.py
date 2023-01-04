#ellena carmean
#9/15/22
#Prime Number Generator
#the following program will then generate a list of prime numbers between 2 and their number and store it in a list.

#first list
print('please enter a number to generate a list of prime numbers between 2 and their number and store it in a list.')

user_value = int(input('please enter a value:'))

primes = [i for i in range(2, user_value + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]

print(primes)