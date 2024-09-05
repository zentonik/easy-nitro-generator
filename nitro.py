import random
import string
import requests

def generate_code(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def check_code(code):
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(f"Valid Code Found: {code}")
        save_valid_code(code)
        return True
    elif response.status_code == 404:
        print(f"Invalid Code: {code}")
    else:
        print("")
    return False

def save_valid_code(code):
    with open("valid_codes.txt", "a") as file:
        file.write(f"{code}\n")
    print(f"Code saved to file: {code}")

def main():
    while True:
        code = generate_code()
        print(f"Checking Code: {code}")
        if check_code(code):
            break

if __name__ == "__main__":
    main()
