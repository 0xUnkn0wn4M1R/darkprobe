# darkprobe
DarkProbe

DarkProbe is a Python-based cybersecurity tool designed for network scanning, SSH password brute forcing, MD5 hash cracking, and website directory brute forcing. It is intended for security professionals who wish to test the security of systems and applications.

Table of Contents
	•	Installation
	•	Usage
	•	Ethical Usage Guidelines
	•	Contributing
	•	Licensing

Installation

Requirements:
	•	Python 3.6+
	•	Pip (Python package manager)

Steps:
	1.	Clone or Download the repository:

git clone https://github.com/your-username/DarkProbe.git


	2.	Install the required libraries:
Navigate to the project folder and run:

pip install -r requirements.txt


	3.	Place the necessary wordlists in the wordlists directory:
	•	passwords.txt: The password list.
	•	directories.txt: The list of directories to try.

Usage

To run the tool, use the main.py file. This script will prompt the user for input and run the corresponding security features. Below are the commands you can use:

Run the tool:

python main.py

Menu:
	1.	Network Scan: Perform a network scan on a specific IP or host.
	2.	SSH Brute Force: Perform an SSH brute force attack on a target server.
	3.	Hash Cracking (MD5): Crack an MD5 hash to reveal the original password.
	4.	Directory Brute Force: Perform a directory brute force attack on a website.
	5.	Exit: Exit the program.

Ethical Usage Guidelines

DarkProbe should only be used for ethical and authorized testing. It is intended for security testers, penetration testers, and cybersecurity professionals. It should not be used for damaging systems or networks. Below are some guidelines:
	1.	Do not use without permission: DarkProbe should only be used on systems or networks for which you have explicit permission. Unauthorized use may be illegal.
	2.	Limit your scope: Only scan systems or networks that you have permission to test.
	3.	Protect personal data: Do not attempt to crack or access personal or sensitive data using this tool.
	4.	Follow the law: Use this tool only in countries or regions where penetration testing and cybersecurity testing are legally permitted. Follow local laws.

Contributing

To contribute to this project, please follow these steps:
	1.	Fork this repository.
	2.	Create a new branch (git checkout -b feature-name).
	3.	Make your changes and commit them (git commit -am 'Add feature').
	4.	Push your branch (git push origin feature-name).
	5.	Open a Pull Request.

