"""
Arguments Module
~~~~~~~~~~~~~~~~

Adding and parsing all arguments, making them accessible.
"""

import argparse


parser = argparse.ArgumentParser(description = "Asymmetric Cryptography - RSA")

args = {}
key = lambda: args["key"]

def init_args() -> None:
    """
    Initializes all defined arguments.
    """
    
    # === Adding arguments === #
    parser.add_argument("-k", "--key", help = "Path to key (private/public)", required = True)
    
    # === Parsing arguments === #
    parsed_args = parser.parse_args()
    
    # === Making arguments accessible through constants === #
    args["key"] = parsed_args.key
