import unittest
import calc

class Testcalc(unittest.TestCase):
    print("performing unittest")
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(12,-5),7)
        self.assertEqual(calc.add(-54, 5), -49)
        self.assertEqual(calc.add(-4,-5),-9)

    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(12,-5),17)
        self.assertEqual(calc.sub(-54, 5),-59)
        self.assertEqual(calc.sub(-4,-5),1)

    def test_mul(self):
        self.assertEqual(calc.mul(10,5),50)
        self.assertEqual(calc.mul(12,-5),-60)
        self.assertEqual(calc.mul(-54, 5),-270)
        self.assertEqual(calc.mul(-4,-5),20)

    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(12,-5),-2.4)
        self.assertEqual(calc.div(-54, 5),-10.8)
        self.assertEqual(calc.div(-4,-5),0.8)

if __name__=='__main__':
    unittest.main()
