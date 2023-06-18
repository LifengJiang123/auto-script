# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1375, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_left_menu = QtWidgets.QWidget(self.centralwidget)
        self.widget_left_menu.setStyleSheet("QPushButton {\n"
"    padding: 4px;\n"
"    font: 10pt \"微软雅黑\";\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 224, 0%);\n"
"    text-align:left\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}\n"
" \n"
"QPushButton:pressed {\n"
"    background-color: #333;\n"
"    border-color: #555;\n"
"    color: #AAA;\n"
"}\n"
" \n"
"QPushButton:disabled {\n"
"    color: #333333;\n"
"}")
        self.widget_left_menu.setObjectName("widget_left_menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_left_menu)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_left_menu = QtWidgets.QPushButton(self.widget_left_menu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu_img/img/left_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/menu_img/img/menu_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_left_menu.setIcon(icon)
        self.btn_left_menu.setObjectName("btn_left_menu")
        self.verticalLayout_6.addWidget(self.btn_left_menu)
        self.line = QtWidgets.QFrame(self.widget_left_menu)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.listWidget = QtWidgets.QListWidget(self.widget_left_menu)
        self.listWidget.setStyleSheet("QListView {\n"
"    outline:none;\n"
"    show-decoration-selected: 1;\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 224, 0%);\n"
"}\n"
"\n"
"#listWidget::item {\n"
"    color: #000000;\n"
"    border: transparent;\n"
"    border-bottom: 1px solid #dbdbdb;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"\n"
"#listWidget::item:hover {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"#listWidget::item:selected {\n"
"    border-left: 3px solid #777777;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu_img/img/home_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu_img/img/boot_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu_img/img/coldstart_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu_img/img/mem_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/menu_img/img/checklist_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/menu_img/img/cmd_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/menu_img/img/tool_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.listWidget.addItem(item)
        self.verticalLayout_6.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.widget_left_menu)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.stackedWidget.addWidget(self.page_home)
        self.page_boot = QtWidgets.QWidget()
        self.page_boot.setStyleSheet("QPushButton {\n"
"    border: 1px solid #555;\n"
"    padding: 4px;\n"
"    font: 10pt \"微软雅黑\";\n"
"\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"    background-color: #999;\n"
"}\n"
" \n"
"QPushButton:pressed {\n"
"    background-color: #333;\n"
"    border-color: #555;\n"
"    color: #AAA;\n"
"}\n"
" \n"
"QPushButton:disabled {\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QTextEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"/*\n"
"QComboBox {\n"
"    background-color: #AAA;\n"
"    border: 1px solid #555;\n"
"    color: black;\n"
"}\n"
"*/\n"
"/*\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-left: 1px solid #333333;\n"
"}\n"
"*/\n"
"\n"
"\n"
"QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"#label_page1{\n"
"    border: 1px solid gray;\n"
"}\n"
"")
        self.page_boot.setObjectName("page_boot")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_boot)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.page_boot)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_boot_mode_selection = QtWidgets.QComboBox(self.page_boot)
        self.comboBox_boot_mode_selection.setObjectName("comboBox_boot_mode_selection")
        self.comboBox_boot_mode_selection.addItem("")
        self.comboBox_boot_mode_selection.addItem("")
        self.comboBox_boot_mode_selection.addItem("")
        self.verticalLayout.addWidget(self.comboBox_boot_mode_selection)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.page_boot)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_boot_android_version_selection = QtWidgets.QComboBox(self.page_boot)
        self.comboBox_boot_android_version_selection.setObjectName("comboBox_boot_android_version_selection")
        self.comboBox_boot_android_version_selection.addItem("")
        self.comboBox_boot_android_version_selection.addItem("")
        self.comboBox_boot_android_version_selection.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_boot_android_version_selection)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.page_boot)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.comboBox_boot_online_offline_selection = QtWidgets.QComboBox(self.page_boot)
        self.comboBox_boot_online_offline_selection.setObjectName("comboBox_boot_online_offline_selection")
        self.comboBox_boot_online_offline_selection.addItem("")
        self.comboBox_boot_online_offline_selection.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_boot_online_offline_selection)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_boot)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.btn_boot_file_selection = QtWidgets.QPushButton(self.page_boot)
        self.btn_boot_file_selection.setObjectName("btn_boot_file_selection")
        self.horizontalLayout_3.addWidget(self.btn_boot_file_selection)
        self.btn_boot_parse = QtWidgets.QPushButton(self.page_boot)
        self.btn_boot_parse.setObjectName("btn_boot_parse")
        self.horizontalLayout_3.addWidget(self.btn_boot_parse)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.textEdit_show_boot_result = QtWidgets.QTextEdit(self.page_boot)
        self.textEdit_show_boot_result.setObjectName("textEdit_show_boot_result")
        self.verticalLayout_5.addWidget(self.textEdit_show_boot_result)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 7)
        self.stackedWidget.addWidget(self.page_boot)
        self.page_coldstart = QtWidgets.QWidget()
        self.page_coldstart.setStyleSheet("QCheckBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"#label_coldstart_output{\n"
"    border: 1px solid gray;\n"
"}")
        self.page_coldstart.setObjectName("page_coldstart")
        self.btn_coldstart_test = QtWidgets.QPushButton(self.page_coldstart)
        self.btn_coldstart_test.setGeometry(QtCore.QRect(230, 20, 171, 31))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/menu_img/img/file_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_coldstart_test.setIcon(icon8)
        self.btn_coldstart_test.setObjectName("btn_coldstart_test")
        self.btn_coldstart_compared = QtWidgets.QPushButton(self.page_coldstart)
        self.btn_coldstart_compared.setGeometry(QtCore.QRect(230, 70, 171, 31))
        self.btn_coldstart_compared.setIcon(icon8)
        self.btn_coldstart_compared.setObjectName("btn_coldstart_compared")
        self.lineEdit_coldstart_test = QtWidgets.QLineEdit(self.page_coldstart)
        self.lineEdit_coldstart_test.setGeometry(QtCore.QRect(20, 20, 191, 31))
        self.lineEdit_coldstart_test.setObjectName("lineEdit_coldstart_test")
        self.lineEdit_coldstart_compared = QtWidgets.QLineEdit(self.page_coldstart)
        self.lineEdit_coldstart_compared.setGeometry(QtCore.QRect(20, 70, 191, 31))
        self.lineEdit_coldstart_compared.setObjectName("lineEdit_coldstart_compared")
        self.pushButton_coldstart_start = QtWidgets.QPushButton(self.page_coldstart)
        self.pushButton_coldstart_start.setGeometry(QtCore.QRect(480, 50, 93, 28))
        self.pushButton_coldstart_start.setObjectName("pushButton_coldstart_start")
        self.tableWidget_coldstart_output = QtWidgets.QTableWidget(self.page_coldstart)
        self.tableWidget_coldstart_output.setGeometry(QtCore.QRect(10, 160, 1101, 511))
        self.tableWidget_coldstart_output.setObjectName("tableWidget_coldstart_output")
        self.tableWidget_coldstart_output.setColumnCount(0)
        self.tableWidget_coldstart_output.setRowCount(0)
        self.stackedWidget.addWidget(self.page_coldstart)
        self.page_memory = QtWidgets.QWidget()
        self.page_memory.setObjectName("page_memory")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_memory)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 250, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_memory)
        self.page_checklist = QtWidgets.QWidget()
        self.page_checklist.setStyleSheet("QCheckBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QGroupBox{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"\n"
"#label_checklist_output{\n"
"    border: 1px solid gray;\n"
"}")
        self.page_checklist.setObjectName("page_checklist")
        self.btn_checklist_start = QtWidgets.QPushButton(self.page_checklist)
        self.btn_checklist_start.setGeometry(QtCore.QRect(80, 390, 201, 41))
        self.btn_checklist_start.setObjectName("btn_checklist_start")
        self.groupBox = QtWidgets.QGroupBox(self.page_checklist)
        self.groupBox.setGeometry(QtCore.QRect(350, 50, 711, 591))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_checklist_output = QtWidgets.QLabel(self.groupBox)
        self.label_checklist_output.setText("")
        self.label_checklist_output.setObjectName("label_checklist_output")
        self.verticalLayout_7.addWidget(self.label_checklist_output)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_checklist)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 40, 231, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_cpu = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_cpu.setObjectName("checkBox_cpu")
        self.verticalLayout_8.addWidget(self.checkBox_cpu)
        self.checkBox_gpu = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_gpu.setObjectName("checkBox_gpu")
        self.verticalLayout_8.addWidget(self.checkBox_gpu)
        self.checkBox_ddr = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_ddr.setObjectName("checkBox_ddr")
        self.verticalLayout_8.addWidget(self.checkBox_ddr)
        self.checkBox_mem = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_mem.setObjectName("checkBox_mem")
        self.verticalLayout_8.addWidget(self.checkBox_mem)
        self.checkBox_others = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_others.setObjectName("checkBox_others")
        self.verticalLayout_8.addWidget(self.checkBox_others)
        self.lineEdit = QtWidgets.QLineEdit(self.page_checklist)
        self.lineEdit.setGeometry(QtCore.QRect(20, 330, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.page_checklist)
        self.pushButton.setGeometry(QtCore.QRect(240, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_checklist)
        self.page_command = QtWidgets.QWidget()
        self.page_command.setObjectName("page_command")
        self.btn_cmd_start = QtWidgets.QPushButton(self.page_command)
        self.btn_cmd_start.setGeometry(QtCore.QRect(320, 40, 93, 28))
        self.btn_cmd_start.setObjectName("btn_cmd_start")
        self.lineEdit_cmd_search = QtWidgets.QLineEdit(self.page_command)
        self.lineEdit_cmd_search.setGeometry(QtCore.QRect(60, 40, 231, 31))
        self.lineEdit_cmd_search.setObjectName("lineEdit_cmd_search")
        self.tableWidget_cmd_output = QtWidgets.QTableWidget(self.page_command)
        self.tableWidget_cmd_output.setGeometry(QtCore.QRect(30, 100, 1041, 551))
        self.tableWidget_cmd_output.setObjectName("tableWidget_cmd_output")
        self.tableWidget_cmd_output.setColumnCount(0)
        self.tableWidget_cmd_output.setRowCount(0)
        self.stackedWidget.addWidget(self.page_command)
        self.page_tool = QtWidgets.QWidget()
        self.page_tool.setObjectName("page_tool")
        self.stackedWidget.addWidget(self.page_tool)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 29))
        self.menubar.setStyleSheet("QMenuBar {\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menu_connect_devices = QtWidgets.QMenu(self.menubar)
        self.menu_connect_devices.setObjectName("menu_connect_devices")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_connect_devices.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_left_menu.setText(_translate("MainWindow", "   Hide Menu"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "   Home"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "   开关机"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "   冷启动"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "   内存"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "   Check List"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "   常用命令"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "   工具"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "模式选择"))
        self.comboBox_boot_mode_selection.setItemText(0, _translate("MainWindow", "开机"))
        self.comboBox_boot_mode_selection.setItemText(1, _translate("MainWindow", "关机"))
        self.comboBox_boot_mode_selection.setItemText(2, _translate("MainWindow", "重启"))
        self.label_3.setText(_translate("MainWindow", "版本选择"))
        self.comboBox_boot_android_version_selection.setItemText(0, _translate("MainWindow", "A12"))
        self.comboBox_boot_android_version_selection.setItemText(1, _translate("MainWindow", "A13"))
        self.comboBox_boot_android_version_selection.setItemText(2, _translate("MainWindow", "A14"))
        self.label_4.setText(_translate("MainWindow", "在线/离线解析"))
        self.comboBox_boot_online_offline_selection.setItemText(0, _translate("MainWindow", "在线"))
        self.comboBox_boot_online_offline_selection.setItemText(1, _translate("MainWindow", "离线"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "ap文件路径"))
        self.btn_boot_file_selection.setText(_translate("MainWindow", "选择文件"))
        self.btn_boot_parse.setText(_translate("MainWindow", "开始解析"))
        self.btn_coldstart_test.setText(_translate("MainWindow", "选择测试文件"))
        self.btn_coldstart_compared.setText(_translate("MainWindow", "选择对比文件"))
        self.lineEdit_coldstart_test.setPlaceholderText(_translate("MainWindow", "测试文件路径"))
        self.lineEdit_coldstart_compared.setPlaceholderText(_translate("MainWindow", "对比文件路径"))
        self.pushButton_coldstart_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.btn_checklist_start.setText(_translate("MainWindow", "开始检查"))
        self.groupBox.setTitle(_translate("MainWindow", "OutPut"))
        self.groupBox_2.setTitle(_translate("MainWindow", "检查项"))
        self.checkBox_cpu.setText(_translate("MainWindow", "CPU"))
        self.checkBox_gpu.setText(_translate("MainWindow", "GPU"))
        self.checkBox_ddr.setText(_translate("MainWindow", "DDR"))
        self.checkBox_mem.setText(_translate("MainWindow", "Memory"))
        self.checkBox_others.setText(_translate("MainWindow", "Others"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "文件选择"))
        self.pushButton.setText(_translate("MainWindow", "文件选择"))
        self.btn_cmd_start.setText(_translate("MainWindow", "开始搜索"))
        self.lineEdit_cmd_search.setPlaceholderText(_translate("MainWindow", "关键字"))
        self.menu_connect_devices.setTitle(_translate("MainWindow", "连接设备"))
import res.image_rc
