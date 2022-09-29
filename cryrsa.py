#!/usr/bin/env python3

from pwn import *
import modules.args as args
import modules.funcs as funcs

from Crypto.PublicKey import RSA
import time


# === MAIN === #
def main():
    """
    Main program flow.
    """
    
    # Arguments
    args.init_args()
    
    # Import Key
    with open(args.key(), 'r') as f:
        key = RSA.importKey(f.read())
    
    p = log.progress("CryRSA")
    p.status("Extracting components...")
    time.sleep(2)
    
    log.info(f"e: {key.e}")
    log.info(f"n: {key.n}")
    
    if key.has_private():
        log.info(f"p: {key.p}")
        log.info(f"q: {key.q}")
        m = key.n - (key.p + key.q - 1)
        log.info(f"m: {m}")
        log.info(f"d: {funcs.modinv(key.e, m)}")
    else:
        p.status("Performing Prime Factorization:")
        print(funcs.factorize(2022))


if __name__ == "__main__":
    main()
