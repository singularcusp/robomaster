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

    # 指定麦轮速度
    speed = 50
    slp = 1

    # 转动右前轮
    ep_chassis.drive_wheels(w1=speed, w2=0, w3=0, w4=0)
    time.sleep(slp)

    # 转动左前轮
    ep_chassis.drive_wheels(w1=0, w2=speed, w3=0, w4=0)
    time.sleep(slp)

    # 转动左后轮
    ep_chassis.drive_wheels(w1=0, w2=0, w3=speed, w4=0)
    time.sleep(slp)

    # 转动右后轮
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed)
    time.sleep(slp)

    # 前进 3秒
    ep_chassis.drive_wheels(w1=speed, w2=speed, w3=speed, w4=speed)
    time.sleep(slp)

    # 后退 3秒
    ep_chassis.drive_wheels(w1=-speed, w2=-speed, w3=-speed, w4=-speed)
    time.sleep(slp)

    # 左移 3秒
    ep_chassis.drive_wheels(w1=speed, w2=-speed, w3=speed, w4=-speed)
    time.sleep(slp)

    # 右移 3秒
    ep_chassis.drive_wheels(w1=-speed, w2=speed, w3=-speed, w4=speed)
    time.sleep(slp)

    # 左转 3秒
    ep_chassis.drive_wheels(w1=speed, w2=-speed, w3=-speed, w4=speed)
    time.sleep(slp)

    # 右转 3秒
    ep_chassis.drive_wheels(w1=-speed, w2=speed, w3=speed, w4=-speed)
    time.sleep(slp)

    # 停止麦轮运动
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)

    ep_robot.close()