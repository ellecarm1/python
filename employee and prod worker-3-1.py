#ellena carmean
#computer programming
#10/21/22
#this program will create employee classes and objects, 
#and will include accessors and mutators for those objects 
#then print the data given using the __str__ method

class Employee:

#initialize our class
#accessors and mutators for employee data
    def __init__(self,name,number):
        self.empName = name
        self.number = number

    def set_emp_name(self,name):
        self.empName = name

    def set_emp_number(self,number):
        self.__number = number

    def get_emp_name(self):
        return self.empName

    def get_emp_number(self):
        return self.number

#create our production class
class ProductionWorker(Employee):

#initialize our class
#accessors and mutators for employee data
    def __init__(self,name,number,shift_num,pay_rate):
        Employee.__init__(self,name,number)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    def set_shift_num(self,shift_num):
        self.__shift_num = shift_num

    def set_pay_rate(self,pay_rate):
        self.__pay_rate = pay_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rates(self):
        return self.__pay_rate

def main():

    #using the __str__ method, accept input from the user to obtain our data
    print('please enter employee information')
    name = input ('Enter Employee Name: ')
    number = input ('Enter Employee Number: ')
    shift = int(input('Enter Shift Number: '))
    pay = float(input('Enter Pay Rate: '))

    emp = ProductionWorker(name,number,shift,pay)

    print ('your information which will be stored in a database and be able to be updated later')
    print ('Name: ',emp.get_emp_name())
    print ('Employee Number: ',emp.get_emp_number())
    print ('Shift Number: ',emp.get_shift_num())
    currency_string = "${:,.2f}".format(pay)
    print(currency_string)
    print ('Pay Rate: ',emp.get_pay_rates())

main()