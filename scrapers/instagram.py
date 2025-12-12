import requests

def download_instagram(url: str):
    try:
        # Ensure URL ends with slash
        url = url.rstrip("/") + "/?__a=1&__d=dis"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Navigate JSON to get video info
        media = data.get("graphql", {}).get("shortcode_media", {})
        
        if not media.get("is_video", False):
            return {"status": "error", "message": "This post has no video."}
        
        video_url = media.get("video_url")
        title = media.get("owner", {}).get("username", "Instagram Video")
        thumbnail = media.get("display_url")
        
        return {
            "status": "ok",
            "title": title,
            "download_url": video_url,
            "thumbnail": thumbnail
        }
        
    except requests.HTTPError as e:
        return {"status": "error", "message": f"HTTP Error: {str(e)}"}
    except requests.RequestException as e:
        return {"status": "error", "message": f"Request Error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Example usage
url = "https://www.instagram.com/reel/XXXXXXXXX/"
result = download_instagram(url)
print(result)
