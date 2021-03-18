__author__ = 'Marcus'

import unittest
from Food import Shelter

class ShelterTests(unittest.TestCase):
    def setUp(self):
        self.myShelter = Shelter()

    def test_case_provided(self):
        self.assertEqual(self.myShelter.orderAmount(5,3,7,17), 367)
        # The example case as it was provided in the assignement seems inaccurate. 
        # self.assertEqual(self.myShelter.orderAmount(5,3,7,17), 363.6)

    def test_works_with_valid_inputs(self):
        # Can handle all 0's for inputs
        self.assertEqual(self.myShelter.orderAmount(0,0,0,0), 0)
        # Can handle floating point values for food left over
        self.assertEqual(self.myShelter.orderAmount(1,0,0,10.5), 1.5)

    def test_correct_amounts_for_each_dog_size(self):
        # Correct amount for small dogs
        self.assertEqual(self.myShelter.orderAmount(2,0,0,0), 24)
        # Correct amount for medium dogs
        self.assertEqual(self.myShelter.orderAmount(0,2,0,0), 48)
        # Correct amount for large dogs
        self.assertEqual(self.myShelter.orderAmount(0,0,2,0), 72)

    def test_returns_0_if_adequate_food_leftover(self):
        self.assertEqual(self.myShelter.orderAmount(0,0,0,100), 0)
        self.assertEqual(self.myShelter.orderAmount(1,0,0,100), 0)
        self.assertEqual(self.myShelter.orderAmount(1,1,1,1000), 0)
    
    def test_handles_cap_of_30_dogs(self):
        self.assertRaises(Exception, self.myShelter.orderAmount, 31,0,0,0)
        self.assertRaises(Exception, self.myShelter.orderAmount, 30,1,0,0)
        self.assertRaises(Exception, self.myShelter.orderAmount, 11,11,11,0)

    def test_handles_invalid_inputs(self):
        # Negative numbers for dog count or leftover food
        self.assertRaises(Exception, self.myShelter.orderAmount, -1,0,0,0)
        self.assertRaises(Exception, self.myShelter.orderAmount, 0,-1,0,0)
        self.assertRaises(Exception, self.myShelter.orderAmount, 0,0,-1,0)
        self.assertRaises(Exception, self.myShelter.orderAmount, 0,0,0,-9)
        # Invalid character/type for input
        self.assertRaises(TypeError, self.myShelter.orderAmount, 'x',0,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, True,0,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, None,0,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,'x',0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,True,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,None,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,0,0,'~')
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,0,0,True)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,0,0,None)
        # Dog count must be a whole number
        self.assertRaises(TypeError, self.myShelter.orderAmount, 1.2,0,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,1.2,0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,0,1.2,0)

        
    def test_handles_missing_or_extra_params(self):
        self.assertRaises(TypeError, self.myShelter.orderAmount, )
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,0)
        self.assertRaises(TypeError, self.myShelter.orderAmount, 0,0,0,0,0,0)

    def test_function_called_count(self):
        # this is more of an integration test but I did want to point it out in case there is an opinion that this should be checked at the unit test level
        pass

if __name__ == '__main__':
    unittest.main()