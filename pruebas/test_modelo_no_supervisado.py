import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from modelo_no_supervisado import cargar_datos, agrupar_viajes, COLUMNAS

class PruebasModeloNoSupervisado(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datos = cargar_datos(ROOT / "datos" / "datos_transporte_no_supervisados.csv")

    def test_dataset_tiene_600_registros(self):
        self.assertEqual(len(self.datos), 600)

    def test_columnas_requeridas_presentes(self):
        self.assertTrue(set(COLUMNAS).issubset(self.datos.columns))

    def test_agrupamiento_crea_tres_grupos(self):
        resultado, modelo, scaler, centros, silueta = agrupar_viajes(self.datos, 3)
        self.assertEqual(resultado["grupo"].nunique(), 3)
        self.assertEqual(len(centros), 3)
        self.assertIsNotNone(silueta)

    def test_rechaza_columnas_faltantes(self):
        with self.assertRaises(ValueError):
            cargar_datos(ROOT / "pruebas" / "datos_invalidos.csv")

    def test_rechaza_numero_invalido_de_grupos(self):
        with self.assertRaises(ValueError):
            agrupar_viajes(self.datos, 1)

if __name__ == "__main__":
    unittest.main()
