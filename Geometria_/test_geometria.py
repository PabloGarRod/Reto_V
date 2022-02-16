from Geometria_.model.Geometria import Geometria
from Geometria_.view.View import View

import unittest


class Test_Geometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Vamos a  testear los metodos de Geometría: ")

    def setUp(self):
        print("Preparando el contexto...")
        self.ejemplo = Geometria(5.0, 10.0, 2.0)
        self.case = 7

    def test_Cuadrado(self):
        resultado = Geometria.areaCuadrado(self, self.ejemplo.a)
        self.assertEqual(resultado, 25)
        print("Realizando prueba test Cuadrado -> OK")
        unittest.skip("No ha pasado el test")

    def test_Circulo(self):
        resultado = Geometria.areaCirculo(self, self.ejemplo.a)
        self.assertEqual(resultado, 78.53999999999999)
        print("Realizando prubea test Circulo -> OK")

    def test_Triangulo(self):
        resultado = Geometria.areaTriangulo(self, self.ejemplo.a, self.ejemplo.b)
        self.assertEqual(resultado, 25)
        print("Realizando prubea test Triangulo -> OK")

    def test_Rectangulo(self):
        resultado = Geometria.areaRectangulo(self, self.ejemplo.a, self.ejemplo.b)
        self.assertEqual(resultado, 50)

    def test_Pentagono(self):
        resultado = Geometria.areaPentagono(self, self.ejemplo.a, self.ejemplo.b)
        self.assertEqual(resultado, 25)

    def test_Rombo(self):
        resultado = Geometria.areaRombo(self, self.ejemplo.a, self.ejemplo.b)
        self.assertEqual(resultado, 25)

    def test_Romboide(self):
        resultado = Geometria.areaRomboide(self, self.ejemplo.a, self.ejemplo.b)
        self.assertEqual(resultado, 50)

    def test_trapecio(self):
        resultado = Geometria.areaTrapecio(self, self.ejemplo.a, self.ejemplo.b, self.ejemplo.c)
        self.assertEqual(resultado, 15)

    def test_FiguraName(self):
        self.ejemplo.set_figuraName(self.case)
        resultado = self.ejemplo.figuraName
        self.assertEqual(resultado, "Romboide")

    def test_Switch(self):
        resultado = self.ejemplo.switch(self.case)
        self.assertEqual(resultado, 50)


    def tearDown(self):
        print("Destruyendo el contexto...")
        del self.ejemplo
        del self.case

    @classmethod
    def tearDownClass(cls):
        print("Testeo finalizado")




if __name__ == '__main__':
    unittest.main()

