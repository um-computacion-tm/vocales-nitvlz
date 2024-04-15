import unittest

from vocales import contar_vocales


class TestContarVocales(unittest.TestCase):
    def test_vacio(self):
        resultado = contar_vocales('mmm')
        self.assertEqual(resultado, {})

    def test_solo_a(self):
        resultado = contar_vocales('mar')
        self.assertEqual(resultado, {'a': 1})

    def test_2_vocales(self):
        resultado = contar_vocales('marto')
        self.assertEqual(resultado, {'a': 1, 'o': 1})

    def test_3_vocales(self):
        resultado = contar_vocales('monitor')
        self.assertEqual(resultado, {'o': 2, 'i': 1})

    def test_4_vocales(self):
        resultado = contar_vocales('mecanico')
        self.assertEqual(resultado, {'e': 1, 'a': 1,'i': 1, 'o': 1})

    def test_5_vocales(self):
        resultado = contar_vocales('angurriento')
        self.assertEqual(resultado, {'a': 1, 'u': 1, 'i': 1, 'e': 1, 'o': 1})

    def test_mayusculas(self):
        resultado = contar_vocales('rEposItoriO')
        self.assertEqual(resultado,{'e': 1, 'o': 3, 'i': 2})




unittest.main()

