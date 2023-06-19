class Animal:
    def __init__(self):
        self._name = "ANIMLA"
        self.__gender = "MAKE"
        self.return_gender()
    def return_gender(self):
        print(self.__gender)
        return self.__gender
a = Animal()
print(a._name)