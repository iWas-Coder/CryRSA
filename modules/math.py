"""
Math Module
~~~~~~~~~~~~~~~~

Module that wraps all mathematical tasks.
"""

from sympy.ntheory import factorint


def egcd(a, b):
    """
    Extended Euclidean Algorithm (EEA) implementation.
    """
    
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """
    Inverse multiplicative modular function implementation.
    """
    
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m


def factorize(N):
    """
    Factorize integer N to two prime numbers p,q.
    """

    factors = factorint(N, verbose = True)
    if len(factors) == 2 and all(exp == 1 for exp in factors.values()):
        factors = list(factors.keys())
        return factors[0], factors[1]
