import instaloader

def download_instagram(url: str, username=None, password=None):
    L = instaloader.Instaloader(download_videos=True, download_comments=False)
    
    # Optional: login for private/reels content
    if username and password:
        L.login(username, password)

    try:
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        video_url = post.video_url
        title = post.owner_username
        thumbnail = post.url
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

# Example usage
url = "https://www.instagram.com/reel/XXXXXXXXX/"
result = download_instagram(url)
print(result)
