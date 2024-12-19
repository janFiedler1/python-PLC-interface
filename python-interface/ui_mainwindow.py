# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.controls_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controls_box.sizePolicy().hasHeightForWidth())
        self.controls_box.setSizePolicy(sizePolicy)
        self.controls_box.setMinimumSize(QtCore.QSize(300, 0))
        self.controls_box.setMaximumSize(QtCore.QSize(500, 16777215))
        self.controls_box.setStyleSheet("QGroupBox{border:0}")
        self.controls_box.setTitle("")
        self.controls_box.setObjectName("controls_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.controls_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.alarm_history_button = QtWidgets.QPushButton(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarm_history_button.sizePolicy().hasHeightForWidth())
        self.alarm_history_button.setSizePolicy(sizePolicy)
        self.alarm_history_button.setObjectName("alarm_history_button")
        self.gridLayout_3.addWidget(self.alarm_history_button, 3, 1, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setObjectName("login_button")
        self.gridLayout_3.addWidget(self.login_button, 4, 0, 1, 1)
        self.live_data_button = QtWidgets.QPushButton(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_data_button.sizePolicy().hasHeightForWidth())
        self.live_data_button.setSizePolicy(sizePolicy)
        self.live_data_button.setObjectName("live_data_button")
        self.gridLayout_3.addWidget(self.live_data_button, 2, 0, 1, 1)
        self.data_settings_button = QtWidgets.QPushButton(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_settings_button.sizePolicy().hasHeightForWidth())
        self.data_settings_button.setSizePolicy(sizePolicy)
        self.data_settings_button.setObjectName("data_settings_button")
        self.gridLayout_3.addWidget(self.data_settings_button, 3, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.controls_box)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_3.addWidget(self.dateTimeEdit, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)
        self.historical_data_button = QtWidgets.QPushButton(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historical_data_button.sizePolicy().hasHeightForWidth())
        self.historical_data_button.setSizePolicy(sizePolicy)
        self.historical_data_button.setObjectName("historical_data_button")
        self.gridLayout_3.addWidget(self.historical_data_button, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.controls_box)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_3.addWidget(self.dateTimeEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.controls_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.controls_box, 0, 2, 3, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("QGroupBox{border:0}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: red;")
        self.label_15.setLineWidth(0)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: red;")
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.graph_box = QtWidgets.QGroupBox(self.centralwidget)
        self.graph_box.setStyleSheet("border:0")
        self.graph_box.setTitle("")
        self.graph_box.setObjectName("graph_box")
        self.gridLayout = QtWidgets.QGridLayout(self.graph_box)
        self.gridLayout.setObjectName("gridLayout")
        self.empty_widget_1 = QtWidgets.QGraphicsView(self.graph_box)
        self.empty_widget_1.setObjectName("empty_widget_1")
        self.gridLayout.addWidget(self.empty_widget_1, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.graph_box, 1, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.alarm_history_button.setText(_translate("MainWindow", "Alarm History"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.live_data_button.setText(_translate("MainWindow", "Live Data"))
        self.data_settings_button.setText(_translate("MainWindow", "Alarms/Graphs"))
        self.label_10.setText(_translate("MainWindow", "End Date"))
        self.historical_data_button.setText(_translate("MainWindow", "Historical Data"))
        self.label_2.setText(_translate("MainWindow", "Start Date"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.label_13.setText(_translate("MainWindow", "Live Data"))
        self.label_15.setText(_translate("MainWindow", "Database: Disconnected"))
        self.label_14.setText(_translate("MainWindow", "PLC: Disconnected"))