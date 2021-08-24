from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl


class Company(BaseModel):
    id: int
    name: str
    RFC: str
    country: str


class Metadata(BaseModel):
    first_name: str
    last_name: str
    company: Company
    contact_id: Optional[int]
    deal_id: Optional[int]


class UserProfile(BaseModel):
    sub: str
    nickname: str
    name: str
    picture: HttpUrl
    email: EmailStr
    email_verified: bool
    metadata: Metadata
