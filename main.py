import argparse
import sys
import os

# Importing the modules
from modules.netscan import network_scan
from modules.brute_force import ssh_brute_force
from modules.hash_cracker import crack_hash
from modules.dir_brute_force import dir_brute_force

# Main function
def main():
    # Ensure temp directory exists
    os.makedirs("temp", exist_ok=True)
    
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="DarkProbe - A cybersecurity tool for network scanning, brute forcing, hash cracking, and directory brute forcing."
    )

    # Add arguments/flags
    parser.add_argument('-n', '--network', help='Perform a network scan on a specific IP or host', type=str)
    parser.add_argument('-b', '--bruteforce', help='Perform SSH brute force on a target server', type=str)
    parser.add_argument('-H', '--hash', help='Crack an MD5 hash', type=str)
    parser.add_argument('-d', '--directory', help='Perform a directory brute force on a website', type=str)

    # Parse the arguments
    args = parser.parse_args()

    # Process based on the provided argument
    if args.network:
        print(f"Performing network scan on {args.network}...")
        network_scan(args.network)
    elif args.bruteforce:
        print(f"Starting SSH brute force attack on {args.bruteforce}...")
        ssh_brute_force(args.bruteforce)
    elif args.hash:
        print(f"Cracking MD5 hash: {args.hash}...")
        crack_hash(args.hash)
    elif args.directory:
        print(f"Performing directory brute force on {args.directory}...")
        dir_brute_force(args.directory)
    else:
        print("No valid flag provided. Use -h or --help for help.")

if __name__ == "__main__":
    main()