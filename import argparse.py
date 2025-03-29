import argparse
import os
import requests

# Function to read wordlist
def read_wordlist(wordlist_file):
    with open(wordlist_file, 'r') as f:
        return [line.strip() for line in f]

# Fuzzing function to check directories
def fuzz_directories(target_url, wordlist):
    print(f"Starting fuzzing on {target_url}...\n")
    for word in wordlist:
        url = os.path.join(target_url, word)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Found directory: {url} (Status Code: {response.status_code})")
            elif response.status_code == 301 or response.status_code == 302:
                print(f"[+] Found directory (redirect): {url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error with {url}: {e}")

# Main function to handle argument parsing and tool execution
def main():
    parser = argparse.ArgumentParser(description="Virgo Directory Buster")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL (e.g., http://example.com)")
    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Wordlist for directory names (e.g., /path/to/wordlist.txt)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (default 10)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    
    args = parser.parse_args()

    # Read wordlist
    wordlist = read_wordlist(args.wordlist)

    # Run the fuzzing function
    fuzz_directories(args.url, wordlist)

if __name__ == "__main__":
    main()
