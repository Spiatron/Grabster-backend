from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utils.detector import detect_platform
from scrapers.facebook import download_facebook
from scrapers.instagram import download_instagram

app = FastAPI()


# ---- CORS ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LinkRequest(BaseModel):
    url: str

@app.post("/download")
async def download(req: LinkRequest):
    url = req.url
    platform = detect_platform(url)

    if platform == "facebook":
        result = download_facebook(url)
    elif platform == "instagram":
        result = download_instagram(url)
    else:
        result = {
            "status": "error",
            "message": "Platform not supported yet"
        }

    return {
        "platform": platform,
        "result": result
    }
