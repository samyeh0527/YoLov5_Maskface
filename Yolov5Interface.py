import sys 
import time
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QApplication, QGraphicsScene,QMainWindow
from PySide6.QtCore import *
from Yolov5UI import Ui_MainWindow
import simplify
import argparse
import sys
import time 
from pathlib import Path
from numpy import empty
import multiprocessing as mp
FILE = Path(__file__).absolute()
sys.path.append(FILE.parents[0].as_posix())  # add yolov5/ to path
from utils.general import check_requirements,colorstr
import argparse
import time
from Autoresize import *
#rtsp://admin:226988@192.168.8.149:554/live/profile.0


soundlock =False
temp_lock = noise_lock = False
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.itemSelectionChanged.connect(self.itemActivated_event)
        self.ui.pushButton.clicked.connect(self.show_all_info)
        self.weights = self.source = self.img_size = self.confidence_threshold = None
        self.temperature = self.noise = False
        self.noise = False
        self.noiseIOU = None
        self.graphicsView_ret_height = (self.ui.spinBox_4.value())- (self.ui.spinBox_2.value())
        self.graphicsView_ret_width = self.ui.spinBox_3.value()- self.ui.spinBox.value()
        self.ui.graphicsView.setScene(self.graphics())
        self.ui.spinBox.valueChanged.connect(self.spinbox_xy_valuechange)
        self.ui.spinBox_2.valueChanged.connect(self.spinbox_xy_valuechange)
        self.ui.spinBox_3.valueChanged.connect(self.spinbox_xy_valuechange)
        self.ui.spinBox_4.valueChanged.connect(self.spinbox_xy_valuechange)
    def spinbox_xy_valuechange(self):
        self.graphicsView_ret_height = (self.ui.spinBox_4.value())- (self.ui.spinBox_2.value())
        self.graphicsView_ret_width = self.ui.spinBox_3.value()- self.ui.spinBox.value()
        self.ui.graphicsView.setScene(self.graphics())
        #Graphics view 
    def graphics(self):
        scene = QGraphicsScene()
        pen = QPen(Qt.blue)
        origin = QPen(Qt.green)
        scene.addRect(QRectF ( 0 , 0,self.graphicsView_ret_width,self.graphicsView_ret_height),pen)
        
        return scene

    def itemActivated_event(self):
        try:
            for item in self.ui.listWidget.selectedItems():
                self.weights = item.text()
        except Exception as e:
            self.ui.textBrowser.append(e)

    def local__time(self):
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
        return result
    def radio_button(self):
        try:
            if self.ui.radioButton.isChecked() :
                self.img_size = 640
            if self.ui.radioButton_2.isChecked() :
                self.img_size = 1280
            if self.ui.radioButton_3.isChecked() :
                self.img_size = 1080
        except Exception as e:
            self.ui.textBrowser.append(e)
    def otherfuction(self):
        self.temperature = self.ui.checkBox_2.isChecked()
        self.noise = self.ui.checkBox.isChecked()
        
        
    def show_all_info(self):
        try:
            cpu_count = mp.cpu_count()
            self.ui.textBrowser.append(f'')
            self.source = self.ui.textEdit.toPlainText()
            self.confidence_threshold = self.ui.doubleSpinBox.value()
            self.noiseIOU = self.ui.doubleSpinBox_2.value()
            self.radio_button()
            self.otherfuction()
            self.ui.textBrowser.append(f'================YOLOV5 Information================')
            self.ui.textBrowser.append(f'{self.local__time()  } CPU 數量 : {cpu_count}')
            self.ui.textBrowser.append(f'{self.local__time()  } model pt : {self.weights} ')
            self.ui.textBrowser.append(f'{self.local__time()  } source  : {self.source} ')
            self.ui.textBrowser.append(f'{self.local__time()  } img_size  : {self.img_size}')
            self.ui.textBrowser.append(f'{self.local__time()  } confidence threshold  : {self.confidence_threshold}')
            self.ui.textBrowser.append(f'{self.local__time()  } other fuction  temperature : {self.temperature} noise : {self.noise}') 
            self.ui.textBrowser.append(f'{self.local__time()  } Noise IOU  : {self.noiseIOU}')     
                                        
            if self.temperature is True and self.noise is True:
                global temp_lock
                temp_lock = True
                global noise_lock
                noise_lock = True 

            elif self.temperature is True:
                temp_lock = True
                noise_lock = False 

            elif self.noise is True:
                temp_lock = False
                noise_lock = True
      
            opt = self.parse_opt()
            main(opt,temp_lock,noise_lock)
        except Exception as e :
            self.ui.textBrowser.append(f'{self.local__time()  } show_all_info error {e}')


        
    def parse_opt(self):
            parser = argparse.ArgumentParser()
            parser.add_argument('--weights', nargs='+', type=str, default='./'+self.weights+'.pt', help='model.pt path(s)')
            parser.add_argument('--source', type=str, default=self.source, help='file/dir/URL/glob, 0 for webcam')
            parser.add_argument('--imgsz', '--img', '--img-size', type=int, default=self.img_size, help='inference size (pixels)')
            parser.add_argument('--conf-thres', type=float, default=self.confidence_threshold, help='confidence threshold')
            parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
            parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
            parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
            parser.add_argument('--project', default='runs/detect', help='save results to project/name')
            parser.add_argument('--name', default='exp', help='save results to project/name')
            parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
            parser.add_argument('--noise',default=self.noiseIOU)
            parser.add_argument('--main_buffer_golab',default=main_buffer_golab)                
            parser.add_argument('--locks',default=locks)
            parser.add_argument('--sound_bools',default=sound_bools)
            opt = parser.parse_args()
            return opt




def main(opt,Temp_lock,noise_lock):
    #Temperature lock and noise is bool for process lock can use process.lock replace
    if Temp_lock and noise_lock is True: 
        process_1 = mp.Process(target=simplify.Daemon_buffer , args=(queue_,main_buffer_golab),daemon=True)
        process_2 = mp.Process(target=simplify.sound_deamon , args=(queue_,sound_bools,locks),daemon=True)
        #temperature
        process_1.start()
        #noise
        process_2.start()
        print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
        check_requirements(exclude=('tensorboard', 'thop'))
        simplify.run(**vars(opt))
        process_2.kill()
        process_1.kill()
        
    elif noise_lock is True: 
        process_2 = mp.Process(target=simplify.sound_deamon , args=(queue_,sound_bools,locks),daemon=True)
        process_2.start()
        print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
        check_requirements(exclude=('tensorboard', 'thop'))
        simplify.run(**vars(opt))
        process_2.kill()
    else:
        print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
        check_requirements(exclude=('tensorboard', 'thop'))
        simplify.run(**vars(opt))
    
if __name__ == "__main__":
    
    cpu_count = mp.cpu_count()
    manager = mp.Manager()
    queue_ = mp.Queue()  
    main_buffer_golab = manager.list()
    sound_bools = manager.list()
    locks = manager.Value('d',1)
    #Default Bools 
    sound_bools.append(False)  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec())
 