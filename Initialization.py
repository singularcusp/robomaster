import robomaster
from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    # 指定机器人的 SN 号
    # sta: 组网wifi, ap: 直接wifi, rndis: usb
    # tcp: 可靠, udp: 不可靠
    ep_robot.initialize(conn_type="sta", proto_type="tcp", sn="3JKCH7T00100D0")
    # ep_robot.initialize(conn_type='rndis')

    print("Robot Version: {0}".format(ep_robot.get_version()))
    print("Robot SN: ", ep_robot.get_sn())
    print("Robot ip: ", ep_robot.ip)
    print("Robot conn_type: ", ep_robot.conn_type)
    print("Robot proto_type: ", ep_robot.proto_type)
    print("Robot audio_stream_addr: ", ep_robot.conf.audio_stream_addr)
    print("Robot audio_stream_port: ", ep_robot.conf.audio_stream_port)
    print("Robot video_stream_addr: ", ep_robot.conf.video_stream_addr)
    print("Robot video_stream_port: ", ep_robot.conf.video_stream_port)
    print("Robot mode: ", ep_robot.get_robot_mode())

    ep_robot.close()