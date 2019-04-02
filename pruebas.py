
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
        self.assertEqual(f.generar_cadena_complementaria("ATTTCG"),"TAAAGC")
        self.assertEqual(f.generar_cadena_complementaria("ATGC"),"TACG")
        self.assertRaises(Exception, f.generar_cadena_complementaria, 'CGTX1')


    def test_calcular_correspondencia(self):
        self.assertEqual(f.calcular_correspondencia('AGTC','GTCA'),0.0)
        self.assertEqual(f.calcular_correspondencia('GT','CT'),50.0)
        self.assertEqual(f.calcular_correspondencia('GCG','AAA'),0.0)
        self.assertRaises(Exception, f.calcular_correspondencia, 'S3TTT',"ATT3")


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
        self.assertEqual(reparar_dano('ATTTCVG','C'),"ATTTCCG")
        self.assertEqual(reparar_dano('XXX0TA','C'),"CCCCTA")
        self.assertEqual(reparar_dano('ATC1','G'),"ATCG")
        

    def test_obtener_secciones(self):
        self.assertEqual(f.obtener_secciones("TATACCCG",4),['TA', 'TA', 'CC', 'CG'])
        self.assertEqual(f.obtener_secciones("CCGTA",2),['CC', 'GTA'])
        self.assertEqual(f.obtener_secciones("TATATA",3),['TA', 'TA', 'TA'])
        self.assertEqual(f.obtener_secciones("CGAATAAAATTTGTC",5),['CGA', 'ATA', 'AAA', 'TTT', 'GTC'])


    def test_obtener_complementos(self):
        self.assertEqual(f.obtener_complementos(['ATT','AC','CCAG']),"TAA","GGTC","TG")
        self.assertEqual(f.obtener_complementos(['CG','ATT']),"CCAG","AC","ATT")
        self.assertEqual(Exception, f.obtener_complementos, 'TT','CC1')


    def test_unir_cadena(self):
        self.assertEqual(f.unir_cadena(['TA','CG']),"TACG")
        self.assertEqual(f.unir_cadena(['CA','GG']),"CAGG")
        self.assertEqual(f.unir_cadena(['TT','CG']),"TTCG")
        self.assertEqual(f.unir_cadena(['GG','TG']),"GGTG")

    def test_complementar_cadenas(self):
    	self.assertEqual(f.complementar_cadenas(['ATT','TTA']),"TAAAAT")
    	self.assertEqual(f.complementar_cadenas(['TA','CC','CT']),"GAATGG")
    	self.assertEqual(Exception, f.complementar_cadenas, '1CC')
    	self.assertEqual(Exception, f.complementar_cadenas, 'TATA')
    	self.assertEqual(Exception, f.complementar_cadenas, 'TA')
    	
        
