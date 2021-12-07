from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from sqlalchemy.orm import Session


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != '_']


def validate_json_schema(data, schema_class):
    try:
        return schema_class.parse_obj(data)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=jsonable_encoder(e.errors())
        )


def get_schema_valiation_obejct(db: Session, model, filter_func):
    schema_object = {
        key: {
            'type': value.type_.__name__,
            'required': value.required
        } for key, value in model.__dict__['__fields__'].items()
    }

    options_attrs = filter_func(db, result_limit=30)
    for attr_name, attr_value in options_attrs.items():
        schema_object[attr_name]['type'] = 'option'
        schema_object[attr_name]['values'] = attr_value

    return schema_object
