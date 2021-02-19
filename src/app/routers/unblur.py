from fastapi import APIRouter, File, UploadFile
from common import Injects
from services.unblur import UnblurService
from starlette.responses import StreamingResponse

import io

import numpy as np
from PIL import Image


router = APIRouter()

#@router.get("/api/unblur")
#async def root(unblur_service: UnblurService = Injects(ImagesService)):
#    return {"message": image_service.process()}
#
#
#@router.post("/api/files")
#async def create_file(file: bytes = File(...)):
#    return {"file_size": len(file)}


@router.post("/api/unblur/{file_name}")
async def unblur_file(file_name, file: UploadFile = File(...), unblur_service: UnblurService = Injects(UnblurService)):
    print(file)
    print(file_name)
    print(file.filename)
    file_data=await file.read()
    file_processed=unblur_service.process(io.BytesIO(file_data))
    bio = io.BytesIO()
    file_processed.save(bio,"JPEG")
    return StreamingResponse(io.BytesIO(bio.getbuffer()), media_type="image/jpeg")
