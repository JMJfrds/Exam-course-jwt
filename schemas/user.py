from pydantic import  BaseModel

class UserRequest(BaseModel):
    username : str
    email : str
    password : str
    is_active : bool
    is_admin : bool

class UpdateUserRequest(BaseModel):
    username : str
    email : str
    is_active : bool


class Token(BaseModel):
    access_token: str
    token_type: str
