from dataclasses import dataclass


@dataclass(frozen=True)
class Animal:
    # these are fields
    name: str = "Dog"
    gender: str = "Male"


a = Animal
print(a.name, a.gender)
print(Animal.name, Animal.gender)
cat = Animal(name="BobCat")
print(cat.name)
print(cat.__repr__())
print(Animal.__repr__(Animal))
# cat.name = "NewBobCat"  # frozen= True will not let use __setattr__
print(cat.__match_args__)


# @dataclass
# class C:
#     a: int
#     b: int = 0


# c1 = C()

from dataclasses import field


@dataclass
class C:
    mylist: list[int] = field(default_factory=list)


c = C()
print(c.mylist)
c.mylist += [1, 2, 3]
print(c.mylist)


class Car:
    def __init__(self) -> None:
        self.brands = []


# @dataclass
# class Car:
#     brands: int = [] #we cannot give mutable default so we use default_factory


lambo = Car()
print(lambo.brands)
lambo.brands.append("Urus")
print(lambo.brands)

ferrari = Car()
print(ferrari.brands)
