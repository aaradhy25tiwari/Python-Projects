# Currency Converter (Python) 💱

A small utility to convert currencies using the Free Currency API. Includes a CLI helper (`main.py`) and a simple Flask web UI (`app.py`).

---

## ⚙️ Requirements

- Python 3.10+
- A Free Currency API key (get one at https://freecurrencyapi.com/)

---

## Repository Structure

```
Currency-Converter/
├── templates/
│   └── index.html
├── app.py              # Flask web UI
├── main.py             # CLI usage & conversion helper
├── requirements.txt
└── README.md
```

- `main.py` — conversion logic and small CLI demo
- `app.py` — Flask web interface that uses `main.convert_currency`
- `templates/index.html` — Bootstrap-based form and result view
- `requirements.txt` — List of modules required for the project
- `README.md` — This Document

---

## 🔧 Setup

1. Clone the repo and change directory:

```bash
git clone https://github.com/aaradhy25tiwari/Python-Projects.git
cd Python-Projects/Currency-Converter
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your API key:

```env
API_KEY="your_freecurrency_api_key"
# Optional: FLASK_SECRET for session flashing
FLASK_SECRET="a-secret-key"
```

---

## ▶️ Usage

### Web UI (recommended)

Start the Flask app:

```bash
python app.py
```

Open your browser at: http://127.0.0.1:5000

Enter base currency (e.g., `USD`), target (e.g., `EUR`) and an amount, then click Convert.

### CLI

You can also run the simple CLI in `main.py`:

```bash
python main.py
# Follow prompts: base currency, target currency, amount
```

Example interaction:

```
Enter base currency (e.g., USD): USD
Enter target currency (e.g., EUR): EUR
Enter amount to convert: 100
1 USD = 0.92 EUR
100 USD = 92.00 EUR
```

---

## Examples & Notes 💡

- The Flask UI shows the rate and converted amount and prints helpful flash messages for errors (missing fields, non-numeric amounts, or API issues).
- API responses may change; the code reads the `data` field from the Free Currency API and expects the API response to include the requested `target` currency key.

---

## ⚠️ Troubleshooting

- Missing API key error: ensure `.env` contains `API_KEY` and restart the app.
- Invalid API key / limit reached: check your Free Currency API dashboard and ensure your key is valid and within rate limits.
- Network errors: ensure your machine has internet access and the API endpoint is reachable.
- Flask app fails to start: check for errors printed to the console; ensure `Flask` is installed and that you activated the virtual environment if used.

---

## ✅ Testing & Quick Checks

- Syntax check: `python -m py_compile app.py main.py`
- Run linting or unit tests if you add them later.

---

## Contributing

Contributions are welcome — feel free to open issues or submit pull requests to:
- improve the UI
- add caching for API responses
- add automated tests

Please follow the usual fork → branch → PR workflow.

---

## License

This project is provided as-is. Add a license (e.g., MIT) if you want to allow reuse.

---

## Author

Created by aaradhy25tiwari. For questions or suggestions, open an issue in the repository.

## Happy Coding! 🖥️
