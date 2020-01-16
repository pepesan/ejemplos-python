from unittest import TestCase

from testunidad.clases.Clase import SelfDrivingCar


class SelfDrivingCarTest(TestCase):

    def setUp(self):
        self.car = SelfDrivingCar()

    def test_stop(self):
        self.car.speed = 5

        self.car.stop()

        # Verify the speed is 0 after stopping

        self.assertEqual(0, self.car.speed)

        # Verify it is Ok to stop again if the car is already stopped

        self.car.stop()

        self.assertEqual(0, self.car.speed)