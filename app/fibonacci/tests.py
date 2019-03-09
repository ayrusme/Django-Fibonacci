from django.test import TestCase

# Create your tests here.
from fibonacci.models import n_fibonacci

class FibonacciTestCase(TestCase):
    def test(self):
        """Check if fibonacci series is right"""
        self.assertEqual(n_fibonacci(1)[0], 1)
        self.assertEqual(n_fibonacci(2)[0], 1)
        self.assertEqual(n_fibonacci(3)[0], 2)
        self.assertEqual(n_fibonacci(4)[0], 3)
        self.assertEqual(n_fibonacci(5)[0], 5)
        self.assertEqual(n_fibonacci(6)[0], 8)
        self.assertEqual(n_fibonacci(7)[0], 13)
        self.assertEqual(n_fibonacci(8)[0], 21)
        self.assertEqual(n_fibonacci(9)[0], 34)

