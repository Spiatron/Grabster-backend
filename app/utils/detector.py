def detect_platform(url: str):
    url = url.lower()
    if "facebook.com" in url or "fb.watch" in url:
        return "facebook"
    if "instagram.com" in url:
        return "instagram"
    if "tiktok.com" in url:
        return "tiktok"
    if "x.com" in url or "twitter.com" in url:
        return "twitter"
    if "reddit.com" in url:
        return "reddit"
    return "unknown"
