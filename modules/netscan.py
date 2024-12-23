import socket

def scan_port(host, port):
    """Port scan on a given host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except socket.error:
        print(f"Couldn't connect to port {port}")

def scan_ports(host, ports):
    """Scan multiple ports on a host."""
    for port in ports:
        scan_port(host, port)

if __name__ == "__main__":
    host = input("Enter the host or IP address to scan: ")
    ports = range(1, 1025)  # Scan ports from 1 to 1024
    scan_ports(host, ports)