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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGraphicsView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTextBrowser, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 803)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1051, 801))
        self.tabWidget.setMinimumSize(QSize(1051, 801))
        self.tabWidget.setMaximumSize(QSize(1051, 801))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 81, 27))
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 60, 741, 641))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(750, 20, 135, 27))
        self.label.setFont(font)
        self.radioButton_2 = QRadioButton(self.tab)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(750, 290, 101, 16))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(750, 220, 135, 27))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(750, 350, 291, 27))
        self.label_5.setFont(font)
        self.doubleSpinBox = QDoubleSpinBox(self.tab)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(900, 380, 81, 31))
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(0.250000000000000)
        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(770, 630, 63, 24))
        font1 = QFont()
        font1.setPointSize(15)
        self.checkBox_2.setFont(font1)
        self.listWidget = QListWidget(self.tab)
        font2 = QFont()
        font2.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font2);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font2);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font2);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setFont(font2);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(750, 50, 231, 61))
        self.listWidget.setFont(font2)
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(750, 170, 231, 31))
        self.radioButton_3 = QRadioButton(self.tab)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(750, 320, 101, 16))
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(860, 630, 83, 24))
        self.checkBox.setFont(font1)
        self.doubleSpinBox_2 = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(900, 470, 81, 31))
        self.doubleSpinBox_2.setSingleStep(0.010000000000000)
        self.doubleSpinBox_2.setValue(0.060000000000000)
        self.radioButton = QRadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(750, 260, 101, 16))
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(900, 680, 91, 31))
        self.pushButton.setFont(font1)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(750, 130, 135, 27))
        self.label_3.setFont(font)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(750, 430, 291, 41))
        self.label_6.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.graphicsView = QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 771, 721))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(950, 10, 91, 41))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(950, 90, 91, 41))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(840, 50, 16, 31))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(940, 50, 16, 31))
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(840, 130, 16, 31))
        self.label_22 = QLabel(self.tab_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(940, 130, 16, 31))
        self.spinBox = QSpinBox(self.tab_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(870, 60, 51, 21))
        self.spinBox.setMinimum(-1000)
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(-10)
        self.spinBox_2 = QSpinBox(self.tab_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(960, 60, 51, 21))
        self.spinBox_2.setMinimum(-1000)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setValue(10)
        self.spinBox_3 = QSpinBox(self.tab_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(870, 140, 51, 21))
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(1000)
        self.spinBox_3.setValue(10)
        self.spinBox_4 = QSpinBox(self.tab_2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(960, 140, 51, 21))
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(1000)
        self.spinBox_4.setValue(20)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8a0a\u606f\u7a97", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 |model \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0Speed(ms) \u00a0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 |YOLOv5s \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a098 \u00a0 \u00a0 \u00a0"
                        " \u00a0 </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 |YOLOv5m \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0224 \u00a0 \u00a0 \u00a0 \u00a0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 |YOLOv5l \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0430 \u00a0 \u00a0 \u00a0 </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 |YOLOv5x \u00a0 \u00a0"
                        " \u00a0 \u00a0 \u00a0 \u00a0766 \u00a0 \u00a0 \u00a0 \u00a0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 * from Yolov5 Github </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier N"
                        "ew','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 * follow \u00a0GPL-3.0 License</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 * Can input Video or youtube or RTSP or http</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 * Suggestion best video size is 640</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0"
                        " * Platform Ubuntu 20 and Windows 10</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 * Python version &gt;= 3.6</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 * If you have GPU should install 'Pytorch-GPU' \u00a0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#ce9178;\">\u00a0 \u00a0 \u00a0 \u00a0 \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594"
                        "\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6a94\u9078\u64c7", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"1280\u00d7720", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u7247\u5c3a\u5bf8", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ConfidenceThreshold", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad4\u6eab", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"yolov5s", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"yolov5m", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"yolov5l", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"yolov5x", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"1080x1920", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8b66\u544a\u97f3", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"640x480", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u7247\u4f86\u6e90", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Warning IOU", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u8a02\u5de6\u4e0b\u89d2\u5ea7\u6a19", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u8a02\u53f3\u4e0a\u89d2\u5ea7\u6a19", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

