"""ballShooterServer Test Suite"""
import unittest
import ballShooterServer as bss
import ballShooter as bl
from ballShooter import ballShooter as bltype


DEF_BALLS = 3
NOERROR = 0


class TestBallShooterServer(unittest.TestCase):
    
    def test_init(self):
        server = bss.ballShooterServer()
        
        self.assertEqual(server.ballsLeft, DEF_BALLS, 'Unsuccesful Default # balls initialization')
        self.assertEqual(server.statusMessage,NOERROR, 'Unsuccesful status initialization')
        self.assertTrue(isinstance(server.shooter,bltype), 'Unsuccesful ballShooter instanciation')
        
    
    def test_status(self):
        server = bss.ballShooterServer()
        
    def test_shootBall(self):
        server = bss.ballShooterServer()
        
        
        #self.assertTrue(testBl.setSpeed(10), 'Unsuccessful return')
        
    
    
    def test_startGame(self):
        server = bss.ballShooterServer()
        
        
    def test_finishGame(self):
        server = bss.ballShooterServer()

        
if __name__ == '__main__':
    unittest.main()