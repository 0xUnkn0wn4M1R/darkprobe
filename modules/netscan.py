import os

# Function for network scanning
def network_scan(target):
    # Define output directory for network scan
    output_dir = "temp/netscan"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, f"{target}_scan_result.txt")

    # Simulating network scan and writing to output file
    with open(output_file, 'w') as f:
        f.write(f"Scanning results for {target}...\n")
        f.write("Port 22: Open\n")
        f.write("Port 80: Open\n")
        f.write("Port 443: Open\n")
    
    print(f"Network scan result saved to {output_file}")
