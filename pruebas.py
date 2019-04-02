
import unittest
import adn as f

class pruebas(unittest.TestCase):


    def test_obtener_complemento(self):
        self.assertEqual(f.obtener_complemento("A"),"T")
        self.assertEqual(f.obtener_complemento("G"),"C")
        self.assertEqual(f.obtener_complemento("T"),"A")
        self.assertEqual(f.obtener_complemento("C"),"G")


    def test_generar_cadena_complementaria(self):
        pass


    def test_calcular_correspondencia(self):
        pass


    def test_corresponden(self):
        # retorna Bool
        pass


    def test_es_cadena_valida(self):
        pass


    def test_es_base(self):
        pass


    def test_es_subcadena(self):
        pass


    def test_reparar_dano(self):
        pass


    def test_obtener_secciones(self):
        pass


    def test_obtener_complementos(self):
        pass


    def test_unir_cadena(lista_adn):
        pass


    def test_complementar_cadenas(lista_adn):
        pass
