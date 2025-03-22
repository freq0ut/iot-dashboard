from pydantic import BaseModel, EmailStr
from typing import List, Optional


# ✅ User Schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


# ✅ Device Schemas
class DeviceCreate(BaseModel):
    name: str
    owner_id: int

class DeviceResponse(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True


# ✅ IoT Data Schema
class IoTData(BaseModel):
    device_id: str
    sensor_type: str
    value: float


# ✅ Token Response Schema
class Token(BaseModel):
    access_token: str
    token_type: str
