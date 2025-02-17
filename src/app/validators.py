from typing import Dict, Any
from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

def validate_user_input(data: Dict[str, Any]) -> Dict[str, Any]:
    schema = UserSchema()
    try:
        return schema.load(data)
    except ValidationError as err:
        raise ValueError(str(err.messages))