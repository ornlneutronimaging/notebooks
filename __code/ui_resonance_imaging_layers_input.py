# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/notebooks/ui/ui_resonance_imaging_layers_input.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(812, 722)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.example_table = QtGui.QTableWidget(self.groupBox)
        self.example_table.setEnabled(False)
        self.example_table.setMaximumSize(QtCore.QSize(16777215, 50))
        self.example_table.setObjectName(_fromUtf8("example_table"))
        self.example_table.setColumnCount(5)
        self.example_table.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.example_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.example_table.setItem(0, 4, item)
        self.example_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.example_table)
        self.layer_table = QtGui.QTableWidget(self.groupBox)
        self.layer_table.setEnabled(True)
        self.layer_table.setAlternatingRowColors(True)
        self.layer_table.setShowGrid(True)
        self.layer_table.setObjectName(_fromUtf8("layer_table"))
        self.layer_table.setColumnCount(5)
        self.layer_table.setRowCount(9)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.layer_table.setHorizontalHeaderItem(4, item)
        self.layer_table.horizontalHeader().setSortIndicatorShown(False)
        self.layer_table.horizontalHeader().setStretchLastSection(False)
        self.layer_table.verticalHeader().setVisible(False)
        self.layer_table.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.layer_table)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.validate_table_iinputs = QtGui.QPushButton(self.groupBox)
        self.validate_table_iinputs.setObjectName(_fromUtf8("validate_table_iinputs"))
        self.horizontalLayout.addWidget(self.validate_table_iinputs)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.check_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.check_groupBox.setEnabled(True)
        self.check_groupBox.setObjectName(_fromUtf8("check_groupBox"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.check_groupBox)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.check_groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.layer_name_combobox = QtGui.QComboBox(self.check_groupBox)
        self.layer_name_combobox.setObjectName(_fromUtf8("layer_name_combobox"))
        self.horizontalLayout_4.addWidget(self.layer_name_combobox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.check_groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.layer_thickness = QtGui.QLabel(self.check_groupBox)
        self.layer_thickness.setObjectName(_fromUtf8("layer_thickness"))
        self.gridLayout.addWidget(self.layer_thickness, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.check_groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.check_groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.layer_density = QtGui.QLabel(self.check_groupBox)
        self.layer_density.setObjectName(_fromUtf8("layer_density"))
        self.gridLayout.addWidget(self.layer_density, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.check_groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_11 = QtGui.QLabel(self.check_groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.element_name_combobox = QtGui.QComboBox(self.check_groupBox)
        self.element_name_combobox.setObjectName(_fromUtf8("element_name_combobox"))
        self.horizontalLayout_5.addWidget(self.element_name_combobox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_15 = QtGui.QLabel(self.check_groupBox)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.element_density = QtGui.QLabel(self.check_groupBox)
        self.element_density.setObjectName(_fromUtf8("element_density"))
        self.gridLayout_2.addWidget(self.element_density, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.check_groupBox)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 1, 2, 1, 1)
        self.label_18 = QtGui.QLabel(self.check_groupBox)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.element_molar_mass = QtGui.QLabel(self.check_groupBox)
        self.element_molar_mass.setObjectName(_fromUtf8("element_molar_mass"))
        self.gridLayout_2.addWidget(self.element_molar_mass, 2, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.check_groupBox)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 2, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.check_groupBox)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.element_number_of_atoms = QtGui.QLabel(self.check_groupBox)
        self.element_number_of_atoms.setObjectName(_fromUtf8("element_number_of_atoms"))
        self.gridLayout_2.addWidget(self.element_number_of_atoms, 0, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.check_groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.element_table = QtGui.QTableWidget(self.check_groupBox)
        self.element_table.setObjectName(_fromUtf8("element_table"))
        self.element_table.setColumnCount(4)
        self.element_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.element_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.element_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.element_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.element_table.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.element_table)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_3 = QtGui.QLabel(self.check_groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.total_iso_ratio = QtGui.QLabel(self.check_groupBox)
        self.total_iso_ratio.setObjectName(_fromUtf8("total_iso_ratio"))
        self.horizontalLayout_8.addWidget(self.total_iso_ratio)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.check_groupBox)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.cancel_button = QtGui.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_7.addWidget(self.cancel_button)
        spacerItem7 = QtGui.QSpacerItem(17, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.ok_button = QtGui.QPushButton(self.centralwidget)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_7.addWidget(self.ok_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.validate_table_iinputs, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.validate_table_input_clicked)
        QtCore.QObject.connect(self.layer_name_combobox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.layer_combobox_clicked)
        QtCore.QObject.connect(self.element_name_combobox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.element_combobox_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Layers", None))
        item = self.example_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.example_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.example_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Elements", None))
        item = self.example_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stoichio. Ratio", None))
        item = self.example_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thickness (mm)", None))
        item = self.example_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Density (g/cm3)", None))
        __sortingEnabled = self.example_table.isSortingEnabled()
        self.example_table.setSortingEnabled(False)
        item = self.example_table.item(0, 0)
        item.setText(_translate("MainWindow", "my_layer_1", None))
        item = self.example_table.item(0, 1)
        item.setText(_translate("MainWindow", "Co, Ag", None))
        item = self.example_table.item(0, 2)
        item.setText(_translate("MainWindow", "1,1", None))
        item = self.example_table.item(0, 3)
        item.setText(_translate("MainWindow", "20", None))
        item = self.example_table.item(0, 4)
        item.setText(_translate("MainWindow", "0.9", None))
        self.example_table.setSortingEnabled(__sortingEnabled)
        item = self.layer_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.layer_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.layer_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Elements", None))
        item = self.layer_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stoichio. Ratio", None))
        item = self.layer_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thickness (mm)", None))
        item = self.layer_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Density (g/cm3)", None))
        self.validate_table_iinputs.setText(_translate("MainWindow", "Validate Table Inputs", None))
        self.check_groupBox.setTitle(_translate("MainWindow", "Check", None))
        self.label.setText(_translate("MainWindow", "Layer\'s Name", None))
        self.label_2.setText(_translate("MainWindow", "Thickness", None))
        self.layer_thickness.setText(_translate("MainWindow", "N/A", None))
        self.label_4.setText(_translate("MainWindow", "mm", None))
        self.label_6.setText(_translate("MainWindow", "Density", None))
        self.layer_density.setText(_translate("MainWindow", "N/A", None))
        self.label_7.setText(_translate("MainWindow", "g/cm3", None))
        self.label_11.setText(_translate("MainWindow", "Element", None))
        self.label_15.setText(_translate("MainWindow", "Density", None))
        self.element_density.setText(_translate("MainWindow", "N/A", None))
        self.label_17.setText(_translate("MainWindow", "g/cm3", None))
        self.label_18.setText(_translate("MainWindow", "Molar Mass", None))
        self.element_molar_mass.setText(_translate("MainWindow", "N/A", None))
        self.label_20.setText(_translate("MainWindow", "g/mol", None))
        self.label_14.setText(_translate("MainWindow", "per cm3", None))
        self.element_number_of_atoms.setText(_translate("MainWindow", "N/A", None))
        self.label_12.setText(_translate("MainWindow", "Number of Atoms", None))
        item = self.element_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Isotopes", None))
        item = self.element_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Density (g/cm3)", None))
        item = self.element_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Iso. Ratio", None))
        item = self.element_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Molar Mass (g/mol)", None))
        self.label_3.setText(_translate("MainWindow", "Total Iso. Ratio:", None))
        self.total_iso_ratio.setText(_translate("MainWindow", "N/A", None))
        self.cancel_button.setText(_translate("MainWindow", "Cancel", None))
        self.ok_button.setText(_translate("MainWindow", "OK", None))

