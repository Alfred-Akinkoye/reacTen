"""ballShooterServer Test Suite"""
import unittest
import ballShooterServer as bss
import ballShooter as bl
from ballShooter import ballShooter as bltype

MAX_BALLS = 6
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
        
        self.assertEqual(server.status() , NOERROR,'Wrong initial status message returned')
        
    def test_shootBall(self):
        server = bss.ballShooterServer()
        
        self.assertTrue(server.shootBall(50),'Unsuccesful return values of True')
        self.assertEqual(server.ballsLeft,DEF_BALLS - 1,'Unsuccesful num balls update')
        
        server.ballsLeft = 0    #Simulate all balls were shot
        
        self.assertFalse(server.shootBall(50),'Unsuccesful return values of False')
        self.assertEqual(server.ballsLeft,0,'Unsuccesful num balls error handle')        
        
        
    def test_startGame(self):
        server = bss.ballShooterServer()
        
        self.assertTrue(server.startGame(20,40,3),'Unsuccesful return values of True')
        self.assertEqual(server.ballsLeft, 3 ,'Unsuccesful num balls update')
        
        self.assertTrue(server.startGame(20,40,7),'Unsuccesful return values of True')
        self.assertEqual(server.ballsLeft, MAX_BALLS ,'Unsuccesful num balls update')  
        
        self.assertFalse(server.startGame(20,40,-3),'Unsuccesful return values of True')
        self.assertEqual(server.ballsLeft, MAX_BALLS ,'Unsuccesful num balls error handle when startGame failed')           
        
        
    def test_finishGame(self):
        server = bss.ballShooterServer()
        
        self.assertTrue(server.finishGame(),'Unsuccesful return values of True')

        
if __name__ == '__main__':
    unittest.main()