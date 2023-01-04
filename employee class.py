#ellena carmean
#computer programming
#10/18/22
#this program will create employee classes and display them

#create class
class employee:

#the init method or constructor
    def __init__(self, name, id, dep, job):
#instance attributes
        self.name = name
        self.id = id
        self.dep = dep
        self.job = job

#create instance of object
Susan = employee(name = 'Susan Meyers', id = '47899', dep = 'accting', job = 'vice president')
Mark = employee(name = 'Mark Jones', id = '39119', dep = 'information tech', job = 'programmer')
Joy = employee(name = 'Joy Rogers', id = '81774', dep = 'manufacturing', job = 'engineer')
# displayEmployee method of class employee
print(Susan.name, Susan.id, Susan.dep, Susan.job)
print(Mark.name, Mark.id, Mark.dep,Mark.job)
print(Joy.name, Joy.id, Joy.dep, Joy.job)