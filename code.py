import requests
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DiscordGiftCodeVerifier:
    def __init__(self, token):
        self.token = token
        self.url = "https://discord.com/api/v10/entitlements/gift-codes/{}"
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

    def verify_code(self, code):
        try:
            response = requests.get(self.url.format(code), headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data.get("valid"), data
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred for code {code}: {http_err}")
            return False, None
        except Exception as err:
            logging.error(f"An error occurred for code {code}: {err}")
            return False, None

    @staticmethod
    def read_codes(file):
        try:
            with open(file, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            logging.error(f"The file {file} was not found.")
            return []

    def verify_codes(self, codes):
        for code in codes:
            is_valid, info = self.verify_code(code)
            if is_valid:
                logging.info(f"The code {code} is valid and can be redeemed.")
            else:
                logging.warning(f"The code {code} is invalid or has already been redeemed.")
            time.sleep(1)  # Add a delay between requests to avoid rate limiting

def main():
    token = "YOUR_TOKEN_HERE"  # Replace with your token
    codes_file = "codes.txt"  # Replace with the path to your file

    verifier = DiscordGiftCodeVerifier(token)
    codes = verifier.read_codes(codes_file)

    if codes:
        verifier.verify_codes(codes)
    else:
        logging.error("No codes to verify.")

if __name__ == "__main__":
    main()
