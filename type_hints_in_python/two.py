from typing import List, Tuple, TypeVar

T = TypeVar("T")  # Type variable


def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]


def pair_elements(a: T, b: T) -> Tuple[T, T]:
    return a, b


# Usage examples
string_list = ["apple", "banana", "cherry"]
reversed_list = reverse_list(string_list)  # inferred as List[str]

result = pair_elements(10, 20)  # inferred as Tuple[int, int]
print(type(result))
