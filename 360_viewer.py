from PySide2.QtWidgets import QApplication
from ui_window_overload import *
import threading
from utils import *
from PySide2.QtCore import (Qt)
import numpy as np
import subprocess
import zmq

BIND_ADRESS ="tcp://localhost:5555"
CHANGE_YAW_CMD ="Parsed_v360_1 yaw"
CHANGE_PITCH_CMD="Parsed_v360_1 pitch"

class ZmqSender():
    def __init__(self, bind_address):
        context = zmq.Context()
        self.requester = context.socket(zmq.REQ)
        self.requester.connect(bind_address)

    def onecmd(self, cmd):
        if cmd == 'EOF':
            sys.exit(0)
        print('Sending command:[%s]' % cmd)
        self.requester.send_string(cmd)
        message = self.requester.recv()
        print('Received reply:[%s]' % message)


class viewWindow:
    def __init__(self):
        
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
            
        self.view_win = viewerWindow()

        self.view_win.bas.clicked.connect(lambda: self.moove_window("bas", self.view_win.bas))
        self.view_win.bas_droit.clicked.connect(lambda: self.moove_window("bas_droit", self.view_win.bas_droit))
        self.view_win.bas_gauche.clicked.connect(lambda: self.moove_window("bas_gauche", self.view_win.bas_gauche))
        self.view_win.haut.clicked.connect(lambda: self.moove_window("haut", self.view_win.haut))
        self.view_win.haut_droit.clicked.connect(lambda: self.moove_window("haut_droit", self.view_win.haut_droit))
        self.view_win.haut_gauche.clicked.connect(lambda: self.moove_window("haut_gauche", self.view_win.haut_gauche))
        self.view_win.droit.clicked.connect(lambda: self.moove_window("droit", self.view_win.droit))
        self.view_win.gauche.clicked.connect(lambda: self.moove_window("gauche", self.view_win.gauche))
        
        # connect its signal to the update_image slot
        thread = threading.Thread(target=self.run)
        thread.start()
        self.zmq = ZmqSender(BIND_ADRESS)
        self.view_win.setWindowTitle("HMI Retro updater ")
        self.view_win.show()
        self.view_win.setWindowState(Qt.WindowActive)
        self.app.exec_()
        #self.view_win.launchUpdateButton.clicked.connect(self.launch_update)


    def moove_window(self, dir, btn) -> None:
        print("ici")
        yaw = 0
        pitch=0
        if("haut" in dir):
            pitch+=5
        elif("bas" in dir):
            pitch-=5
        if("droit" in dir):
            yaw+=5
        elif("gauche" in dir):
            yaw-=5
        if(yaw != 0):
            self.zmq.onecmd(f"{CHANGE_YAW_CMD} {yaw}")
        if(pitch != 0):
            self.zmq.onecmd(f"{CHANGE_PITCH_CMD} {pitch}")
            
    def run(self):
        
        width = 736
        height = 368
        
        in_stream = 'rtsp://localhost:8554/mystream'
        
        command = ['ffmpeg', # Using absolute path for example (in Linux replacing 'C:/ffmpeg/bin/ffmpeg.exe' with 'ffmpeg' supposes to work).
                '-rtsp_transport', 'tcp',   # Force TCP (for testing)
                '-max_delay', '30000000',   # 30 seconds (sometimes needed because the stream is from the web).
                '-i', in_stream,
                '-f', 'rawvideo',
                '-filter_complex', '[0]zmq=[a],[a]v360=dfisheye:dfisheye:ih_fov=185:iv_fov=185:roll=90[b],[b]v360=dfisheye:rectilinear:yaw=0:pitch=0',
                '-pix_fmt', 'bgr24',        # bgr24 pixel format matches OpenCV default pixels format.
                '-an', 'pipe:']
        
        ffmpeg_process = subprocess.Popen(command, stdout=subprocess.PIPE)
        while True:
            # Read width*height*3 bytes from stdout (1 frame)
            raw_frame = ffmpeg_process.stdout.read(width*height*3)

            if len(raw_frame) != (width*height*3):
                print('Error reading frame!!!')  # Break the loop in case of an error (too few bytes were read).
                break

            frame = np.frombuffer(raw_frame, np.uint8).reshape((height, width, 3))
            self.view_win.update_img.emit(frame)

if __name__ == '__main__':
    viewWindow()
