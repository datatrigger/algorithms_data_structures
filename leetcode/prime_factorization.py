def prime_factors(n: int):

    factors = []

    if n < 2:
        return factors
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2

    if n > 1:
        factors.append(n)

    return factors

from unittest import TestCase

class PrimeTest(TestCase):
    def test(self):
        self.assertEqual(prime_factors(0), [])
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(3), [3])
        self.assertEqual(prime_factors(4), [2, 2])
        self.assertEqual(prime_factors(5), [5])
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(60), [2, 2, 3, 5])
        self.assertEqual(prime_factors(37), [37])
        

PrimeTest().test()