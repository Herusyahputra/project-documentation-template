from Moildev import Moildev
import unittest
import json


class TestMoildev(unittest.TestCase):
    image = "../SourceImage/image.jpg"
    camera_parameter = 'camera_parameters/camera_parameters.json'
    camera_type = "Raspi"
    with open(camera_parameter) as f:
        data = json.load(f)
        if camera_type in data.keys():
            camera = data[camera_type]["cameraName"]
            sensor_width = data[camera_type]['cameraSensorWidth']
            sensor_height = data[camera_type]['cameraSensorHeight']
            Icx = data[camera_type]['iCx']
            Icy = data[camera_type]['iCy']
            ratio = data[camera_type]['ratio']
            imageWidth = data[camera_type]['imageWidth']
            imageHeight = data[camera_type]['imageHeight']
            calibrationRatio = data[camera_type]['calibrationRatio']
            parameter0 = data[camera_type]['parameter0']
            parameter1 = data[camera_type]['parameter1']
            parameter2 = data[camera_type]['parameter2']
            parameter3 = data[camera_type]['parameter3']
            parameter4 = data[camera_type]['parameter4']
            parameter5 = data[camera_type]['parameter5']

    moildev = Moildev(camera_parameter, camera_type)

    def test_test(self):
        self.moildev.test()
        self.assertTrue(True)

    def test_get_Icx(self):
        self.assertEqual(self.moildev.get_Icx(), self.Icx)

    def test_get_Icy(self):
        self.assertEqual(self.moildev.get_Icy(), self.Icy)

    def test_imageWidth(self):
        self.assertEqual(self.moildev.get_imageWidth(), self.imageWidth)

    def test_getAlphabeta(self):
        alpha, beta = self.moildev.get_alpha_beta(500,500, 2)
        self.assertTrue(alpha is not None)
