class Converter:
    def __init__(self, value):
        self.value = value
        self._name = "cheems"
        self.__gender = "male"
    def to_nepali(self):
        return self.value*100


nepali = Converter(8)
#
#print(nepali.to_nepali())
#print(nepali.__dict__)
#print("A new line")
#print(nepali.__dict__['value'])
#print(nepali._name)
#print(nepali.__dict__)
#print(nepali.__gender)

class Student:

    def __init__(self, fname, lname, grade):
        self.fname = fname
        self.lname = lname
        self.grade = grade

    def student_info(self):
        return f"{self.fname} {self.lname} studying in grade {self.grade}"
    
    def get_info(self):
        print("GETTING INFO")
        return f"Student name: {self.fname} {self.lname} Grade: {self.grade}"

    def set_info(self, fname, lname, grade):
        print("SETTING INFO")
        self.fname = fname
        self.lname = lname
        self.grade = grade
    
    def get_name(self):
        print("GETTINGNAME")
        return self.fname

    def set_name(self, name):
        self.fname = name

    info = property(get_info, set_info)
    fname = property(get_name, set_name)

student1 = Student('cheems', 'bahadur',10)
print(student1.student_info())
print(student1.set_info('dog', 'bhau', 12))
print(student1.get_info())
print(student1.student_info())



print("////")
print(student1.info)
print(student1.fname)

