from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.detector import detect_platform
from app.services.downloader_service import process_download

router = APIRouter(prefix="/download", tags=["Downloader"])

class DownloadRequest(BaseModel):
    url: str

@router.post("/")
async def download_media(data: DownloadRequest):

    platform = detect_platform(data.url)

    if platform is None:
        return {"error": "Unsupported or invalid URL"}

    result = await process_download(platform, data.url)

    return {
        "platform": platform,
        "result": result
    }
