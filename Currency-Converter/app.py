from flask import Flask, render_template, request, flash
import os
from dotenv import load_dotenv

load_dotenv()

# Import the existing conversion function from main.py
from main import convert_currency

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")

# Supported currencies for dropdowns (code, display name)
CURRENCIES = [
    ("EUR", "Euro"),
    ("USD", "US Dollar"),
    ("JPY", "Japanese Yen"),
    ("BGN", "Bulgarian Lev"),
    ("CZK", "Czech Republic Koruna"),
    ("DKK", "Danish Krone"),
    ("GBP", "British Pound Sterling"),
    ("HUF", "Hungarian Forint"),
    ("PLN", "Polish Zloty"),
    ("RON", "Romanian Leu"),
    ("SEK", "Swedish Krona"),
    ("CHF", "Swiss Franc"),
    ("ISK", "Icelandic Króna"),
    ("NOK", "Norwegian Krone"),
    ("HRK", "Croatian Kuna"),
    ("RUB", "Russian Ruble"),
    ("TRY", "Turkish Lira"),
    ("AUD", "Australian Dollar"),
    ("BRL", "Brazilian Real"),
    ("CAD", "Canadian Dollar"),
    ("CNY", "Chinese Yuan"),
    ("HKD", "Hong Kong Dollar"),
    ("IDR", "Indonesian Rupiah"),
    ("ILS", "Israeli New Sheqel"),
    ("INR", "Indian Rupee"),
    ("KRW", "South Korean Won"),
    ("MXN", "Mexican Peso"),
    ("MYR", "Malaysian Ringgit"),
    ("NZD", "New Zealand Dollar"),
    ("PHP", "Philippine Peso"),
    ("SGD", "Singapore Dollar"),
    ("THB", "Thai Baht"),
    ("ZAR", "South African Rand"),
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    rate = None

    # Default form values
    base_value = "USD"
    target_value = "EUR"
    amount_value = ""

    if request.method == 'POST':
        base_value = request.form.get('base', '').strip().upper()
        target_value = request.form.get('target', '').strip().upper()
        amount_value = request.form.get('amount', '').strip()

        # Basic validation
        if not base_value or not target_value or not amount_value:
            flash('Please provide base currency, target currency and amount.', 'danger')
            return render_template('index.html', result=None, currencies=CURRENCIES, base_value=base_value, target_value=target_value, amount_value=amount_value)

        try:
            amount = float(amount_value)
        except ValueError:
            flash('Amount must be a number.', 'danger')
            return render_template('index.html', result=None, currencies=CURRENCIES, base_value=base_value, target_value=target_value, amount_value=amount_value)

        rates = convert_currency(base_value, target_value)
        if not rates:
            flash('Failed to fetch rates. Check your API key and network connection.', 'danger')
            return render_template('index.html', result=None, currencies=CURRENCIES, base_value=base_value, target_value=target_value, amount_value=amount_value)

        if target_value not in rates:
            flash(f'Currency {target_value} not found in API response.', 'warning')
            return render_template('index.html', result=None, currencies=CURRENCIES, base_value=base_value, target_value=target_value, amount_value=amount_value)

        rate = rates[target_value]
        converted = amount * rate
        result = {
            'base': base_value,
            'target': target_value,
            'amount': amount,
            'rate': rate,
            'converted': converted
        }

    return render_template('index.html', result=result, currencies=CURRENCIES, base_value=base_value, target_value=target_value, amount_value=amount_value)

if __name__ == '__main__':
    # Use host=0.0.0.0 if you want to expose to other machines on your network
    app.run(debug=True)
