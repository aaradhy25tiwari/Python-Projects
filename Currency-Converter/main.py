"""Currency Converter using Free Currency API"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

def convert_currency(base, target):
    """Fetch conversion rate from base currency to target currency."""
    try:
        response = requests.get(f"{BASE_URL}&base_currency={base}&currencies={target}", timeout=10)
        data = response.json()
        if response.status_code != 200:
            print(f"Error: {data.get('error', 'Unknown error occurred')}")
            return None
        return data['data']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input("Enter amount to convert: "))

    rates = convert_currency(base_currency, target_currency)
    if rates:
        if target_currency in rates:
            converted_amount = rates[target_currency]
            print(f"1 {base_currency} = {converted_amount:.2f} {target_currency}")
            print(f"{amount} {base_currency} = {amount * converted_amount:.2f} {target_currency}")
        else:
            print(f"Currency {target_currency} not found in the response.")
