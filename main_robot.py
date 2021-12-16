import time
import sys
sys.path.append('/home/pi/mlf/api')
from robot_control import RobotController

robot = RobotController

def goal_pose_object(X=213.3,Y=0,Z=229):
    robot.set_position_xyz(X,Y,Z)
    print("GOING TO POSITION")

def move_belt(direction):
    robot.move_belt(direction)
    print(f"RUNNING BELT on {direction} direction")

def turn_servo_eff(ang=0):
    robot.turn_servo(ang)
    print(f"TURNING SERVO TO {ang}")