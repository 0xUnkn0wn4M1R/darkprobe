import os
from modules.netscan import perform_network_scan
from modules.brute_force import brute_force_ssh
from modules.hash_cracker import crack_hash
from modules.dir_brute_force import brute_force_directories

def show_menu():
    print("\nDarkProbe - Select an option:")
    print("1. Network Scan")
    print("2. SSH Brute Force")
    print("3. Hash Cracking (MD5)")
    print("4. Directory Brute Force")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            host = input("Enter target IP or host for network scan: ")
            perform_network_scan(host)
        
        elif choice == '2':
            host = input("Enter the host/IP for SSH brute force: ")
            username = input("Enter the username for SSH: ")
            with open('wordlists/passwords.txt', 'r') as file:
                passwords = [line.strip() for line in file.readlines()]
            brute_force_ssh(host, username, passwords)

        elif choice == '3':
            hash_to_crack = input("Enter the MD5 hash to crack: ")
            with open('wordlists/passwords.txt', 'r') as file:
                wordlist = [line.strip() for line in file.readlines()]
            crack_hash(hash_to_crack, wordlist)

        elif choice == '4':
            base_url = input("Enter the base URL (e.g., http://example.com): ")
            with open('wordlists/directories.txt', 'r') as file:
                wordlist = [line.strip() for line in file.readlines()]
            brute_force_directories(base_url, wordlist)

        elif choice == '5':
            print("Exiting DarkProbe. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()