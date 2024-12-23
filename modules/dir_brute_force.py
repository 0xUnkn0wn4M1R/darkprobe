import requests

def brute_force_directories(base_url, wordlist):
    """Brute force directories on a website."""
    for dir in wordlist:
        url = f"{base_url}/{dir}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Found directory: {url}")
        else:
            print(f"Failed to find: {url}")

if __name__ == "__main__":
    # Base URL of the website
    base_url = input("Enter the base URL (e.g., http://example.com): ")
    
    # Read the wordlist (directories to try)
    with open('wordlists/directories.txt', 'r') as file:
        wordlist = [line.strip() for line in file.readlines()]

    brute_force_directories(base_url, wordlist)