class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)
    

class student(person):
    number_of_students = 0

    def __init__(self, name, age, course):
        person.__init__(self,name,age)
        self.course = course
        student.number_of_students += 1
    
    def __del__(self):
        # print(self.name)
        print("This is distructor")
    
    def show_course(self):
        print(self.course)

# multilevel inheritence
class CR(student):
    def __init__(self, name, age, course, votes):
        student.__init__(self,name, age, course)
        self.votes = votes

    def show_votes(self):
        print(self.votes)


obj = student("sandeep",19,"BCA")
print(obj.number_of_students)

obj2 = CR("sandeep",19,"BCA",100)
print(obj2.number_of_students)

obj.show_name()