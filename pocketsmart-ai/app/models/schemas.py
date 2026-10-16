from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: str
    password: str = Field(min_length=8, max_length=128)

    @field_validator('email')
    @classmethod
    def valid_email(cls, value):
        if '@' not in value or '.' not in value.rsplit('@', 1)[-1]:
            raise ValueError('Enter a valid email address')
        return value.lower().strip()

class LoginRequest(BaseModel):
    email: str
    password: str

class HomeRequest(BaseModel):
    budget: float = Field(gt=0, le=10_000_000)
    room_type: str = Field(min_length=2, max_length=50)
    style: str = Field(default='Modern', max_length=50)
    items: str = Field(default='lights, ceiling fan, table', max_length=500)
    notes: str = Field(default='', max_length=1000)

class PartyRequest(BaseModel):
    budget: float = Field(gt=0, le=10_000_000)
    guests: int = Field(gt=0, le=10000)
    event_type: str = Field(min_length=2, max_length=50)
    venue: str = Field(default='Any', max_length=100)
    food_preference: str = Field(default='Mixed', max_length=100)
    notes: str = Field(default='', max_length=1000)

class RecommendationItem(BaseModel):
    category: str
    title: str
    platform: str
    estimated_price: float
    reason: str
    link: str

class RecommendationResponse(BaseModel):
    planner: str
    budget: float
    summary: str
    allocations: dict
    recommendations: List[RecommendationItem]
    tips: List[str]
    demo_mode: bool = False

class JewelryText(BaseModel):
    budget: float = Field(gt=0, le=10_000_000)
    occasion: str = Field(min_length=2, max_length=80)
    style: str = Field(default='Elegant', max_length=80)
    metal: str = Field(default='Any', max_length=50)
    notes: str = Field(default='', max_length=1000)
