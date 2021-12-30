from robomaster import version
from robomaster import robot
from robomaster import led
import time




if __name__ == "__main__":
    sdk_version = version.__version__
    print("sdk version:", sdk_version)

    ep_robot = robot.Robot()
    # 指定机器人的 SN 号
    ep_robot.initialize(conn_type="sta", proto_type="tcp", sn="3JKCH7T00100D0")

    ep_chassis = ep_robot.chassis

    x_val = 0.5
    y_val = 0.6
    z_val = 90

    # 前进 0.5米
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()

    # 后退 0.5米
    ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()

    # 左移 0.6米
    ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=0.7).wait_for_completed()

    # 右移 0.6米
    ep_chassis.move(x=0, y=y_val, z=0, xy_speed=0.7).wait_for_completed()

    # 左转 90度
    ep_chassis.move(x=0, y=0, z=z_val, z_speed=45).wait_for_completed()

    # 右转 90度
    ep_chassis.move(x=0, y=0, z=-z_val, z_speed=45).wait_for_completed()

    ep_robot.close()