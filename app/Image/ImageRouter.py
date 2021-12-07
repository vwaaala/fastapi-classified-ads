from fastapi import APIRouter

from Image import ImageService

router = APIRouter(
    prefix="/images",
    tags=["images"],
)


@router.get("/image_data/{image_name}", response_model=bytes)
async def get_image_data(image_name: str):
    return ImageService.get_image(image_name)
