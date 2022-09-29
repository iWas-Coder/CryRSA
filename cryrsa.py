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
    
    extract = log.progress("EXTRACT")
    
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
        log.info(f"d: {funcs.modinv(key.e, m)}")
        
        extract.success("Done! :)")
    else:
        extract.failure("No private component found :(")
        time.sleep(1)
        compute = log.progress("COMPUTE")
        
        compute.status("Performing prime factorization...")
        p, q = funcs.factorize(8633)
        if p and q:
            log.info(f"p: {p}")
            log.info(f"q: {q}")
            time.sleep(2)
            
            m = key.n - (p + q -1)
            log.info(f"m: {m}")
            log.info(f"d: {funcs.modinv(key.e, m)}")
            compute.success("Done! :)")
        else:
            compute.failure("No factors found :(")


if __name__ == "__main__":
    main()
