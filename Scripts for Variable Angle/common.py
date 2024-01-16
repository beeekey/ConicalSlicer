from enum import Enum

class ConeType(str, Enum):
    INWARD = "inward"
    OUTWARD = 'outward'

class AngleCompensation(str, Enum):
    RADIAL = 'radial'
    TANGENTIAL= 'tangential'
    MIXED = 'mixed'