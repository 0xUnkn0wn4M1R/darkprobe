import os

# Function for directory brute force
def dir_brute_force(target):
    # Define output directory for directory brute force
    output_dir = "temp/directory_brute_force"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, f"{target}_dir_brute_force_result.txt")

    # Simulating directory brute force and writing to output file
    with open(output_file, 'w') as f:
        f.write(f"Directory brute force results for {target}...\n")
        f.write("/admin - 200 OK\n")
        f.write("/login - 200 OK\n")
        f.write("/dashboard - 403 Forbidden\n")
    
    print(f"Directory brute force result saved to {output_file}")
