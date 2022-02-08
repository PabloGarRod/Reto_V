from Geometria_.model.Geometria import Geometria
from Geometria_.view.View import View

import unittest


class Test_Geometria(unittest.TestCase):

    def test_Cuadrado(self):
        result = Geometria.areaCuadrado(self, 5)
        self.assertEqual(result, 25)
        print("Realizando prueba -> OK")


if __name__ == '__main__':
    unittest.main()
