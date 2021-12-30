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

    ep_led = ep_robot.led
    # 设置灯效为常亮，亮度递增
    bright = 1
    for i in range(0, 8):
        ep_led.set_led(comp=led.COMP_BOTTOM_LEFT, r=(bright << i), g=(bright << i), b=(bright << i), effect=led.EFFECT_ON)
        time.sleep(1)
        print("brightness: {0}".format(bright << i))

    ep_robot.close()