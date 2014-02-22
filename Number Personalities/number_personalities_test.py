import unittest
from number_personalities import *

class TestNumberPersonalities(unittest.TestCase):

    def tell_about(self, fun, n, should_be):
        if fun(n) == should_be:
            return
        if should_be:
            self.fail(str(n) + " should be " + fun.__name__[3:])
        else:
            self.fail(str(n) + " should not be " + fun.__name__[3:])
        
    def test_is_prime(self):
        #self.tell_about(is_prime, 1, False)
        self.tell_about(is_prime, 2, True)
        self.tell_about(is_prime, 3, True)
        self.tell_about(is_prime, 4, False)
        self.tell_about(is_prime, 5, True)
        self.tell_about(is_prime, 6, False)
        self.tell_about(is_prime, 99, False)
        self.tell_about(is_prime, 97, True)
        self.tell_about(is_prime, 169, False)

    def test_is_happy(self):
        self.tell_about(is_happy, 1, True)
        self.tell_about(is_happy, 5, False)
        self.tell_about(is_happy, 7, True)
        self.tell_about(is_happy, 50, False)
        self.tell_about(is_happy, 79, True)
        self.tell_about(is_happy, 320, True)
        self.tell_about(is_happy, 1028, False)

    def test_is_triangular(self):
        self.tell_about(is_triangular, 1, True)
        self.tell_about(is_triangular, 2, False)
        self.tell_about(is_triangular, 3, True)
        self.tell_about(is_triangular, 5, False)
        self.tell_about(is_triangular, 6, True)
        self.tell_about(is_triangular, 21, True)
        self.tell_about(is_triangular, 30, False)
        self.tell_about(is_triangular, 55, True)

    def test_is_square(self):
        self.tell_about(is_square, 1, True)
        self.tell_about(is_square, 2, False)
        self.tell_about(is_square, 4, True)
        self.tell_about(is_square, 8, False)
        self.tell_about(is_square, 49, True)
        self.tell_about(is_square, 99, False)
        self.tell_about(is_square, 100, True)
        self.tell_about(is_square, 121, True)
        self.tell_about(is_square, 10000, True)
        self.tell_about(is_square, 10001, False)

    def test_is_smug(self):
        self.tell_about(is_smug, 1, False)
        self.tell_about(is_smug, 2, True)
        self.tell_about(is_smug, 3, False)
        self.tell_about(is_smug, 4, False)
        self.tell_about(is_smug, 5, True)
        self.tell_about(is_smug, 8, True)
        self.tell_about(is_smug, 34, True)
        self.tell_about(is_smug, 46, False)
        self.tell_about(is_smug, 85, True)
        self.tell_about(is_smug, 99, False)

    def test_is_honest(self):
        #self.tell_about(is_honest, 1, True)
        self.tell_about(is_honest, 3, True)
        self.tell_about(is_honest, 5, False)
        self.tell_about(is_honest, 36, True)
        self.tell_about(is_honest, 90, True)
        self.tell_about(is_honest, 1024, True)
        self.tell_about(is_honest, 1028, False)
         
        
unittest.main()
