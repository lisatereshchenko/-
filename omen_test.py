from Omen import Calc, math
import unittest 
r = Calc()

class CalcTest(unittest.TestCase): 

    def test_start_value(self):
        result = r.total
        self.assertEqual(result, 0)

    def test_valid_function(self):
        self.total = 10
        self.current = 5
        result1 = (self.total-self.current)
        self.assertEqual(result1, (5))
    def test_divide(self):
        self.total = 100
        self.current = 5
        result2 = (self.total/self.current)
        self.assertEqual(result2, (20))

    def test_squared(self):
        self.current = 36
        result3= math.sqrt(self.current)
        self.assertEqual(result3, (6))
if __name__ == '__main__': 
    unittest.main()