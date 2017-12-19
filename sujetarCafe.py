#!/usr/bin/env python
# -*- encoding: UTF-8 -*-



import qi
import argparse
import sys
import time
import math





def main(session):


    motion_service  = session.service("ALMotion")
   
    motion_service.setStiffnesses("LArm", 1.0)
    motion_service.setStiffnesses("RArm", 1.0)
    motion_service.setMoveArmsEnabled(False,False)  


    names  = ["LShoulderRoll","LHand","RShoulderRoll","RHand"] 
    angles  = [math.radians(22),1,math.radians(-22),1]
    fractionMaxSpeed  = 0.7
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(5)

    names  = ["LShoulderRoll","LHand","RShoulderRoll","RHand"] 
    angles  = [math.radians(19),1,math.radians(-19),1]
    fractionMaxSpeed  = 0.7
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(5)


    




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="172.18.33.122",
                        help="Robot IP address. On robot or Local Naoqi: use '172.18.33.122'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    

    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
