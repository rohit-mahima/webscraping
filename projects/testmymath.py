import mymath
import unittest

class TestAdd(unittest.TestCase):
    """ 
    Test the additon function 
    """
    def test_add_integer(self):# it is importatnt to write test
        """ 
        Test the addition of two numbers 
        """
        result=mymath.add(1, 2)
        self.assertEqual(result,3)

    def test_add_float(self):
        """ Test the additon of float values """
        result=mymath.add(10.5,4.5)
        self.assertEqual(result,15)

    def test_add_string(self):
        """ Test the addtion of stirngs """
        result=mymath.add('abc','def')
        self.assertEqual(result,'abcdef')

if __name__=='__main__':
    unittest.main()
    
