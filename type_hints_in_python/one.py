# Vector = list[float]
# # here Vector is a type alias
# print(Vector)
# Vector2: list[float] = [1, 2, 3]
# print(Vector2)


# def scale(scalar: float, vector: Vector) -> Vector:
#     return [scalar * num for num in vector]


# new_vector = scale(2.0, [1.0, 2.4, 5.1])
# print(new_vector)


from typing import TypeAlias
from typing import NewType

# this is not a normal variable assignment
Vector: TypeAlias = list[float]
print(type(Vector))

UserId = NewType("UserId", int)
print(type(UserId))
first_user = UserId(1)
print(type(first_user))
some_id = UserId(2341)
print(type(some_id))


def get_user_name(user_id: UserId) -> str:
    pass


user_a = get_user_name(UserId(234))

user_b = get_user_name(-1)

output = UserId(1) + UserId(2)
print(output)

# you cannot create subtype of derived

# UserId = NewType("UserId", int)
# print(UserId, type(UserId))


# not possible to create subclass of "derived type alias"
# class AdminUserId(UserId):
#     pass


UserId = NewType("UserId", int)
ProUserId = NewType("ProUserId", UserId)
print(UserId == ProUserId)
