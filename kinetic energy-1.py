#ellena carmean
#computer programming
#9/19/22
#this program calculates the kinetic energy of a moving object

#this is our function with our formula
def kinectic_energy():

    m = float(input('please enter the mass in kilograms:'))

    v = float(input('please entery the velocity in meters per second:'))

    print('The object has a mass of', m, 'kilograms, a velocity of', v, ' meters per second')

    energy__ = 0.5 * m * v * v

    print('The object\'s kinetic energy is', energy__,'joules')

    

#we call our function
kinectic_energy()
