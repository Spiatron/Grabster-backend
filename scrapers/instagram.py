from yt_dlp import YoutubeDL

def download_instagram(url: str):
    ydl_opts = {"format": "best", "quiet": True}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get("url")
            thumbnail = info.get("thumbnail")
            title = info.get("title", "Instagram Video")
            return {
                "status": "ok",
                "title": title,
                "download_url": video_url,
                "thumbnail": thumbnail
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
