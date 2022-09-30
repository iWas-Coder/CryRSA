"""
Math Module
~~~~~~~~~~~~~~~~

(...)
"""

from sympy.ntheory import factorint


def egcd(a, b):
    """
    (...)
    """
    
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """
    (...)
    """
    
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m


def factorize(N):
    """
    (...)
    """

    factors = factorint(N, verbose = True)
    if len(factors) == 2 and all(exp == 1 for exp in factors.values()):
        factors = list(factors.keys())
        return factors[0], factors[1]
