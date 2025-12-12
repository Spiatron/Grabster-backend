# scrapers/instagram.py
import os
from yt_dlp import YoutubeDL

def download_instagram(url: str):
    """
    Download public Instagram Reels or posts using yt-dlp.
    Works only for public content.
    """
    try:
        ydl_opts = {
            "format": "mp4",
            "noplaylist": True,
            "quiet": True,
            "skip_download": True,  # Only get metadata + download URL
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        video_url = info.get("url")
        thumbnail = info.get("thumbnail")
        title = info.get("title", "Instagram Reel")

        if not video_url:
            return {"status": "error", "message": "Video not found or not public."}

        return {
            "status": "ok",
            "title": title,
            "download_url": video_url,
            "thumbnail": thumbnail,
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
