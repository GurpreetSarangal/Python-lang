class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

class teacher:
    def __init__(self, experties, college):
        # person.__init__(self, name, age)
        self.experties = experties
        self.college = college

    def show(self):
        print(self.experties)
        print(self.college)

# multiple inheritence
class head_of_department(person, teacher):
    def __init__(self, name, age, experties, college, department):
        person.__init__(self, name, age)
        teacher.__init__(self, experties, college)
        self.department = department

    
    def show(self):
        person.show(self)
        teacher.show(self)
        print(self.department)
# insert into employees values (100, "name", "address","salary")
# len()
# min()
# max()
# sum()



vik = head_of_department("Vikram Sharma",55,"CA","DAV","CS")

vik.show()