#Link - https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4


# A class cannot
class Employee:
    raise_amount=1.04
    num_of_emps=0
    # KNOWN AS DUNDER INIT
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps +=1
    #USED TO HELP OTHER SDE UNDERSTAND CODE AND WHAT CREATED THE INSTANCE    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())  
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    #regular instance methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay *self.raise_amount)
#       self.pay=int(self.pay *self.raise_amount)    even this works
# first it will chekc if instance has raise amount else it will check if class or inherited class conatins the raise amount
    
    #class will be the fisrt argument instead of self(instance)
    #alternative constructor
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        #cls(first,last,pay) even this works in return
        return Employee(first,last,pay)
    #static methods dont take seld or class as first argument
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


#this means Developer inherit from Employee
class Developer(Employee):
    raise_amount=1.30
    def __init__(self, first, last, pay, prog_lang):
        #can also call emplyee directly
        # Employee.__init__(self,first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang    

    
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            

print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
print(Employee.num_of_emps)
emp_2 = Employee('Test', 'Employee', 60000)
print(Employee.num_of_emps)
emp_3 = Employee('aadil', 'raf', 2000)
print(Employee.num_of_emps)

emp_str_4='John-Doe-5032'

#first,last,pay =emp_str_4.split('-')
#emp_4=Employee(first,last,pay)

emp_4=Employee.from_string(emp_str_4)
print(Employee.num_of_emps)


emp_3.raise_amount=1.9
Employee.set_raise_amt(1.1)  
Developer.set_raise_amt(1.8)   


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)
print(Employee.num_of_emps)


import datetime
mydate=datetime.date(2022,1,3)
print(Employee.is_workday(mydate))


dev_1 = Developer('Luke', 'Peng', 50000,'Python')
print(Developer.num_of_emps)
print(dev_1.email)
dev_2 = Developer('Hassa', 'yahya', 60000,'R')
print(dev_2.email)
print(Developer.num_of_emps)
print(Employee.num_of_emps)



### IMPORTANT ==>print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

##PRINTS EMPLUYEE OBJ
print('\n \nPRINTS EMPLUYEE OBJ: ')
print(emp_1.__dict__)

##PRINTS EMPLUYEE CLASS
print('\n \n PRINTS EMPLUYEE CLASS: ')
print(Employee.__dict__)

print('\n \n PRINTS mgr obj: ')
print(mgr_1.__dict__)

print(isinstance(mgr_1,Developer))
print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))

print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))

#DONE BECUAASE OF ADD
print(emp_1 + emp_2)
#DONE BECUAASE OF LEN
print(len(emp_1))






