from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from WishList import WishListSchema, WishListService
from database import get_db

router = APIRouter(
    prefix="/wishlist",
    tags=["Wish List"],
)


@router.get("/{user_id}", response_model=List[WishListSchema.WishListItem])
def get_items(user_id: int, db: Session = Depends(get_db)):
    return WishListService.get_wishlist_items(user_id, db)


@router.post("/", response_model=WishListSchema.WishListItem)
def add_item(item: WishListSchema.CreateWishListItem, db: Session = Depends(get_db)):
    return WishListService.add_item_to_wishlist(item, db)


@router.delete("/{wishlist_item_id}")
def get_machinery(wishlist_item_id: int, db: Session = Depends(get_db)):
    return WishListService.delete_wish_list_item(wishlist_item_id, db)
