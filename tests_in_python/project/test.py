import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of ints
        """
        data = [2, 3, 1]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """Test for a list of fractions"""
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        # data created as input i.e fixture
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

    @unittest.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
    def test_add_numbers(self, a, b, expected):
        result = add_numbers(a, b)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()


# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def __eq__(self, other):
#         if isinstance(other, Circle):
#             return self.radius == other.radius
#         return False


# obj1 = Circle(5)
# obj2 = Circle(5)

# print(obj1 == obj2)
# print(obj1 is obj2)
