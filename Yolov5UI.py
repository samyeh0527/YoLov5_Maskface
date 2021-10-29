# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Yolov5.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1058, 803)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 40, 741, 721))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(900, 670, 91, 31))
        font = QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(860, 620, 83, 24))
        self.checkBox.setFont(font)
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(770, 620, 63, 24))
        self.checkBox_2.setFont(font)
        self.listWidget = QListWidget(self.centralwidget)
        font1 = QFont()
        font1.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font1);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font1);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setFont(font1);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(750, 40, 231, 61))
        self.listWidget.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(750, 10, 135, 27))
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 9, 81, 27))
        self.label_2.setFont(font2)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(750, 160, 231, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(750, 120, 135, 27))
        self.label_3.setFont(font2)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(750, 250, 83, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(750, 210, 135, 27))
        self.label_4.setFont(font2)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(750, 280, 83, 16))
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(750, 310, 83, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(750, 340, 291, 27))
        self.label_5.setFont(font2)
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(900, 370, 81, 31))
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(0.250000000000000)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(750, 420, 291, 27))
        self.label_6.setFont(font2)
        self.doubleSpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(900, 450, 81, 31))
        self.doubleSpinBox_2.setSingleStep(0.010000000000000)
        self.doubleSpinBox_2.setValue(0.060000000000000)
        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget.raise_()
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.radioButton.raise_()
        self.label_4.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.label_5.raise_()
        self.doubleSpinBox.raise_()
        self.label_6.raise_()
        self.doubleSpinBox_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1058, 21))
        self.menuYoLov5 = QMenu(self.menubar)
        self.menuYoLov5.setObjectName(u"menuYoLov5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuYoLov5.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8b66\u544a\u97f3", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad4\u6eab", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"yolov5s", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"yolov5x", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"yolov5l", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"yolov5m", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6a94\u9078\u64c7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8a0a\u606f\u7a97", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u7247\u4f86\u6e90", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"640x480", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u7247\u5c3a\u5bf8", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"1280\u00d7720", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"1080x1920", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ConfidenceThreshold", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Warning IOU", None))
        self.menuYoLov5.setTitle(QCoreApplication.translate("MainWindow", u"YoLov5", None))
    # retranslateUi

