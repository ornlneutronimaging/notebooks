# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/notebooks/ui/ui_display_counts_of_region_vs_stack.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.file_index_ratio_button = QtWidgets.QRadioButton(self.groupBox)
        self.file_index_ratio_button.setChecked(True)
        self.file_index_ratio_button.setObjectName("file_index_ratio_button")
        self.horizontalLayout_8.addWidget(self.file_index_ratio_button)
        self.tof_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.tof_radio_button.setObjectName("tof_radio_button")
        self.horizontalLayout_8.addWidget(self.tof_radio_button)
        self.lambda_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.lambda_radio_button.setObjectName("lambda_radio_button")
        self.horizontalLayout_8.addWidget(self.lambda_radio_button)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.distance_source_detector_value = QtWidgets.QLineEdit(self.centralwidget)
        self.distance_source_detector_value.setMinimumSize(QtCore.QSize(80, 0))
        self.distance_source_detector_value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.distance_source_detector_value.setObjectName("distance_source_detector_value")
        self.horizontalLayout_2.addWidget(self.distance_source_detector_value)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.detector_offset_value = QtWidgets.QLineEdit(self.centralwidget)
        self.detector_offset_value.setMinimumSize(QtCore.QSize(80, 0))
        self.detector_offset_value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.detector_offset_value.setObjectName("detector_offset_value")
        self.horizontalLayout_2.addWidget(self.detector_offset_value)
        self.detector_offset_units = QtWidgets.QLabel(self.centralwidget)
        self.detector_offset_units.setObjectName("detector_offset_units")
        self.horizontalLayout_2.addWidget(self.detector_offset_units)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.time_spectra_file = QtWidgets.QLabel(self.centralwidget)
        self.time_spectra_file.setObjectName("time_spectra_file")
        self.horizontalLayout_3.addWidget(self.time_spectra_file)
        self.time_spectra_file_browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.time_spectra_file_browse_button.setMinimumSize(QtCore.QSize(100, 0))
        self.time_spectra_file_browse_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.time_spectra_file_browse_button.setObjectName("time_spectra_file_browse_button")
        self.horizontalLayout_3.addWidget(self.time_spectra_file_browse_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.done_button = QtWidgets.QPushButton(self.centralwidget)
        self.done_button.setObjectName("done_button")
        self.horizontalLayout.addWidget(self.done_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.done_button.clicked.connect(MainWindow.done_button_clicked)
        self.distance_source_detector_value.editingFinished.connect(MainWindow.distance_source_detector_validated)
        self.detector_offset_value.returnPressed.connect(MainWindow.detector_offset_validated)
        self.time_spectra_file_browse_button.clicked.connect(MainWindow.time_spectra_file_browse_button_clicked)
        self.file_index_ratio_button.clicked.connect(MainWindow.radio_button_clicked)
        self.tof_radio_button.clicked.connect(MainWindow.radio_button_clicked)
        self.lambda_radio_button.clicked.connect(MainWindow.radio_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Xaxis"))
        self.file_index_ratio_button.setText(_translate("MainWindow", "File Index"))
        self.tof_radio_button.setText(_translate("MainWindow", "TOF (us)"))
        self.lambda_radio_button.setText(_translate("MainWindow", "lambda (A)"))
        self.label.setText(_translate("MainWindow", "Distance Source-Detector"))
        self.label_2.setText(_translate("MainWindow", "m"))
        self.label_3.setText(_translate("MainWindow", "Detector Offset"))
        self.detector_offset_units.setText(_translate("MainWindow", "us"))
        self.label_5.setText(_translate("MainWindow", "Time Spectra File:"))
        self.time_spectra_file.setText(_translate("MainWindow", "N/A"))
        self.time_spectra_file_browse_button.setText(_translate("MainWindow", "Browse ..."))
        self.done_button.setText(_translate("MainWindow", "DONE"))

