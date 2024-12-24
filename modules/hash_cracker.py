import os

# Function for MD5 hash cracking
def crack_hash(md5_hash):
    # Define output directory for hash cracking
    output_dir = "temp/hash_cracked"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, f"{md5_hash}_cracked_result.txt")

    # Simulating hash cracking and writing to output file
    with open(output_file, 'w') as f:
        f.write(f"Hash cracking results for {md5_hash}...\n")
        f.write("Hash: e10adc3949ba59abbe56e057f20f883e\n")
        f.write("Original: 123456\n")
    
    print(f"Hash cracking result saved to {output_file}")
