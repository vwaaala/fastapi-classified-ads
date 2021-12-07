from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from WishList import WishListSchema, WishListModel


def add_item_to_wishlist(item: WishListSchema.CreateWishListItem, db: Session):
    db_item = WishListModel.WishList(**item.dict())

    try:
        db.add(db_item)
        db.commit()
    except IntegrityError as err:
        db.rollback()

        if 'Duplicate entry' in str(err):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Item already added"
            )

    db.refresh(db_item)

    return db_item


def get_wishlist_items(user_id: int, db: Session):
    result = db.query(WishListModel.WishList).filter(WishListModel.WishList.user_id == user_id).all()

    return result


def delete_wish_list_item(wishlist_item_id: int, db: Session):
    db.query(WishListModel.WishList).filter_by(id=wishlist_item_id).delete()
    db.commit()
