from enum import Enum


class UserRole(str, Enum):
    COACH = "Coach"
    MEMBER = "Member"
    GYM = "Gym"

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

