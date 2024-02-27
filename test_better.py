import unittest
from better import fizzbuzz

class TestBetter(unittest.TestCase):

    def test_multiples_of_three(self):
        multiples_of_three = [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]
        for num in multiples_of_three:
            self.assertEqual(fizzbuzz(num), 'Three')

    def test_multiples_of_five(self):
        multiples_of_five = [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]
        for num in multiples_of_five:
            self.assertEqual(fizzbuzz(num), 'Five')

    def test_multiples_of_three_and_five(self):
        multiples_of_three_and_five = [15, 30, 45, 60, 75, 90]
        for num in multiples_of_three_and_five:
            self.assertEqual(fizzbuzz(num), 'ThreeFive')

    def test_not_multiples_of_three_or_five(self):
        not_multiples_of_three_or_five = [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49, 52, 53, 56, 58, 59, 61, 62, 64, 67, 68, 71, 73, 74, 76, 77, 79, 82, 83, 86, 88, 89, 91, 92, 94, 97, 98]
        for num in not_multiples_of_three_or_five:
            self.assertEqual(fizzbuzz(num), num)

if __name__ == '__main__':
    unittest.main()
