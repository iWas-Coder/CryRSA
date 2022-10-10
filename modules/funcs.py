"""
Functions Module
~~~~~~~~~~~~~~~~

Module that wraps all global functionalities.
"""

from pwn import *
from Crypto.PublicKey import RSA
import modules.args as args
import modules.math as math
import time
import sys
import signal


def ctrl_c():
    """
    Trap SIGINT signal when doing 'Ctrl + C', and
    redirect the program flow to the handler function.
    """
    
    def def_handler(sig, frame):
        log.warn("Process cancelled by user D:")
        sys.exit(1)
    signal.signal(signal.SIGINT, def_handler)


def import_key():
    """
    Import the key to work with it more easily.
    """
    
    with open(args.key(), 'r') as f:
        return RSA.importKey(f.read())


def extract(key: RSA.RsaKey):
    """
    Get and extract all components (public & private)
    from the key.
    """
    
    extract = log.progress("Extraction")
    
    extract.status("Extracting public components...")
    time.sleep(2)
    
    log.info(f"e: {key.e}")
    log.info(f"n: {key.n}")
    
    time.sleep(1)
    
    if key.has_private():
        extract.status("Extracting private components...")
        time.sleep(2)
        
        log.info(f"p: {key.p}")
        log.info(f"q: {key.q}")
        m = key.n - (key.p + key.q - 1)
        log.info(f"m: {m}")
        log.info(f"d: {math.modinv(key.e, m)}")
        
        extract.success("Done! :)")
    else:
        extract.failure("No private component found :(")
        time.sleep(1)
        d, p, q = compute(key)
        if d and p and q:
            private_key = RSA.construct((key.n, key.e, d, p , q))
            print(private_key.decode())


def compute(key: RSA.RsaKey):
    """
    Compute private components of the key by factorizing N
    into p,q.
    """
    
    compute = log.progress("Compute")
    compute.status("Performing prime factorization...")
    p, q = math.factorize(key.n)
    
    if p and q:
        log.info(f"p: {p}")
        log.info(f"q: {q}")
        compute.success("Done! :)")
        
        m = key.n - (p + q - 1)
        log.info(f"m: {m}")
        d = math.modinv(key.e, m)
        log.info(f"d: {d}")
        
        return d, p, q
    else:
        compute.failure("No factors found :(")
        return None, None, None
