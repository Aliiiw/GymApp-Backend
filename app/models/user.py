from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.models.enums import UserRole, Gender


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    hashed_password: str
    role: UserRole
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)

    coach_profile: Optional["CoachProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False},
    )
    member_profile: Optional["MemberProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}
    )
    gym_profile: Optional["GymProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}
    )


class CoachProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id", unique=True, nullable=False)
    name: str
    last_name: str
    phone_number: str
    gender: Optional[Gender] = Field(default=None)
    national_code: Optional[str] = Field(default=None)
    bio: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None)
    user: User = Relationship(back_populates="coach_profile")


class MemberProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id", unique=True, nullable=False)
    name: str
    last_name: str
    phone_number: str
    height: Optional[float] = Field(default=None)
    weight: Optional[float] = Field(default=None)
    birth_date: Optional[str] = Field(default=None)
    gender: Optional[Gender] = Field(default=None)
    user: User = Relationship(back_populates="member_profile")


class GymProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True, nullable=False)
    gym_name: str = Field(nullable=False)
    address: Optional[str] = None
    phone_number: Optional[str] = None
    description: Optional[str] = None
    city: Optional[str] = None
    website: Optional[str] = None
    user: User = Relationship(back_populates="gym_profile")
