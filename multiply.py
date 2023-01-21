import unittest

def multiply_3_numbers(one, two, three):
    result = one * two * three
    return result

#print(multiply_3_numbers(2,1,3))

class Test_multiply_3s(unittest.TestCase):
    '''Contains unit test functions'''

    def test_1(self):
        one = 2
        two = 1
        three = 3
        result = multiply_3_numbers(2, 1, 3)
        self.assertEqual(result, 6)

    def test_2(self):
        one = 0
        two = 1
        three = 3
        result = multiply_3_numbers(0, 1, 3)
        self.assertEqual(result, 0)

    def test_3(self):
        one = -2
        two = 1
        three = 3
        result = multiply_3_numbers(-2, 1, 3)
        self.assertEqual(result, -6)

if __name__ == '__main__':
    unittest.main()