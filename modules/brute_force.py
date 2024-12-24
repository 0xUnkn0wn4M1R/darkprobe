import os

# Function for SSH brute force
def ssh_brute_force(target):
    # Define output directory for brute force
    output_dir = "temp/user_brute_force"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, f"{target}_brute_force_result.txt")

    # Simulating brute force and writing to output file
    with open(output_file, 'w') as f:
        f.write(f"Brute force attempt results for {target}...\n")
        f.write("Attempt 1: Failed\n")
        f.write("Attempt 2: Failed\n")
        f.write("Attempt 3: Success - Username: admin, Password: admin123\n")
    
    print(f"Brute force result saved to {output_file}")
