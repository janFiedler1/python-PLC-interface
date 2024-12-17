# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarms_graphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(656, 453)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.select_graph_profile_dropdown = QtWidgets.QComboBox(Dialog)
        self.select_graph_profile_dropdown.setObjectName("select_graph_profile_dropdown")
        self.select_graph_profile_dropdown.addItem("")
        self.verticalLayout_2.addWidget(self.select_graph_profile_dropdown)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        #self.scrollArea.setLayoutDirection(QtCore.Qt.Qt::LayoutDirection::LeftToRight)
        self.scrollArea.setStyleSheet("QScrollArea { border: 0; }")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignLeading|QtCore.Qt.Qt::AlignmentFlag::AlignLeft|QtCore.Qt.Qt::AlignmentFlag::AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 283))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph_settings_x = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_settings_x.sizePolicy().hasHeightForWidth())
        self.graph_settings_x.setSizePolicy(sizePolicy)
        self.graph_settings_x.setObjectName("graph_settings_x")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.graph_settings_x)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.graph_settings_x)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.graph_settings_x)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.graph_alarm_value_input = QtWidgets.QLineEdit(self.graph_settings_x)
        self.graph_alarm_value_input.setObjectName("graph_alarm_value_input")
        self.gridLayout_2.addWidget(self.graph_alarm_value_input, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.graph_settings_x)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.graph_settings_x)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.graph_settings_x)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.graph_settings_x)
        self.groupBox.setStyleSheet("QGroupBox {border:0}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_enable_toggle = QtWidgets.QPushButton(self.groupBox)
        self.graph_enable_toggle.setObjectName("graph_enable_toggle")
        self.horizontalLayout.addWidget(self.graph_enable_toggle)
        self.graph_remove_button = QtWidgets.QPushButton(self.groupBox)
        self.graph_remove_button.setObjectName("graph_remove_button")
        self.horizontalLayout.addWidget(self.graph_remove_button)
        self.gridLayout_2.addWidget(self.groupBox, 6, 0, 1, 3)
        self.graph_alarm_value_dropdown = QtWidgets.QComboBox(self.graph_settings_x)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_alarm_value_dropdown.sizePolicy().hasHeightForWidth())
        self.graph_alarm_value_dropdown.setSizePolicy(sizePolicy)
        self.graph_alarm_value_dropdown.setObjectName("graph_alarm_value_dropdown")
        self.graph_alarm_value_dropdown.addItem("")
        self.graph_alarm_value_dropdown.addItem("")
        self.gridLayout_2.addWidget(self.graph_alarm_value_dropdown, 5, 1, 1, 1)
        self.graph_y_max_input = QtWidgets.QLineEdit(self.graph_settings_x)
        self.graph_y_max_input.setObjectName("graph_y_max_input")
        self.gridLayout_2.addWidget(self.graph_y_max_input, 3, 1, 1, 2)
        self.graph_y_min_input = QtWidgets.QLineEdit(self.graph_settings_x)
        self.graph_y_min_input.setObjectName("graph_y_min_input")
        self.gridLayout_2.addWidget(self.graph_y_min_input, 2, 1, 1, 2)
        self.graph_tag_input = QtWidgets.QLineEdit(self.graph_settings_x)
        self.graph_tag_input.setObjectName("graph_tag_input")
        self.gridLayout_2.addWidget(self.graph_tag_input, 1, 1, 1, 2)
        self.graph_name_input = QtWidgets.QLineEdit(self.graph_settings_x)
        self.graph_name_input.setObjectName("graph_name_input")
        self.gridLayout_2.addWidget(self.graph_name_input, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.graph_settings_x)
        self.add_new_graph_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add_new_graph_button.setObjectName("add_new_graph_button")
        self.verticalLayout.addWidget(self.add_new_graph_button)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(353, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancel_graph_modal_button = QtWidgets.QPushButton(self.groupBox_2)
        self.cancel_graph_modal_button.setObjectName("cancel_graph_modal_button")
        self.horizontalLayout_3.addWidget(self.cancel_graph_modal_button)
        self.save_graph_modal_button = QtWidgets.QPushButton(self.groupBox_2)
        self.save_graph_modal_button.setObjectName("save_graph_modal_button")
        self.horizontalLayout_3.addWidget(self.save_graph_modal_button)
        self.save_exit_graph_modal_button = QtWidgets.QPushButton(self.groupBox_2)
        self.save_exit_graph_modal_button.setObjectName("save_exit_graph_modal_button")
        self.horizontalLayout_3.addWidget(self.save_exit_graph_modal_button)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.select_graph_profile_dropdown.setItemText(0, _translate("Dialog", "Select Profile..."))
        self.graph_settings_x.setTitle(_translate("Dialog", "Graph 1"))
        self.label_3.setText(_translate("Dialog", "y Range Minimum"))
        self.label_4.setText(_translate("Dialog", "y Range Maximum"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_6.setText(_translate("Dialog", "Alarm"))
        self.label_2.setText(_translate("Dialog", "Tag"))
        self.graph_enable_toggle.setText(_translate("Dialog", "Disable"))
        self.graph_remove_button.setText(_translate("Dialog", "Remove"))
        self.graph_alarm_value_dropdown.setItemText(0, _translate("Dialog", "Is Less Than"))
        self.graph_alarm_value_dropdown.setItemText(1, _translate("Dialog", "Is More Than"))
        self.add_new_graph_button.setText(_translate("Dialog", "+ Add New"))
        self.cancel_graph_modal_button.setText(_translate("Dialog", "Cancel"))
        self.save_graph_modal_button.setText(_translate("Dialog", "Save"))
        self.save_exit_graph_modal_button.setText(_translate("Dialog", "Save and Exit"))
