"""Unittest code"""
import unittest
import ballShooter as bl

class TestBallShooter(unittest.TestCase):
    
    def test_setSpeed(self):
        testBl = bl.ballShooter()
        self.assertTrue(testBl.setSpeed(10), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,10, 'Unsuccessfull speed change')
        self.assertTrue(testBl.setSpeed(20), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,20, 'Unsuccessfull speed change')  
        self.assertTrue(testBl.setSpeed(-20), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,0, 'Unsuccessfull negative value handling')   
        self.assertTrue(testBl.setSpeed(120), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,100, 'Unsuccessfull too large value handling')                
        
    
        

if __name__ == '__main__':
    unittest.main()
