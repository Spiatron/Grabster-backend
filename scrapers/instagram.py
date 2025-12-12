import os
import tempfile
from yt_dlp import YoutubeDL
from dotenv import load_dotenv

# Read cookies content from environment variable (optional)
COOKIES_CONTENT = os.environ.get("INSTAGRAM_COOKIES")

def download_instagram(url: str):
    """
    Download Instagram video info using yt-dlp.
    Works with public posts without cookies.
    If COOKIES_CONTENT is set, it will use cookies for private posts.
    """
    ydl_opts = {
        "format": "best",
        "quiet": True,
        "noplaylist": True,
        "skip_download": True,  # only get URL
    }

    temp_cookie_file = None

    # If cookies are provided, create a temporary file
    if COOKIES_CONTENT:
        temp_cookie_file = tempfile.NamedTemporaryFile(delete=False)
        temp_cookie_file.write(COOKIES_CONTENT.encode())
        temp_cookie_file.flush()
        ydl_opts["cookiefile"] = temp_cookie_file.name

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get("url")
            title = info.get("title", "Instagram Video")
            thumbnail = info.get("thumbnail")
            return {
                "status": "ok",
                "title": title,
                "download_url": video_url,
                "thumbnail": thumbnail
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        # Clean up temp cookie file if created
        if temp_cookie_file:
            temp_cookie_file.close()
            os.unlink(temp_cookie_file.name)

