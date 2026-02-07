"""Language translator application using Deep Translator and Flask."""
from flask import Flask, render_template_string, request
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound, ServerException

app = Flask(__name__)

# HTML Template
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DataFlair Language Translator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .container { max-width: 800px; margin-top: 50px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">DataFlair Language Translator</h1>
        <div class="card p-4 shadow-sm">
            <form method="POST">
                <div class="mb-3">
                    <label for="language" class="form-label">Target Language</label>
                    <select class="form-select" id="language" name="language">
                        <option value="" disabled {% if not selected_lang %}selected{% endif %}>Choose a language</option>
                        {% for lang in languages %}
                            <option value="{{ lang }}" {% if lang == selected_lang %}selected{% endif %}>{{ lang }}</option>
                        {% endfor %}
                    </select>
                </div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label for="source_text" class="form-label">Source Text</label>
                        <textarea class="form-control" id="source_text" name="source_text" rows="6" placeholder="Enter text...">{{ source_text }}</textarea>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label for="translated_text" class="form-label">Translated Text</label>
                        <textarea class="form-control" id="translated_text" rows="6" readonly>{{ translated_text }}</textarea>
                    </div>
                </div>
                <div class="text-center">
                    <button type="submit" class="btn btn-warning btn-lg">Translate</button>
                </div>
            </form>
            {% if error %}
                <div class="alert alert-danger mt-3">{{ error }}</div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    translator = GoogleTranslator()
    languages_dict = translator.get_supported_languages(as_dict=True)
    languages = list(languages_dict.keys())

    selected_lang = None
    source_text = ""
    translated_text = ""
    error = None

    if request.method == 'POST':
        source_text = request.form.get('source_text', '').strip()
        selected_lang = request.form.get('language')

        if source_text and selected_lang:
            try:
                lang_code = languages_dict.get(selected_lang)
                if lang_code:
                    translator = GoogleTranslator(source='auto', target=lang_code)
                    translated_text = translator.translate(source_text)
                else:
                    error = "Selected language not found."
            except (TranslationNotFound, ServerException) as e:
                error = f"Translation failed: {str(e)}"
        elif not selected_lang:
            error = "Please select a target language."

    return render_template_string(TEMPLATE, languages=languages, selected_lang=selected_lang, source_text=source_text, translated_text=translated_text, error=error)

if __name__ == "__main__":
    app.run(debug=True)
