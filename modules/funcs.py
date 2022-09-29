"""
Functions Module
~~~~~~~~~~~~~~~~

(...)
"""

import math
from pwn import *
from modules.timeout import timeout


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


def factorize(n):
    """
    (...)
    """
    
    sqrt = int(n ** 0.5) + 1
    for i in range(sqrt, 3, -2):
        if n % i == 0:
            return i, int(n/i)
