# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
import time
from pathlib import Path
import cv2
import numpy
import torch.cuda
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import detect
from GUI import terminalWindow


class Ui_MainWindow(QMainWindow):
    progress = pyqtSignal(int)
    display_signal = pyqtSignal(str)

    # next_frame = pyqtSignal(numpy.ndarray)

    def __init__(self):
        super().__init__()
        self.path = 'TestImages/bus.jpg'
        self.savepath = 'runs'
        self.device = '0' if torch.cuda.is_available() else 'cpu'
        self.model = 'yolov5s.pt'
        self.setupUi(self)
        self.retranslateUi(self)
        self.terminal = terminalWindow.Ui_Dialog()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 22))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuDevice = QtWidgets.QMenu(self.menuSetting)
        self.menuDevice.setObjectName("menuDevice")
        self.menuModel = QtWidgets.QMenu(self.menuSetting)
        self.menuModel.setObjectName("menuModel")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_image = QtWidgets.QAction(MainWindow)
        self.actionOpen_image.setCheckable(False)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCPU = QtWidgets.QAction(MainWindow)
        self.actionCPU.setCheckable(True)
        self.actionCPU.setChecked(not torch.cuda.is_available())
        self.actionCPU.setObjectName("actionCPU")
        self.actionGPU = QtWidgets.QAction(MainWindow)
        self.actionGPU.setCheckable(True)
        self.actionGPU.setChecked(torch.cuda.is_available())
        self.actionGPU.setObjectName("actionGPU")
        self.actionOpen_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder.setObjectName("actionOpen_folder")
        self.actionOpen_video = QtWidgets.QAction(MainWindow)
        self.actionOpen_video.setObjectName("actionOpen_video")
        self.actionTerminal = QtWidgets.QAction(MainWindow)
        self.actionTerminal.setObjectName("actionTerminal")
        self.actionyolov5s = QtWidgets.QAction(MainWindow)
        self.actionyolov5s.setCheckable(True)
        self.actionyolov5s.setChecked(True)
        self.actionyolov5s.setObjectName("actionyolov5s")
        self.actionyolov5m = QtWidgets.QAction(MainWindow)
        self.actionyolov5m.setCheckable(True)
        self.actionyolov5m.setObjectName("actionyolov5m")
        self.actionyolov5l = QtWidgets.QAction(MainWindow)
        self.actionyolov5l.setCheckable(True)
        self.actionyolov5l.setObjectName("actionyolov5l")
        self.actionyolov5x = QtWidgets.QAction(MainWindow)
        self.actionyolov5x.setCheckable(True)
        self.actionyolov5x.setObjectName("actionyolov5x")
        self.actionSaving_Path = QtWidgets.QAction(MainWindow)
        self.actionSaving_Path.setObjectName("actionSaving_Path")
        self.menuMain.addAction(self.actionOpen_image)
        self.menuMain.addAction(self.actionOpen_video)
        self.menuMain.addAction(self.actionOpen_folder)
        self.menuMain.addAction(self.actionSave)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionExit)
        self.menuDevice.addAction(self.actionCPU)
        self.menuDevice.addAction(self.actionGPU)
        self.menuModel.addAction(self.actionyolov5s)
        self.menuModel.addAction(self.actionyolov5m)
        self.menuModel.addAction(self.actionyolov5l)
        self.menuModel.addAction(self.actionyolov5x)
        self.menuSetting.addAction(self.menuModel.menuAction())
        self.menuSetting.addAction(self.menuDevice.menuAction())
        self.menuSetting.addAction(self.actionSaving_Path)
        self.menuTools.addAction(self.actionTerminal)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionOpen_image.triggered.connect(self.open_img)
        self.actionOpen_video.triggered.connect(self.open_video)
        self.actionOpen_folder.triggered.connect(self.open_folder)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.change_save)
        self.actionCPU.triggered.connect(self.setCPU)
        self.actionGPU.triggered.connect(self.setGPU)
        self.actionyolov5s.triggered.connect(self.model_s)
        self.actionyolov5m.triggered.connect(self.model_m)
        self.actionyolov5l.triggered.connect(self.model_l)
        self.actionyolov5x.triggered.connect(self.model_x)
        self.terminal = terminalWindow.Ui_Dialog()
        self.actionTerminal.triggered.connect(self.show_terminal)
        self.pushButton_3.clicked.connect(self.open_result_folder)
        self.actionSaving_Path.triggered.connect(self.change_save)
        self.progress.connect(self.updateProgressBar)
        self.display_signal.connect(self.display)
        # self.terminal_signal.connect(self.terminal.add_line)
        # self.next_frame.connect(show_img)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Change saving path"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_3.setText(_translate("MainWindow", "Result"))
        self.menuMain.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuDevice.setTitle(_translate("MainWindow", "Device"))
        self.menuModel.setTitle(_translate("MainWindow", "Model"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))
        self.actionSave.setText(_translate("MainWindow", "Open webcam"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCPU.setText(_translate("MainWindow", "CPU"))
        self.actionGPU.setText(_translate("MainWindow", "GPU"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionOpen_video.setText(_translate("MainWindow", "Open video"))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal"))
        self.actionyolov5s.setText(_translate("MainWindow", "yolov5s"))
        self.actionyolov5m.setText(_translate("MainWindow", "yolov5m"))
        self.actionyolov5l.setText(_translate("MainWindow", "yolov5l"))
        self.actionyolov5x.setText(_translate("MainWindow", "yolov5x"))
        self.actionSaving_Path.setText(_translate("MainWindow", "Saving Path"))

    def updateProgressBar(self, val):
        self.progressBar.setValue(val)

    def open_img(self):
        self.img_thread = Open_img(self)
        self.img_thread.run()

    def open_video(self):
        self.video_thread = Open_video(self)
        self.video_thread.run()

    def open_folder(self):
        self.folder_thread = Open_folder(self)
        self.folder_thread.run()

    def display(self, path):
        if path.endswith(".jpg") or path.endswith(".png") or path.endswith(".jpeg"):
            img = cv2.imread(path)  # 读取图像
            show_img(img, self)
        # show video
        elif path.endswith(".mp4"):
            # self.video_play(path)
            capture = cv2.VideoCapture(path)
            if capture.isOpened():
                # while True:
                    ret, img = capture.read()
                    # if not ret:
                        # break
                    show_img(img, self)
                    # time.sleep(0.2)
            else:
                print('video open fail')
            # TODO: show each frame while running (optional)

    def change_save(self):
        self.save_thread = Change_save(self)
        self.save_thread.run()

    def run(self):
        self.run_thread = Run(self)
        self.run_thread.start()

    def setCPU(self):
        self.cpu_thread = Set_cpu(self)
        self.cpu_thread.run()

    def setGPU(self):
        self.gpu_thread = Set_gpu(self)
        self.gpu_thread.run()

    def model_s(self):
        self.s_thread = Model_s(self)
        self.s_thread.run()

    def model_m(self):
        self.m_thread = Model_m(self)
        self.m_thread.run()

    def model_l(self):
        self.l_thread = Model_l(self)
        self.l_thread.run()

    def model_x(self):
        self.x_thread = Model_x(self)
        self.x_thread.run()

    def show_terminal(self):
        # self.terminal_thread = Show_terminal()
        # self.terminal_thread.start()
        # self.terminal = terminalWindow.Ui_Dialog()
        self.terminal.show()
        # for i in range(1, 10):
        #     self.terminal.add_line(str(i))

    def open_result_folder(self):
        os.startfile(self.savepath)

    def video_play(self, path):
        self.video_play_thread = Video_play(self, path)
        self.video_play_thread.start()


class Run(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        # get save path
        p = Path(self.main_window.path)
        # run detect
        detect.run(window=self.main_window, source=self.main_window.path, weights=self.main_window.model,
                   device=self.main_window.device, project=self.main_window.savepath)
        if os.path.isdir(p):
            # show the first img or first frame of the first video in a directory
            first_file = os.listdir(self.main_window.path)[0]
            s = self.main_window.savepath + '/' + first_file
        else:
            s = self.main_window.savepath + '/' + p.name
        self.main_window.display_signal.emit(s)


class Open_img(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        file_name = QFileDialog.getOpenFileName(self.main_window, 'Choose file', './', 'image(*.jpg , *.png)')
        image_path = file_name[0]
        self.main_window.path = image_path
        self.main_window.display_signal.emit(self.main_window.path)


class Open_folder(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        p = QFileDialog.getExistingDirectory(self.main_window, 'Choose folder')
        # Check file type inside folder
        for files in os.listdir(p):
            if not files.endswith(".mp4") and not files.endswith(".jpg") and not files.endswith(".png"):
                # show error message and return
                s = "errorMessage/ERROR_1.jpg"
                self.main_window.display_signal.emit(s)
                return
        # show the first img or first frame of the first video inside the directory
        self.main_window.path = p
        first_file = os.listdir(self.main_window.path)[0]
        s = self.main_window.path + '/' + first_file
        self.main_window.display_signal.emit(s)


class Open_video(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        file_name = QFileDialog.getOpenFileName(self.main_window, 'Choose file', './', 'video(*.mp4)')
        self.main_window.path = file_name[0]
        print(self.main_window.path)
        # show the video
        self.main_window.display_signal.emit(self.main_window.path)


class Set_gpu(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.device = '0'
        self.main_window.actionCPU.setChecked(False)


class Set_cpu(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.device = 'cpu'
        self.main_window.actionGPU.setChecked(False)


class Model_s(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.model = 'yolov5s.pt'
        self.main_window.actionyolov5m.setChecked(False)
        self.main_window.actionyolov5l.setChecked(False)
        self.main_window.actionyolov5x.setChecked(False)


class Model_m(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.model = 'yolov5m.pt'
        self.main_window.actionyolov5s.setChecked(False)
        self.main_window.actionyolov5l.setChecked(False)
        self.main_window.actionyolov5x.setChecked(False)


class Model_l(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.model = 'yolov5l.pt'
        self.main_window.actionyolov5m.setChecked(False)
        self.main_window.actionyolov5s.setChecked(False)
        self.main_window.actionyolov5x.setChecked(False)


class Model_x(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.model = 'yolov5x.pt'
        self.main_window.actionyolov5m.setChecked(False)
        self.main_window.actionyolov5l.setChecked(False)
        self.main_window.actionyolov5s.setChecked(False)


class Show_terminal(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.terminal.show()
        time.sleep(100)


class Change_save(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.savepath = QFileDialog.getExistingDirectory(self.main_window, 'Choose save path')


class Video_play(QThread):
    def __init__(self, main_window, path):
        super().__init__()
        self.main_window = main_window
        self.path = path

    def run(self):
        capture = cv2.VideoCapture(self.path)
        if capture.isOpened():
            while True:
                ret, img = capture.read()
                if not ret:
                    break
                self.main_window.next_frame.emit(img)
                time.sleep(0.1)


def show_img(img, window):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
    x = img.shape[1]  # 获取图像大小
    y = img.shape[0]
    ratio = x / y
    window_x = window.graphicsView.width() - 10
    window_y = window.graphicsView.height() - 10
    if ratio * window_y <= window_x:
        x = int(ratio * window_y)
        y = window_y
    else:
        x = window_x
        y = int(window_x / ratio)
    img = cv2.resize(img, (x, y))
    frame = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
    pix = QPixmap.fromImage(frame)
    window.item = QGraphicsPixmapItem(pix)
    window.scene = QGraphicsScene()
    window.scene.addItem(window.item)
    window.graphicsView.setScene(window.scene)


def play_video(path):
    pass
