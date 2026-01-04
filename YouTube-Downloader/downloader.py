"""Download helper used by both the CLI and Flask UI."""
import os
from pytubefix import YouTube
from werkzeug.utils import secure_filename


def download_video(url, output_dir=None):
    """Download a YouTube video and save it into output_dir.

    Returns a dict with keys: success, filename (on success), path (on success), error (on failure).
    """
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), "downloads")

    os.makedirs(output_dir, exist_ok=True)

    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest = streams.get_highest_resolution()

        # Use a filesystem-safe filename
        filename = secure_filename(f"{yt.title}.mp4")
        target_path = highest.download(output_path=output_dir, filename=filename)

        return {"success": True, "filename": os.path.basename(target_path), "path": target_path}

    except Exception as e:
        return {"success": False, "error": str(e)}
