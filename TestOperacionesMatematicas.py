import unittest
import operaciones_matematicas as op

class TestOperacionesMatematicas(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(op.sumar(3, 2), 5)
        self.assertEqual(op.sumar(-1, 1), 0)
        self.assertEqual(op.sumar(0, 0), 0)
    
    def test_restar(self):
        self.assertEqual(op.restar(3, 2), 1)
        self.assertEqual(op.restar(-1, 1), -2)
        self.assertEqual(op.restar(0, 0), 0)
    
    def test_multiplicar(self):
        self.assertEqual(op.multiplicar(3, 2), 6)
        self.assertEqual(op.multiplicar(-1, 1), -1)
        self.assertEqual(op.multiplicar(0, 0), 0)
    
    def test_dividir(self):
        self.assertEqual(op.dividir(6, 2), 3)
        self.assertEqual(op.dividir(7, 3), 2.3333333333333335)
        self.assertIsNone(op.dividir(3, 0))  

if __name__ == '__main__':
    unittest.main()