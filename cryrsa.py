#!/usr/bin/env python3


import modules.args as args
import modules.funcs as funcs


# === MAIN === #
def main():
    """
    Main program flow.
    """
    
    # Arguments
    args.init_args()
    
    # Import Key
    key = funcs.import_key()
    
    # Extract public & private components
    funcs.extract(key)


if __name__ == "__main__":
    main()
