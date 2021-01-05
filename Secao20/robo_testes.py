import unittest
from Secao20.robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def tearDown(self):
        print('tearDown() sendo executado...')


if __name__ == "__main__":
    unittest.main()
