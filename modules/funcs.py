"""
Functions Module
~~~~~~~~~~~~~~~~

(...)
"""

import math
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


# 30min timeout if not found any.
@timeout(1800)
def factorize(n):
    """
    (...)
    """
    
    poss_p = math.floor(math.sqrt(n))
    if poss_p % 2 == 0:
        poss_p += 1
    while poss_p < n:
        if n % poss_p == 0:
            return poss_p
        poss_p += 2
