# virgo
Virgo is a lightweight, fast, and customizable directory buster tool written in Python. It allows penetration testers, security researchers, and developers to quickly discover hidden directories or files on web servers through fuzzing.


# Virgo - A Fast Fuzzing Tool for Linux

**Virgo** is a lightweight, high-speed fuzzing tool designed for Linux, built in Python. It leverages asynchronous HTTP requests to quickly test web endpoints for vulnerabilities or hidden resources. Virgo is ideal for security researchers, penetration testers, and developers who need a fast and customizable fuzzing solution.

 Features
- **Asynchronous Requests**: Uses `asyncio` and `aiohttp` for blazing-fast fuzzing.
- **Premium Templates**: Includes built-in high-quality templates for common fuzzing scenarios.
- **Custom Wordlists**: Supports user-provided wordlists or generates random inputs.
- **Configurable**: Adjust delay, max requests, and templates via CLI.
- **Simple Setup**: Easy to install and use on any Linux system.

## Installation
1. **Install Dependencies**
   sudo apt update
   sudo apt install python3-pip
   pip3 install aiohttp
   git clone https://github.com/yourusername/virgo-fuzzer.git
   cd virgo-fuzzer
   chmod +x virgo.py

 # Usage
Basic fuzzing with default settings:
./virgo.py http://example.com/
./virgo.py -w /path/to/wordlist.txt http://example.com/

##**Fuzz with custom templates and delay:**
./virgo.py -t "{FUZZ}.php" "admin/{FUZZ}" -d 0.1 http://example.com/
./virgo.py -m 500 http://example.com/

**Features.**
Virgo includes the following built-in templates:

{FUZZ} - Basic fuzzing
admin/{FUZZ} - Admin directory fuzzing
{FUZZ}.php - PHP file fuzzing
api/v1/{FUZZ} - API endpoint fuzzing
{FUZZ}/login - Login path fuzzing
Additional templates are available in templates.txt.

**License
This project is licensed under the MIT License**

**Save the file, then add and push it to GitHub:
git add README.md
git commit -m "Added README file"
git push

**

