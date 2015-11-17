from gopigo import *
import time
 STOP_DIST = 50


__author__ = 'ericulchaker'

class Pigo:

    ######
    ###### BASIC STATUS AND METHODS
    ######

    status = {'ismoving' : = False, 'servo' : 90, 'leftspeed' : 175}
    {'rightspeed' : 175}

    def __init__(self):
        print "I am very tired today."
        self.status['dist'] = us_dist(15)

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "I messed up :("

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            Print "This is not possible."
            for x in range(3):
                fwd()
    #Check if the conditions are safefor the pigo to continue
    def keepGoing(self):
        if self.status["dist"] < STOP_DIST
            print "Obstacle within stop distance"
        elif volt() > 14 or volt() < 6:
            Print "Voltage outside of safe range: " + str(volt())
            refurn False
        else:
            return True

    def checkDist(selfself):
        self.status["dist"] = us_dist(15)
        print "I see something " + str(self.status["dist"]) + "mm away"
    ######
    ###### COMPLEX METHODS
    ######

    ######
    ###### MAIN APP STARTS HERE
    ######

    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160):
            if ang % 3 == 0:
            servo(ang)
            time.sleep(.1)


    def dance(selfself):
        print "I just want to DANCE!"
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rturn()
        self.lturn()
        self.blink()



tina = Pigo()

while tina.keepGoing():
    tina.checkDist()
    tina.fwd()

    time.sleep(2)
    tina.stop()
