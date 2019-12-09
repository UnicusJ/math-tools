import unittest
import binary_converter as bc
import euler_totient as et
import greatest_common_divisor as gd
import factors_of_num as fon
import lcm as l
import power_set as ps


class TestAlgoritm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    #test binary_convert.py
    def test_binary_convert(self):
        #test positiv 
        self.assertEqual(bc.binary_convert(16), '10000')
        self.assertEqual(bc.binary_convert(1), '1')
        self.assertEqual(bc.binary_convert(45), '101101')
        self.assertEqual(bc.binary_convert(0), '0')
         
        #test for errors
        with self.assertRaises(ValueError):
            #range values
            bc.binary_convert(1.5)
            #strings
            bc.binary_convert('Hello World')
            #negativ values
            bc.binary_convert(-1) 

    #test euler_totient.py
    def test_euler_totient(self):
        self.assertEqual(et.euler_totient(1), 1)
        self.assertEqual(et.euler_totient(2), 1)
        self.assertEqual(et.euler_totient(9), 6)
        self.assertEqual(et.euler_totient(457), 456)
        
        #test for errors
        #with self.assertRaises(ValueError):
        
    # test factor_of_num.py
    def test_factor_of_num(self):
        self.assertEqual(fon.factors(24), [1, 2, 3, 4, 6, 8, 12, 24])
        self.assertEqual(fon.factors(15), [1, 3, 5, 15])
        self.assertEqual(fon.factors(17), [1, 17])
        
        #test for errors
        #with self.assertRaises(ValueError):
        
    # test greatest_common_divisor.py
    def test_greatest_common_divisor(self):
        self.assertEqual(gd.gcd(10,5), 5)
        self.assertEqual(gd.gcd(10,3), 1)
        self.assertEqual(gd.gcd(10,0), 10)
        self.assertEqual(gd.gcd(5,10), 5)
        
        #test for errors
        #with self.assertRaises(ValueError):
        
    #test lcm.py
    def test_lcm(self):
        self.assertEqual(l.lcm([3,4,5]), 60)
        self.assertEqual(l.lcm([1,2,3,4,5,6,7,8,9,10]), 2520)
        self.assertEqual(l.lcm([1]), 'Please enter a list containing more than 1 number.')
        self.assertEqual(l.lcm([0,1]), 'The LCM of zero does not exist, please remove it from input list.')
        self.assertEqual(l.lcm([1,-2]), 2)
        
        #test for errors
        #with self.assertRaises(ValueError):
        
    #test power_set.py
    def test_power_set(self):
        self.assertEqual(ps.power_set([1,2,3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        self.assertEqual(ps.power_set([]), [[]])
        self.assertEqual(ps.power_set(['a']), [[], ['a']])
        
        #test for errors
        #with self.assertRaises(ValueError):
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
