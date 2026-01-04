"""Minimal Flask UI for the YouTube downloader."""
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from downloader import download_video

app = Flask(__name__)
app.secret_key = "change-me-in-production"
app.config["DOWNLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), "downloads")

os.makedirs(app.config["DOWNLOAD_FOLDER"], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url:
            flash("Please provide a YouTube URL.")
            return redirect(url_for("index"))

        result = download_video(url, app.config["DOWNLOAD_FOLDER"])
        if result["success"]:
            flash(f"Downloaded: {result['filename']}")
            return redirect(url_for("index"))
        else:
            flash(f"Error: {result['error']}")
            return redirect(url_for("index"))

    # list downloaded files
    files = sorted(os.listdir(app.config["DOWNLOAD_FOLDER"]))
    return render_template("index.html", files=files)


@app.route("/files/<path:filename>")
def files(filename):
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
