from PyQt5 import QtWidgets, QtCore, QtGui
from ui.m import Ui_MainWindow
import sys
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
import pandas as pd
import numpy as np

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class Window_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window_main, self, ).__init__()
        self.setupUi(self)
        self.show()
        
        self.listWidget.currentRowChanged['int'].connect(self.menu_list)

        self.initData()

    def initData(self):
        self.boot()
    
    def boot(self):
        self.btn_boot_file_selection.clicked.connect(self.Slot_boot_openfile)
        self.btn_boot_parse.clicked.connect(self.Slot_boot_parse_data)

    def cool_start(self):
        pass
    
    def Slot_boot_parse_data(self):
        if self.mode == "请选择模式":
            self.textEdit_show_boot_result.setText("请选择开机、关机、重启模式之一...")
        else:
            self.mode = self.comboBox_boot_mode_selection.currentText()
            self.android_version = self.comboBox_boot_android_version_selection.currentText()
            self.online_offline = self.comboBox_boot_online_offline_selection.currentText()

            self.textEdit_show_boot_result.append(self.mode + "\n" + self.android_version + "\n" + self.online_offline)

    def Slot_boot_openfile(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件','.')
        self.path_openfile_name = openfile_name[0]
        self.lineEdit_2.setText(self.path_openfile_name)
        self.textEdit_show_boot_result.append('选择的文件路径：' + self.path_openfile_name)

    # list变化的
    def menu_list(self, i):
        self.stackedWidget.setCurrentIndex(i)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window_main = Window_main()
    sys.exit(app.exec_())