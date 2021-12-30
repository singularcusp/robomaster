from robomaster import version
from robomaster import robot
from robomaster import camera
import cv2
import time




if __name__ == "__main__":
    sdk_version = version.__version__
    print("sdk version:", sdk_version)

    ep_robot = robot.Robot()
    # 指定机器人的 SN 号
    ep_robot.initialize(conn_type="sta", proto_type="tcp", sn="3JKCH7T00100D0")

    ep_camera = ep_robot.camera
    print("ip ", ep_camera.video_stream_addr[0])
    print("port ", ep_camera.video_stream_addr[1])

    result = ep_camera.take_photo()

    # 显示十秒图传

    ep_camera.start_video_stream(display=False, resolution=camera.STREAM_360P)
    for i in range(0, 10):
        img = ep_camera.read_cv2_image(strategy="newest")
        cv2.imshow("Robot", img)
        cv2.waitKey(1)
        time.sleep(1)
    cv2.destroyAllWindows()
    time.sleep(10)
    ep_camera.stop_video_stream()

    ep_robot.close()

