import mymath
import unittest

class TestAdd(unittest.TestCase):
    """ 
    Test the additon function 
    """
    def add_integer(self):
        """ 
        Test the addition of two numbers 
        """
        result=mymath.add(1, 2)
        self.assertEqual(result,3)

    def add_float(self):
        """ Test the additon of float values """
        result=mymath.add(10.5,4.5)
        self.assertEqual(result,15)

    def add_string(self):
        """ Test the addtion of stirngs """
        result=mymath.add('abc','def')
        self.assertEqual(result,'abcdef')

if __name__=='__main__':
    unittest.main()
    
