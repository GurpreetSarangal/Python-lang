# object oriented programming
# class => variables, functions ' . '
'''

class variables
object/instance variable



class student
    number of students =0 ==> class variable
    name 
    age
    rollno
    class
    fees_pending

    def __init__(self, name):
        self.name = name
        self.age
        self.rollno


    constructor => name , age, rollno, class, fees_pending
        assign all values to object variables


    func - show_class(self, ... )
        print - class
    
    func - name(self, ... )
        print - name
    
    func - fees(self, ... )
        print fees_pending

    destructor => 
        print("")

obj => student
obj.name='sandeep'
obj.age = 19
obj.class = 'bca 3'

obj.show_class()
obj.name()
    

obj2 => student
obj2.name = 'gurpreet'
obj2.age = 18
obj2.class = 'bca 3'

obj2.name()


obj.number_of_students
obj2.number_of_students
    
    '''

'''
class person
    name 
    age 
        constructor()

        distructor()

class student(person)
    roll_no
    course

        constructor()
            self.name
            self.age
            self.roll_no
            self.course

        distructor()

class class_representative(student)
    votes


class teacher(person)
    experties
    college
        constructor
            self.name
            self.age
            self.experties

class head_of_dept(person, teacher)
    department
        constructor()   
            self.name
            self.age
            self.experties
            self.college
            self.department
        

person 
||
student
||
CR
multilevel Inheritence

person , teacher
     ||
head of department
multiple inheritence



'''
