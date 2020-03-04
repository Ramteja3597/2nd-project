import calc2
a=5
b=4
c=calc2.mod(a,b)
d=calc2.hw()
e=calc2.evenodd(a)
f=calc2.fact(a)
print(c)
print(d)
print(e)
print(f)

import unittest
class Testcalc(unittest.TestCase):
    print("performing unittest")
    def test_mod(self):
        self.assertEqual(calc2.mod(10,5),0)
    def test_evenodd(self):
        self.assertEqual(calc2.evenodd(10),"even")
    def test_fact(self):
        self.assertEqual(calc2.fact(5),120)

if __name__=='__main__':
    unittest.main()

