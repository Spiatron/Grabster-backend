import instaloader

def download_instagram(url: str):
    L = instaloader.Instaloader(download_videos=False, download_comments=False, save_metadata=False)

    try:
        shortcode = url.rstrip("/").split("/")[-1]  # get the post/reel shortcode
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        # Only public content
        if not post.is_video and not post.video_url:
            return {"status": "error", "message": "This post has no video."}
        
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
        return {"status": "error", "message": str(e)}


# Example usage
url = "https://www.instagram.com/reel/XXXXXXXXX/"
result = download_instagram(url)
print(result)
