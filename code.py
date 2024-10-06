import requests

def verify_code(token, code):
    url = f"https://discord.com/api/v10/entitlements/gift-codes/{code}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("valid"):
            return True, data  # Valid code
        else:
            return False, data  # Code already redeemed or invalid
    else:
        return False, response.text  # Error in the request

def read_codes(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Example usage
token = "YOUR_TOKEN_HERE"  # Replace with your token
codes_file = "codes.txt"  # Replace with the path to your file

codes = read_codes(codes_file)

for code in codes:
    is_valid, info = verify_code(token, code)
    if is_valid:
        print(f"The code {code} is valid and can be redeemed.")
    else:
        print(f"The code {code} is invalid or has already been redeemed.")
