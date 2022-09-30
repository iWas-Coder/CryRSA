"""
Math Module
~~~~~~~~~~~~~~~~

(...)
"""


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


def factorize(N, progress):
    """
    (...)
    """
    
    compute_iters = lambda start, end, step: (end - start - 1) // step + 1
    
    sqrt = int(N ** 0.5) + 1
    iters = compute_iters(sqrt, 3, -2)
    
    for iter, i in enumerate(range(sqrt, 3, -2)):
        progress.status(f"Performing prime factorization...\nIters: {iter} / {iters}\nPercentage: {(iter/iters)*100} %")
        if N % i == 0:
            return i, int(N/i)
    
    return None, None
