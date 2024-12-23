import argparse
import sys

# Import your functions for each module (network scan, brute force, hash cracking, etc.)
from modules.netscan import network_scan
from modules.brute_force import ssh_brute_force
from modules.hash_cracker import crack_hash
from modules.dir_brute_force import dir_brute_force

# Define the main function
def main():
    # Display tool name and copyright information
    print("""
    ***************************************
    DarkProbe - A Cybersecurity Tool
    ***************************************
    Copyright (c) 0xUnkn0wn4M1R
    ***************************************
    """)

    # Create the argument parser
    parser = argparse.ArgumentParser(description="DarkProbe - A cybersecurity tool for network scanning, brute forcing, hash cracking, and directory brute forcing.")

    # Add arguments/flags for each option
    parser.add_argument('-n', '--network', help='Perform a network scan on a specific IP or host', type=str)
    parser.add_argument('-b', '--bruteforce', help='Perform SSH brute force on a target server', type=str)
    parser.add_argument('-H', '--hash', help='Crack an MD5 hash', type=str)
    parser.add_argument('-d', '--directory', help='Perform a directory brute force on a website', type=str)

    # Parse the arguments
    args = parser.parse_args()

    # Check which flag is provided and run the corresponding function
    if args.network:
        print(f"Performing network scan on {args.network}...")
        network_scan(args.network)  # Call your network scan function from modules

    elif args.bruteforce:
        print(f"Starting SSH brute force attack on {args.bruteforce}...")
        ssh_brute_force(args.bruteforce)  # Call your brute force function from modules

    elif args.hash:
        print(f"Cracking MD5 hash: {args.hash}...")
        crack_hash(args.hash)  # Call your hash cracking function from modules

    elif args.directory:
        print(f"Performing directory brute force on {args.directory}...")
        dir_brute_force(args.directory)  # Call your directory brute force function from modules

    else:
        print("No valid flag provided. Use -h or --help for help.")

if __name__ == "__main__":
    main()