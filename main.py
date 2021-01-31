import queue
import threading
import cv2 as cv
import subprocess as sp


frame_queue = queue.Queue()
command = ""
# 自行设置
rtmpUrl = "rtmp://150.158.176.170:1935/live/test_10"
camera_path = "D://test.mkv"


def read_frame():
    print("开启推流")
    cap = cv.VideoCapture(camera_path)

    # Get video information
    fps = int(cap.get(cv.CAP_PROP_FPS))
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    # ffmpeg command
    command = ['ffmpeg',
                    '-y',
                    '-f', 'rawvideo',
                    '-vcodec', 'rawvideo',
                    '-pix_fmt', 'bgr24',
                    '-s', "{}x{}".format(width, height),
                    '-r', str(fps),
                    '-i', '-',
                    '-c:v', 'libx264',
                    '-pix_fmt', 'yuv420p',
                    '-preset', 'ultrafast',
                    '-f', 'flv',
                    rtmpUrl]

    # read webcamera
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            print("Opening camera is failed")
            # cap = cv.VideoCapture(camera_path)
            break

        # put frame into queue
        frame_queue.put(frame)


def push_frame():
    # 防止多线程时 command 未被设置
    while True:
        if len(command) > 0:
            # 管道配置
            p = sp.Popen(command, stdin=sp.PIPE)
            break

    while True:
        if frame_queue.empty() != True:
            frame = frame_queue.get()
            # process frame
            # 你处理图片的代码
            # write to pipe，。。
            p.stdin.write(frame.tostring())


def run():
    threads = [
        threading.Thread(target=read_frame, args=()),
        threading.Thread(target=push_frame, args=())
    ]
    [thread.setDaemon(True) for thread in threads]
    [thread.start() for thread in threads]