"""Ball Shooter Software Test Suite"""
import unittest
import ballShooter as bl

PWMPIN = 12
PWMPERIOD = 1000

OFF = 0
LOWLIMIT = 0
HIGHLIMIT = 100
DEF_LOW = 40
DEF_HIGH = 100

class TestBallShooter(unittest.TestCase):
    
    def test_setSpeed(self):
        testBl = bl.ballShooter()
        self.assertTrue(testBl.setSpeed(10), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,10, 'Unsuccessfull speed change')
        
        self.assertTrue(testBl.setSpeed(20), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,20, 'Unsuccessfull speed change')  
        
        self.assertTrue(testBl.setSpeed(-20), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,LOWLIMIT, 'Unsuccessfull negative value handling')   
        
        self.assertTrue(testBl.setSpeed(120), 'Unsuccessful return')
        self.assertEqual(testBl.currSpeed,HIGHLIMIT, 'Unsuccessfull too large value handling')                
        
    def test_setLimits(self):
        testBl = bl.ballShooter()
        self.assertEqual(testBl.lowLimit,DEF_LOW, 'Unsuccessfull lowLimit initialization')
        self.assertEqual(testBl.highLimit,DEF_HIGH, 'Unsuccessfull highLimit initialization')        
        
        self.assertTrue(testBl.setLimits(10, 40), 'Unsuccessful return')
        self.assertEqual(testBl.lowLimit,10, 'Unsuccessfull lowLimit change')
        self.assertEqual(testBl.highLimit,40, 'Unsuccessfull highLimit change')
        
        self.assertTrue(testBl.setLimits(-10, 40), 'Unsuccessful return')
        self.assertEqual(testBl.lowLimit,LOWLIMIT, 'Unsuccessfull lowLimit change')
        self.assertEqual(testBl.highLimit,40, 'Unsuccessfull highLimit change')        
        
        self.assertFalse(testBl.setLimits(50, 30), 'Unsuccessful return for incompatible low and highlimit')
        self.assertEqual(testBl.lowLimit,LOWLIMIT, 'Unsuccessfull lowLimit handling for incompatible low and highlimit values')
        self.assertEqual(testBl.highLimit,40, 'Unsuccessfull lhighLimit handling for incompatible low and highlimit values')        
        
    def test_turnOff(self):
        testBl = bl.ballShooter()
        
        self.assertFalse(testBl.idle, 'Unsuccessfull iddle initialization to False')
        self.assertFalse(testBl.turnOff(), 'Unsuccessfull return')
        
        testBl.idle = True
        
        self.assertTrue(testBl.turnOff(), 'Unsuccessfull return')
        self.assertFalse(testBl.idle, 'Unsuccessfull idle update')
        
        
    def test_turnOn(self):
        testBl = bl.ballShooter()   
        
        self.assertTrue(testBl.turnOn(), 'Unsuccessfull return')
        self.assertTrue(testBl.idle, 'Unsuccessfull idle update')        
        
        self.assertFalse(testBl.turnOn(), 'Unsuccessfull return')
        self.assertTrue(testBl.idle, 'Unsuccessfull idle no change handling')        
        
        
        
        
        
        

if __name__ == '__main__':
    unittest.main()
    
