import hashlib

def crack_hash(hash_to_crack, wordlist):
    """Try to crack the hash using a wordlist."""
    for word in wordlist:
        # Hash each word from the wordlist and compare
        hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
        if hashed_word == hash_to_crack:
            print(f"Found! The password is: {word}")
            return word
    print("Hash not cracked.")
    return None

if __name__ == "__main__":
    # Read the hash to crack
    hash_to_crack = input("Enter the hash to crack (MD5): ")

    # Read the wordlist
    with open('wordlists/passwords.txt', 'r') as file:
        wordlist = [line.strip() for line in file.readlines()]

    crack_hash(hash_to_crack, wordlist)