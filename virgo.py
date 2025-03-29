#!/usr/bin/env python3
import asyncio
import aiohttp
import argparse
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor

# Default premium templates for fuzzing
PREMIUM_TEMPLATES = [
    "{FUZZ}",              # Basic fuzzing
    "admin/{FUZZ}",        # Admin directory fuzzing
    "{FUZZ}.php",          # PHP file fuzzing
    "api/v1/{FUZZ}",       # API endpoint fuzzing
    "{FUZZ}/login",        # Login path fuzzing
]

class VirgoFuzzer:
    def __init__(self, url, wordlist=None, templates=None, delay=0, max_requests=1000):
        self.url = url
        self.wordlist = wordlist or self.generate_random_words(1000)
        self.templates = templates or PREMIUM_TEMPLATES
        self.delay = delay
        self.max_requests = max_requests
        self.results = []

    def generate_random_words(self, count):
        """Generate random strings if no wordlist is provided."""
        return [''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) for _ in range(count)]

    async def fetch(self, session, url):
        """Perform an asynchronous HTTP GET request."""
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                return response.status, await response.text()
        except Exception as e:
            return 0, str(e)

    async def fuzz_endpoint(self):
        """Fuzz the target URL with templates and wordlist."""
        async with aiohttp.ClientSession() as session:
            tasks = []
            for template in self.templates:
                for word in self.wordlist[:self.max_requests]:
                    fuzz_url = self.url + template.replace("{FUZZ}", word)
                    tasks.append(self.fetch(session, fuzz_url))
                    if self.delay > 0:
                        await asyncio.sleep(self.delay)

            responses = await asyncio.gather(*tasks)
            for status, content in responses:
                self.results.append((status, content))

    def run(self):
        """Run the fuzzer."""
        start_time = time.time()
        asyncio.run(self.fuzz_endpoint())
        end_time = time.time()
        print(f"\nFuzzing completed in {end_time - start_time:.2f} seconds.")
        self.display_results()

    def display_results(self):
        """Display fuzzing results."""
        print("\nResults:")
        for status, content in self.results:
            if status >= 200 and status < 300:
                print(f"[{status}] Success - {content[:50]}...")
            elif status > 0:
                print(f"[{status}] Failed")

def main():
    parser = argparse.ArgumentParser(description="Virgo - A fast fuzzing tool for Linux")
    parser.add_argument("url", help="Target URL to fuzz (e.g., http://example.com/)")
    parser.add_argument("-w", "--wordlist", help="Path to custom wordlist file")
    parser.add_argument("-t", "--templates", nargs="+", help="Custom templates (e.g., '{FUZZ}.php')")
    parser.add_argument("-d", "--delay", type=float, default=0, help="Delay between requests in seconds")
    parser.add_argument("-m", "--max", type=int, default=1000, help="Max number of requests")
    args = parser.parse_args()

    # Load wordlist if provided
    wordlist = None
    if args.wordlist:
        with open(args.wordlist, "r") as f:
            wordlist = [line.strip() for line in f]

    fuzzer = VirgoFuzzer(
        url=args.url,
        wordlist=wordlist,
        templates=args.templates,
        delay=args.delay,
        max_requests=args.max
    )
    fuzzer.run()

if __name__ == "__main__":
    main()