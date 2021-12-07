from typing import List

from pydantic import BaseModel


class CreateWishListItem(BaseModel):
    user_id: int
    item_id: int
    item_type: str


class WishListItem(CreateWishListItem):
    id: int

    class Config:
        orm_mode = True


