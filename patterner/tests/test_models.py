import unittest

from patterner import models


class TestModels(unittest.TestCase):
    def test_dataclass_params(self):
        params = models.BodyModel.__dataclass_params__
        self.assertTrue(params.frozen)
        self.assertTrue(params.init)
        self.assertTrue(params.repr)
        self.assertTrue(params.eq)
        self.assertFalse(params.order)
        self.assertFalse(params.unsafe_hash)

    def test_body_model_attibutes_defaults(self):
        model = models.BodyModel()
        self.assertEqual(model.biceps_circumference, 0)
        self.assertEqual(model.center_back_neck_to_waist, 0)
        self.assertEqual(model.chest_circumference, 0)
        self.assertEqual(model.head_circumference, 0)
        self.assertEqual(model.hips_circumference, 0)
        self.assertEqual(model.hips_to_upper_leg, 0)
        self.assertEqual(model.natural_waist, 0)
        self.assertEqual(model.natural_waist_to_hip, 0)
        self.assertEqual(model.neck_circumference, 0)
        self.assertEqual(model.shoulder_slope, 0)
        self.assertEqual(model.shoulder_to_elbow, 0)
        self.assertEqual(model.shoulder_to_shoulder, 0)
        self.assertEqual(model.shoulder_to_wrist, 0)
        self.assertEqual(model.upper_leg_circumference, 0)
        self.assertEqual(model.wrist_circumference, 0)

    def test_man_size_34(self):
        model = models.man_size_34
        self.assertEqual(model.biceps_circumference, 335)
        self.assertEqual(model.center_back_neck_to_waist, 489)
        self.assertEqual(model.chest_circumference, 849)
        self.assertEqual(model.head_circumference, 570)
        self.assertEqual(model.hips_circumference, 722)
        self.assertEqual(model.hips_to_upper_leg, 183)
        self.assertEqual(model.natural_waist_to_hip, 100)
        self.assertEqual(model.neck_circumference, 366)
        self.assertEqual(model.shoulder_slope, 43)
        self.assertEqual(model.shoulder_to_shoulder, 419)
        self.assertEqual(model.shoulder_to_wrist, 670)
        self.assertEqual(model.upper_leg_circumference, 565)
        self.assertEqual(model.wrist_circumference, 175)

    def test_man_size_36(self):
        model = models.man_size_36
        self.assertEqual(model.biceps_circumference, 290)
        self.assertEqual(model.center_back_neck_to_waist, 492)
        self.assertEqual(model.chest_circumference, 907)
        self.assertEqual(model.head_circumference, 575)
        self.assertEqual(model.hips_circumference, 780)
        self.assertEqual(model.hips_to_upper_leg, 193)
        self.assertEqual(model.natural_waist_to_hip, 105)
        self.assertEqual(model.neck_circumference, 378)
        self.assertEqual(model.shoulder_slope, 46)
        self.assertEqual(model.shoulder_to_shoulder, 431)
        self.assertEqual(model.shoulder_to_wrist, 675)
        self.assertEqual(model.upper_leg_circumference, 582)
        self.assertEqual(model.wrist_circumference, 180)

    def test_man_size_38(self):
        model = models.man_size_38
        self.assertEqual(model.biceps_circumference, 305)
        self.assertEqual(model.center_back_neck_to_waist, 495)
        self.assertEqual(model.chest_circumference, 965)
        self.assertEqual(model.head_circumference, 580)
        self.assertEqual(model.hips_circumference, 838)
        self.assertEqual(model.hips_to_upper_leg, 202)
        self.assertEqual(model.natural_waist_to_hip, 110)
        self.assertEqual(model.neck_circumference, 391)
        self.assertEqual(model.shoulder_slope, 49)
        self.assertEqual(model.shoulder_to_shoulder, 444)
        self.assertEqual(model.shoulder_to_wrist, 680)
        self.assertEqual(model.upper_leg_circumference, 598)
        self.assertEqual(model.wrist_circumference, 185)

    def test_man_size_40(self):
        model = models.man_size_40
        self.assertEqual(model.biceps_circumference, 320)
        self.assertEqual(model.center_back_neck_to_waist, 498)
        self.assertEqual(model.chest_circumference, 1023)
        self.assertEqual(model.head_circumference, 585)
        self.assertEqual(model.hips_circumference, 896)
        self.assertEqual(model.hips_to_upper_leg, 211)
        self.assertEqual(model.natural_waist_to_hip, 115)
        self.assertEqual(model.neck_circumference, 404)
        self.assertEqual(model.shoulder_slope, 52)
        self.assertEqual(model.shoulder_to_shoulder, 457)
        self.assertEqual(model.shoulder_to_wrist, 685)
        self.assertEqual(model.upper_leg_circumference, 614)
        self.assertEqual(model.wrist_circumference, 190)

    def test_man_size_42(self):
        model = models.man_size_42
        self.assertEqual(model.biceps_circumference, 335)
        self.assertEqual(model.center_back_neck_to_waist, 501)
        self.assertEqual(model.chest_circumference, 1081)
        self.assertEqual(model.head_circumference, 590)
        self.assertEqual(model.hips_circumference, 995)
        self.assertEqual(model.hips_to_upper_leg, 220)
        self.assertEqual(model.natural_waist, 925)
        self.assertEqual(model.natural_waist_to_hip, 120)
        self.assertEqual(model.neck_circumference, 416)
        self.assertEqual(model.shoulder_slope, 55)
        self.assertEqual(model.shoulder_to_elbow, 415)
        self.assertEqual(model.shoulder_to_shoulder, 470)
        self.assertEqual(model.shoulder_to_wrist, 690)
        self.assertEqual(model.upper_leg_circumference, 630)
        self.assertEqual(model.wrist_circumference, 195)

    def test_man_size_44(self):
        model = models.man_size_44
        self.assertEqual(model.biceps_circumference, 350)
        self.assertEqual(model.center_back_neck_to_waist, 505)
        self.assertEqual(model.chest_circumference, 1139)
        self.assertEqual(model.head_circumference, 595)
        self.assertEqual(model.hips_circumference, 1012)
        self.assertEqual(model.hips_to_upper_leg, 229)
        self.assertEqual(model.natural_waist_to_hip, 125)
        self.assertEqual(model.neck_circumference, 429)
        self.assertEqual(model.shoulder_slope, 58)
        self.assertEqual(model.shoulder_to_shoulder, 483)
        self.assertEqual(model.shoulder_to_wrist, 700)
        self.assertEqual(model.upper_leg_circumference, 646)
        self.assertEqual(model.wrist_circumference, 200)
