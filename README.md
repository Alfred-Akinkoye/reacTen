# ReacTen

Project Overview

_reacTen_ is a modernized tennis simulation game that aims to help people keep fit and better their tennis skills. _reacTen_ offers an in-home method of learning and playing tennis. It consists of a system of devices that simulates the tennis experience where it is setup. Users can either play by themselves, in which they can adjust ball speed to their comfort level or play against online users within their skill sets. With a machine like _reacTen_, users can easily learn tennis in the comfort of their backyard or play a competitive match against a player in another vicinity or country, without worrying about travelling, or the current pandemic situation.

A player is composed of a ball shooter server and a target server, where each of these components are hosted by their own Raspberry Pi and manage their respective hardware devices. The processing of data, game logic, database, and GUI are managed by the server computer. The server computer communicates with the ball shooter server and target server through thingSpeak for all hardware servers. The simulated player implements the ball shooter server and target server as a simulator for each server and hosted by an individual Raspberry Pi. These simulators emulate the architecture of their real-life counterpart, in which their messages are randomized using weighted probabilities. The simulated player sends and receives information through thingSpeak, similarly to an actual player, which allows for the interaction with the live user. This simulated player in an eventual system to market would be replaced by the other players that also have hardware devices.

Player Ball Shooter Server Setup on Raspberry Pi 1:

The ball shooter server will automatically respond to messages from the game engine once it has been initialized. After initialization it also starts to send the status for the ball shooter (DC motor), the servo motor and proximity sensor (simulated).

Steps

1. Make sure that all hardware devices are connected as seen in Appendix D.
2. Make sure that the Raspberry pi can run python2.
3. Install the dependencies httplib, urllib, time, thread, requests, json, RPi.GPIO and numpy
  1. Note: these are all pre-installed in Raspbian.
4. Download from the github link the files ballShooter.py, ballShooterServer.py, servomotor.py and proximitySensorSimulator.py and save them in the same folder.
5. Open the command line and navigate to the same folder.
6. Start the ballShooterServer.py script by typing the command:

python2 ballShooterServer.py

1. The ball shooter is ready for games to start.

Target Simulator on Raspberry PI 2:

1. Download target\_simulator.py from github in the targetSimulator folder
2. Load Thonny on the raspberry pi
3. Run the target\_simulator.py

Server/UI Setup on Raspberry PI 3:

1. Download all files reacTenGUIfile folder and GameServer folder

1. Put files from both folders into 1 folder
2. Run GameEngine.py

Simulated Player Setup on Raspberry PI 4:

As stated earlier, the simulator adheres to the same functions as the ball shooter and target. To set up:

1. Download target\_simulator\_player2.py and ballShooterServerSimulator.py from github link in finalcodesubmission branch
2. Load both files onto the raspberry pi connected either wireless or to your monitor
