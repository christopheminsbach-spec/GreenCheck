from fastapi import APIRouter, UploadFile, File

from services.ai_recognition import recognize


router = APIRouter()


@router.post("/species")
async def identify_species(
    image: UploadFile = File(...)
):

    result = recognize(image)

    return result