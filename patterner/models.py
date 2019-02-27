"""
models of different common body measurements and sizes
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class BodyModel:
    biceps_circumference: int = 0
    center_back_neck_to_waist: int = 0
    chest_circumference: int = 0
    head_circumference: int = 0
    hips_circumference: int = 0
    hips_to_upper_leg: int = 0
    natural_waist: int = 0
    natural_waist_to_hip: int = 0
    neck_circumference: int = 0
    shoulder_slope: int = 0
    shoulder_to_elbow: int = 0
    shoulder_to_shoulder: int = 0
    shoulder_to_wrist: int = 0
    upper_leg_circumference: int = 0
    wrist_circumference: int = 0


class FemaleBodyModel(BodyModel):
    """Includes extra parameters for suspiciously shapely individuals"""

    # TODO: actually include extra fields


man_size_34 = BodyModel(
    biceps_circumference=335,
    center_back_neck_to_waist=489,
    chest_circumference=849,
    head_circumference=570,
    hips_circumference=722,
    hips_to_upper_leg=183,
    natural_waist_to_hip=100,
    neck_circumference=366,
    shoulder_slope=43,
    shoulder_to_shoulder=419,
    shoulder_to_wrist=670,
    upper_leg_circumference=565,
    wrist_circumference=175,
)


man_size_36 = BodyModel(
    biceps_circumference=290,
    center_back_neck_to_waist=492,
    chest_circumference=907,
    head_circumference=575,
    hips_circumference=780,
    hips_to_upper_leg=193,
    natural_waist_to_hip=105,
    neck_circumference=378,
    shoulder_slope=46,
    shoulder_to_shoulder=431,
    shoulder_to_wrist=675,
    upper_leg_circumference=582,
    wrist_circumference=180,
)


man_size_38 = BodyModel(
    biceps_circumference=305,
    center_back_neck_to_waist=495,
    chest_circumference=965,
    head_circumference=580,
    hips_circumference=838,
    hips_to_upper_leg=202,
    natural_waist_to_hip=110,
    neck_circumference=391,
    shoulder_slope=49,
    shoulder_to_shoulder=444,
    shoulder_to_wrist=680,
    upper_leg_circumference=598,
    wrist_circumference=185,
)


man_size_40 = BodyModel(
    biceps_circumference=320,
    center_back_neck_to_waist=498,
    chest_circumference=1023,
    head_circumference=585,
    hips_circumference=896,
    hips_to_upper_leg=211,
    natural_waist_to_hip=115,
    neck_circumference=404,
    shoulder_slope=52,
    shoulder_to_shoulder=457,
    shoulder_to_wrist=685,
    upper_leg_circumference=614,
    wrist_circumference=190,
)


man_size_42 = BodyModel(
    biceps_circumference=335,
    center_back_neck_to_waist=501,
    chest_circumference=1081,
    head_circumference=590,
    hips_circumference=995,
    hips_to_upper_leg=220,
    natural_waist=925,
    natural_waist_to_hip=120,
    neck_circumference=416,
    shoulder_slope=55,
    shoulder_to_elbow=415,
    shoulder_to_shoulder=470,
    shoulder_to_wrist=690,
    upper_leg_circumference=630,
    wrist_circumference=195,
)


man_size_44 = BodyModel(
    biceps_circumference=350,
    center_back_neck_to_waist=505,
    chest_circumference=1139,
    head_circumference=595,
    hips_circumference=1012,
    hips_to_upper_leg=229,
    natural_waist_to_hip=125,
    neck_circumference=429,
    shoulder_slope=58,
    shoulder_to_shoulder=483,
    shoulder_to_wrist=700,
    upper_leg_circumference=646,
    wrist_circumference=200,
)
