from sqlalchemy import func, asc, desc, or_
from sqlalchemy.orm import Session

from database import Base


def get_unique_values(model: Base, db: Session, column, query=None, limit=5):
    if query:
        sub_query = db.query(model.id).filter_by(**query).subquery()
        result = db.query(
            column.label('val'),
            func.count(column).label('qty'),
        ).filter(model.id.in_(sub_query)).group_by(column).order_by(desc('qty')).limit(limit).all()

    else:
        result = db.query(
            column.label('val'),
            func.count(column).label('qty'),
        ).group_by(column).order_by(desc('qty')).limit(limit).all()

    return [row.val for row in result]


def get_all_items(db_model: Base, response_model, db: Session, page: int = 1, limit: int = 12, sort=None,
                  query=None):
    if query is None:
        query = {}
    if sort is None:
        sort = db_model.last_updated

    orm_query = db.query(db_model)

    if 'q' in query:
        orm_query = orm_query.filter(or_(db_model.id.like(f"%{query['q']}%"), db_model.title.like(f"%{query['q']}%")))
        del query['q']

    orm_query = orm_query.filter_by(**query)
    orm_query = orm_query.order_by(desc(sort), db_model.id.asc())
    results = orm_query.offset((page - 1) * limit).limit(limit).all()
    total = orm_query.count()

    # noinspection PyCallingNonCallable
    response = response_model(items=results, page=page, pages=int(total / limit) + 1, limit=limit)

    return response

def get_all_modified(db_model: Base, response_model, db: Session, page: int = 1, limit: int = 12, sort=None,
                  query=None, order=None):
    if query is None:
        query = {}
    if sort is None:
        sort = db_model.last_updated

    orm_query = db.query(db_model)

    if 'q' in query:
        orm_query = orm_query.filter(or_(db_model.id.like(f"%{query['q']}%"), db_model.title.like(f"%{query['q']}%")))
        del query['q']

    orm_query = orm_query.filter_by(**query)

    if order is not None:
        sortInfo = desc(sort) if order == "desc" else asc(sort)
    orm_query = orm_query.order_by(sortInfo)
    results = orm_query.offset((page - 1) * limit).limit(limit).all()
    total = orm_query.count()

    # noinspection PyCallingNonCallable
    response = response_model(items=results, page=page, pages=int(total / limit) + 1, limit=limit)

    return response