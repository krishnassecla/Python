from dataclasses import dataclass

@dataclass
class Person:
	name:str = 'name'
	age:int = 0


cheems = Person('cheems', 19)
jude = Person('Jude', 21)
C = Person()
D = Person()
print(Person == Person)
print(id(Person), id(Person))
print(Person() == Person())
print(isinstance(Person(), Person))

class X:
	a = 'default'

A = X()
B = X()
print(isinstance(X(), X))
print(X()== X())
print(A == B)
print(C == D)


@dataclass
class Emp:
	name: str 
	# ls: list = (name, name)
	def __post_init__(self):
		self.x = self.name
cheems = Emp('cheems')
print(cheems.name)
print(cheems.x)