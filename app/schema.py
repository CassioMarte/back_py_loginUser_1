from pydantic import BaseModel, EmailStr, field_validator
#from pydantic import BaseModel, EmailStr, validator
import re

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    
    @field_validator('password')   
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one capital letter')
        if not re.search(r'[0-9]', v):
             raise ValueError('Password must contain at least one number')
        return v
    
class UserResponse(UserBase):
    id:int
    is_active: bool
    
    class Config:
        orm_model = True
 