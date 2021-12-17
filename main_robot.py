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
    robot.turn_servo_eff(ang)
    print(f"TURNING SERVO TO {ang}")

def grab_object(status=0):
    if status:
        robot.electro_status(1)
        print("ACTIVANDO GRIPPER")
    else:
        robot.electro_status(0)
        print("DESACTIVANDO GRIPPER")