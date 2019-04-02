
import unittest
import adn as f

class pruebas(unittest.TestCase):


    def test_obtener_complemento(self):
        self.assertEqual(f.obtener_complemento("A"),"T")
        self.assertEqual(f.obtener_complemento("G"),"C")
        self.assertEqual(f.obtener_complemento("T"),"A")
        self.assertEqual(f.obtener_complemento("C"),"G")
        self.assertRaises(Exception, f.obtener_complemento, 'r')
        self.assertRaises(Exception, f.obtener_complemento, '1')
        self.assertRaises(Exception, f.obtener_complemento, '-')


    def test_generar_cadena_complementaria(self):
        self.assertEqual(f.gernerar_cadena_complementaria("ATTTCG"),"TAAAGC")
        self.assertEqual(f.gernerar_cadena_complementaria("ATGC"),"TACG")
        self.assertEqual(Exception, f.generar_cadena_complementaria, 'CGTX1')


    def test_calcular_correspondencia(self):
        self.assertEqual(f.calcular_correspondencia('AGTC','GTCA'),100.0)
        self.assertEqual(f.calcular_correspondencia('GT','GC'),50.0)
        self.assertEqual(f.calcular_correspondencia('GCG','AAA'),0.0)


    def test_corresponden(self):
        self.assertEqual(f.corresponden("AGTA","TCAT"),True)
        self.assertEqual(f.corresponden("GCGA","CGCG"),False)
        self.assertEqual(f.corresponden("TAA","ATTCC"),False)

        
    def test_es_cadena_valida(self):
        self.assertEqual(f.es_cadena_valida("ATAT"),True)
        self.assertEqual(f.es_cadena_valida("CGTA"),True)
        self.assertEqual(f.es_cadena_valida("CZTa"),False)
        self.assertEqual(f.es_cadena_valida("123a"),False)


    def test_es_base(self):
    	self.assertEqual(f.es_base("A"),True)
    	self.assertEqual(f.es_base("X"),False)
    	self.assertEqual(f.es_base("C"),True)
    	self.assertEqual(f.es_base("D"),False)


    def test_es_subcadena(self):
        self.assertEqual(f.es_subcadena("TATA","TA"),True)
        self.assertEqual(f.es_subcadena("CGCG","GC"),True)
        self.assertEqual(f.es_subcadena("CaX0","-0"),False)
        self.assertEqual(f.es_subcadena("1-a","XX"),False)


    def test_reparar_dano(self):
    	self.assertEqual(reparar_dano())
        pass


    def test_obtener_secciones(self):
        self.assertEqual(f.obtener_secciones("TATACCCG",4),['TA', 'TA', 'CC', 'CG'])
        self.assertEqual(f.obtener_secciones("CCGTA",2),['CC', 'GTA'])
        self.assertEqual(f.obtener_secciones("TATATA",3),['TA', 'TA', 'TA'])
        self.assertEqual(f.obtener_secciones("CGAATAAAATTTGTC",5),['CGA', 'ATA', 'AAA', 'TTT', 'GTC'])


    def test_obtener_complementos(self):
        pass


    def test_unir_cadena(self):
        self.assertEqual(f.unir_cadena(['TA','CG']),"TACG")
        self.assertEqual(f.unir_cadena(['CA','GG']),"CAGG")
        self.assertEqual(f.unir_cadena(['TT','CG']),"TTCG")
        self.assertEqual(f.unir_cadena(['GG','TG']),"GGTG")

    def test_complementar_cadenas(self):
    	pass
        
