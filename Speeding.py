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
    y_val = 0.3
    z_val = 30

    # 前进 3秒
    ep_chassis.drive_speed(x=x_val, y=0, z=0, timeout=5)
    time.sleep(3)

    # 后退 3秒
    ep_chassis.drive_speed(x=-x_val, y=0, z=0, timeout=5)
    time.sleep(3)

    # 左移 3秒
    ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
    time.sleep(3)

    # 右移 3秒
    ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
    time.sleep(3)

    # 左转 3秒
    ep_chassis.drive_speed(x=0, y=0, z=-z_val, timeout=5)
    time.sleep(3)

    # 右转 3秒
    ep_chassis.drive_speed(x=0, y=0, z=z_val, timeout=5)
    time.sleep(3)

    # 停止麦轮运动
    ep_chassis.drive_speed(x=0, y=0, z=0, timeout=5)

    ep_robot.close()