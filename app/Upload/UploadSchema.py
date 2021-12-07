# noinspection PyPackageRequirements
from pydantic import BaseModel


class UploadForm(BaseModel):
    site: str
    file: bytes
