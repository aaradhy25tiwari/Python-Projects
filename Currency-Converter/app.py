from flask import Flask, render_template, request, flash
import os
from dotenv import load_dotenv

load_dotenv()

# Import the existing conversion function from main.py
from main import convert_currency

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    rate = None
    if request.method == 'POST':
        base = request.form.get('base', '').strip().upper()
        target = request.form.get('target', '').strip().upper()
        amount_str = request.form.get('amount', '').strip()

        # Basic validation
        if not base or not target or not amount_str:
            flash('Please provide base currency, target currency and amount.', 'danger')
            return render_template('index.html', result=None)

        try:
            amount = float(amount_str)
        except ValueError:
            flash('Amount must be a number.', 'danger')
            return render_template('index.html', result=None)

        rates = convert_currency(base, target)
        if not rates:
            flash('Failed to fetch rates. Check your API key and network connection.', 'danger')
            return render_template('index.html', result=None)

        if target not in rates:
            flash(f'Currency {target} not found in API response.', 'warning')
            return render_template('index.html', result=None)

        rate = rates[target]
        converted = amount * rate
        result = {
            'base': base,
            'target': target,
            'amount': amount,
            'rate': rate,
            'converted': converted
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Use host=0.0.0.0 if you want to expose to other machines on your network
    app.run(debug=True)
