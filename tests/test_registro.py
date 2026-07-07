import unittest
from models import Persona
from registry import RegistroPersonas
from tests.data_test import DATA_VALIDA, DATA_EDAD_NEGATIVA, DATA_DNI_DUPLICADO, DATA_VACIA

class TestRegistroPersonas(unittest.TestCase):
    
    def test_creacion_persona_valida(self):
        p = Persona('123', 'Test', 'Test', 20)
        self.assertEqual(p.dni, '123')
        self.assertEqual(p.edad, 20)

    def test_creacion_persona_edad_negativa(self):
        with self.assertRaises(ValueError):
            Persona('123', 'Test', 'Test', -1)

    def test_inmutabilidad_persona(self):
        p = Persona('123', 'Test', 'Test', 20)
        with self.assertRaises(Exception):
            p.edad = 21

    def test_cargar_datos_validos(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        self.assertEqual(len(r._personas), 2)
        self.assertIn('11111111', r._personas)

    def test_cargar_datos_duplicados(self):
        r = RegistroPersonas()
        with self.assertRaises(ValueError):
            r.cargar_datos(DATA_DNI_DUPLICADO)

    def test_formatear_registros(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        formateados = r.formatear_registros()
        self.assertEqual(formateados['11111111'], ('Pedro', 'Paez', 24))

    def test_obtener_mayor_edad(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        mayor = r.obtener_mayor_edad()
        self.assertEqual(mayor.edad, 30)

    def test_obtener_menor_edad(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        menor = r.obtener_menor_edad()
        self.assertEqual(menor.edad, 24)

    def test_promedio_edad(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        self.assertEqual(r.promedio_edad(), 27.0)

    def test_segmentar_por_edad(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        seg = r.segmentar_por_edad(25)
        self.assertEqual(len(seg['menor_igual']), 1)
        self.assertEqual(len(seg['mayor']), 1)

    def test_consultar_edad_existente(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        self.assertEqual(r.consultar_edad('11111111'), 24)

    def test_consultar_edad_inexistente(self):
        r = RegistroPersonas()
        r.cargar_datos(DATA_VALIDA)
        with self.assertRaises(KeyError):
            r.consultar_edad('99999999')

if __name__ == '__main__':
    unittest.main()
