# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'particle_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Particledust(object):
    def setupUi(self, Particledust):
        Particledust.setObjectName("Particledust")
        Particledust.resize(460, 226)
        self.centralwidget = QtWidgets.QWidget(Particledust)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 461, 205))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.randomgen = QtWidgets.QGroupBox(self.tab)
        self.randomgen.setGeometry(QtCore.QRect(280, 0, 171, 181))
        self.randomgen.setObjectName("randomgen")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(-1, 0, 281, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(5, 12, 131, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 15, 31, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.r_spin = QtWidgets.QSpinBox(self.groupBox)
        self.r_spin.setGeometry(QtCore.QRect(50, 15, 51, 22))
        self.r_spin.setMaximum(255)
        self.r_spin.setObjectName("r_spin")
        self.g_spin = QtWidgets.QSpinBox(self.groupBox)
        self.g_spin.setGeometry(QtCore.QRect(50, 40, 51, 22))
        self.g_spin.setMaximum(255)
        self.g_spin.setObjectName("g_spin")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 41, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.b_spin = QtWidgets.QSpinBox(self.groupBox)
        self.b_spin.setGeometry(QtCore.QRect(50, 65, 51, 22))
        self.b_spin.setMaximum(255)
        self.b_spin.setObjectName("b_spin")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 65, 41, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.rgbreturn = QtWidgets.QPushButton(self.groupBox)
        self.rgbreturn.setGeometry(QtCore.QRect(65, 90, 61, 23))
        self.rgbreturn.setObjectName("rgbreturn")
        self.tosharp = QtWidgets.QLineEdit(self.groupBox)
        self.tosharp.setGeometry(QtCore.QRect(10, 91, 51, 20))
        self.tosharp.setAcceptDrops(False)
        self.tosharp.setFrame(False)
        self.tosharp.setReadOnly(True)
        self.tosharp.setObjectName("tosharp")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(140, 12, 141, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(-10, 15, 31, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(0, 40, 21, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(0, 65, 21, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.dx = QtWidgets.QLineEdit(self.groupBox_4)
        self.dx.setGeometry(QtCore.QRect(20, 15, 51, 20))
        self.dx.setObjectName("dx")
        self.dy = QtWidgets.QLineEdit(self.groupBox_4)
        self.dy.setGeometry(QtCore.QRect(20, 40, 51, 20))
        self.dy.setObjectName("dy")
        self.dz = QtWidgets.QLineEdit(self.groupBox_4)
        self.dz.setGeometry(QtCore.QRect(20, 65, 51, 20))
        self.dz.setObjectName("dz")
        self.dcalculate = QtWidgets.QPushButton(self.groupBox_4)
        self.dcalculate.setGeometry(QtCore.QRect(75, 90, 31, 23))
        self.dcalculate.setObjectName("dcalculate")
        self.realtimeprocess = QtWidgets.QCheckBox(self.groupBox_4)
        self.realtimeprocess.setGeometry(QtCore.QRect(80, 10, 51, 51))
        self.realtimeprocess.setChecked(True)
        self.realtimeprocess.setObjectName("realtimeprocess")
        self.readfromopt = QtWidgets.QPushButton(self.groupBox_4)
        self.readfromopt.setGeometry(QtCore.QRect(3, 90, 71, 23))
        self.readfromopt.setObjectName("readfromopt")
        self.tocmdpopt = QtWidgets.QPushButton(self.groupBox_4)
        self.tocmdpopt.setGeometry(QtCore.QRect(107, 90, 31, 23))
        self.tocmdpopt.setObjectName("tocmdpopt")
        self.random_d = QtWidgets.QPushButton(self.groupBox_4)
        self.random_d.setGeometry(QtCore.QRect(80, 63, 51, 23))
        self.random_d.setObjectName("random_d")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 140, 281, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cmdout = QtWidgets.QLineEdit(self.groupBox_2)
        self.cmdout.setGeometry(QtCore.QRect(4, 13, 271, 20))
        self.cmdout.setAcceptDrops(False)
        self.cmdout.setStyleSheet("background-color:#f0f0f0")
        self.cmdout.setFrame(False)
        self.cmdout.setDragEnabled(False)
        self.cmdout.setClearButtonEnabled(True)
        self.cmdout.setObjectName("cmdout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setEnabled(False)
        self.label_14.setGeometry(QtCore.QRect(13, 11, 431, 161))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 0, 211, 181))
        self.groupBox_7.setObjectName("groupBox_7")
        self.simu_img_pre = QtWidgets.QLabel(self.groupBox_7)
        self.simu_img_pre.setGeometry(QtCore.QRect(0, 12, 209, 171))
        self.simu_img_pre.setText("")
        self.simu_img_pre.setAlignment(QtCore.Qt.AlignCenter)
        self.simu_img_pre.setObjectName("simu_img_pre")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(215, 10, 54, 12))
        self.label_15.setObjectName("label_15")
        self.simu_img_path = QtWidgets.QLineEdit(self.tab_4)
        self.simu_img_path.setGeometry(QtCore.QRect(270, 7, 161, 18))
        self.simu_img_path.setFrame(False)
        self.simu_img_path.setReadOnly(True)
        self.simu_img_path.setObjectName("simu_img_path")
        self.simu_img_select = QtWidgets.QPushButton(self.tab_4)
        self.simu_img_select.setGeometry(QtCore.QRect(424, 5, 31, 20))
        self.simu_img_select.setObjectName("simu_img_select")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(215, 130, 81, 16))
        self.label_16.setObjectName("label_16")
        self.simu_ret_forceseq = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.simu_ret_forceseq.setGeometry(QtCore.QRect(290, 127, 62, 22))
        self.simu_ret_forceseq.setMaximum(1.0)
        self.simu_ret_forceseq.setSingleStep(0.01)
        self.simu_ret_forceseq.setProperty("value", 0.95)
        self.simu_ret_forceseq.setObjectName("simu_ret_forceseq")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(215, 33, 54, 12))
        self.label_17.setObjectName("label_17")
        self.simu_img_path_2 = QtWidgets.QLineEdit(self.tab_4)
        self.simu_img_path_2.setGeometry(QtCore.QRect(270, 30, 181, 18))
        self.simu_img_path_2.setAcceptDrops(False)
        self.simu_img_path_2.setFrame(False)
        self.simu_img_path_2.setReadOnly(True)
        self.simu_img_path_2.setObjectName("simu_img_path_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_8.setGeometry(QtCore.QRect(210, 50, 241, 71))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_18 = QtWidgets.QLabel(self.groupBox_8)
        self.label_18.setGeometry(QtCore.QRect(30, 20, 61, 20))
        self.label_18.setObjectName("label_18")
        self.simu_format_float = QtWidgets.QLineEdit(self.groupBox_8)
        self.simu_format_float.setGeometry(QtCore.QRect(10, 20, 16, 20))
        self.simu_format_float.setFrame(False)
        self.simu_format_float.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.simu_format_float.setObjectName("simu_format_float")
        self.label_19 = QtWidgets.QLabel(self.groupBox_8)
        self.label_19.setGeometry(QtCore.QRect(150, 20, 61, 20))
        self.label_19.setObjectName("label_19")
        self.simu_format_scale = QtWidgets.QLineEdit(self.groupBox_8)
        self.simu_format_scale.setGeometry(QtCore.QRect(118, 20, 31, 20))
        self.simu_format_scale.setFrame(False)
        self.simu_format_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.simu_format_scale.setObjectName("simu_format_scale")
        self.label_20 = QtWidgets.QLabel(self.groupBox_8)
        self.label_20.setGeometry(QtCore.QRect(30, 45, 51, 20))
        self.label_20.setObjectName("label_20")
        self.simu_format_yf = QtWidgets.QLineEdit(self.groupBox_8)
        self.simu_format_yf.setGeometry(QtCore.QRect(10, 45, 16, 20))
        self.simu_format_yf.setFrame(False)
        self.simu_format_yf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.simu_format_yf.setObjectName("simu_format_yf")
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setEnabled(False)
        self.label_21.setGeometry(QtCore.QRect(120, 45, 51, 20))
        self.label_21.setObjectName("label_21")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(170, 45, 51, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.simu_start = QtWidgets.QPushButton(self.tab_4)
        self.simu_start.setGeometry(QtCore.QRect(370, 127, 75, 23))
        self.simu_start.setObjectName("simu_start")
        self.simu_log = QtWidgets.QLabel(self.tab_4)
        self.simu_log.setGeometry(QtCore.QRect(220, 152, 201, 20))
        self.simu_log.setObjectName("simu_log")
        self.simu_color_now = QtWidgets.QLabel(self.tab_4)
        self.simu_color_now.setGeometry(QtCore.QRect(430, 153, 20, 20))
        self.simu_color_now.setFrameShape(QtWidgets.QFrame.Box)
        self.simu_color_now.setAlignment(QtCore.Qt.AlignCenter)
        self.simu_color_now.setObjectName("simu_color_now")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.cmdsetting = QtWidgets.QGroupBox(self.tab_2)
        self.cmdsetting.setGeometry(QtCore.QRect(20, 0, 141, 171))
        self.cmdsetting.setObjectName("cmdsetting")
        self.label_4 = QtWidgets.QLabel(self.cmdsetting)
        self.label_4.setGeometry(QtCore.QRect(3, 15, 31, 20))
        self.label_4.setObjectName("label_4")
        self.prefix = QtWidgets.QLineEdit(self.cmdsetting)
        self.prefix.setGeometry(QtCore.QRect(30, 15, 101, 20))
        self.prefix.setFrame(False)
        self.prefix.setObjectName("prefix")
        self.label_5 = QtWidgets.QLabel(self.cmdsetting)
        self.label_5.setGeometry(QtCore.QRect(3, 40, 31, 20))
        self.label_5.setObjectName("label_5")
        self.particleid = QtWidgets.QLineEdit(self.cmdsetting)
        self.particleid.setGeometry(QtCore.QRect(30, 40, 101, 20))
        self.particleid.setFrame(False)
        self.particleid.setObjectName("particleid")
        self.particlescale = QtWidgets.QLineEdit(self.cmdsetting)
        self.particlescale.setGeometry(QtCore.QRect(30, 65, 101, 20))
        self.particlescale.setFrame(False)
        self.particlescale.setObjectName("particlescale")
        self.label_6 = QtWidgets.QLabel(self.cmdsetting)
        self.label_6.setGeometry(QtCore.QRect(3, 65, 31, 20))
        self.label_6.setObjectName("label_6")
        self.particlepos = QtWidgets.QLineEdit(self.cmdsetting)
        self.particlepos.setGeometry(QtCore.QRect(30, 90, 101, 20))
        self.particlepos.setFrame(False)
        self.particlepos.setObjectName("particlepos")
        self.label_10 = QtWidgets.QLabel(self.cmdsetting)
        self.label_10.setGeometry(QtCore.QRect(3, 90, 31, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.cmdsetting)
        self.label_11.setGeometry(QtCore.QRect(3, 115, 31, 20))
        self.label_11.setObjectName("label_11")
        self.particlespreadpos = QtWidgets.QLineEdit(self.cmdsetting)
        self.particlespreadpos.setGeometry(QtCore.QRect(30, 115, 101, 20))
        self.particlespreadpos.setFrame(False)
        self.particlespreadpos.setObjectName("particlespreadpos")
        self.label_12 = QtWidgets.QLabel(self.cmdsetting)
        self.label_12.setGeometry(QtCore.QRect(3, 140, 31, 20))
        self.label_12.setObjectName("label_12")
        self.particlespeed = QtWidgets.QLineEdit(self.cmdsetting)
        self.particlespeed.setGeometry(QtCore.QRect(30, 140, 31, 20))
        self.particlespeed.setFrame(False)
        self.particlespeed.setObjectName("particlespeed")
        self.label_13 = QtWidgets.QLabel(self.cmdsetting)
        self.label_13.setGeometry(QtCore.QRect(65, 140, 31, 20))
        self.label_13.setObjectName("label_13")
        self.particlenum = QtWidgets.QLineEdit(self.cmdsetting)
        self.particlenum.setGeometry(QtCore.QRect(95, 140, 36, 20))
        self.particlenum.setFrame(False)
        self.particlenum.setObjectName("particlenum")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(170, 0, 281, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.forcesimilar_enable = QtWidgets.QCheckBox(self.groupBox_5)
        self.forcesimilar_enable.setGeometry(QtCore.QRect(60, 20, 91, 21))
        self.forcesimilar_enable.setObjectName("forcesimilar_enable")
        self.forcesimilar_value = QtWidgets.QLineEdit(self.groupBox_5)
        self.forcesimilar_value.setEnabled(False)
        self.forcesimilar_value.setGeometry(QtCore.QRect(155, 20, 61, 20))
        self.forcesimilar_value.setObjectName("forcesimilar_value")
        self.force_net_enable = QtWidgets.QCheckBox(self.groupBox_5)
        self.force_net_enable.setGeometry(QtCore.QRect(60, 40, 111, 21))
        self.force_net_enable.setObjectName("force_net_enable")
        self.force_net_value = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.force_net_value.setEnabled(False)
        self.force_net_value.setGeometry(QtCore.QRect(165, 40, 51, 22))
        self.force_net_value.setMinimum(0.48)
        self.force_net_value.setMaximum(1.0)
        self.force_net_value.setSingleStep(0.001)
        self.force_net_value.setProperty("value", 0.74)
        self.force_net_value.setObjectName("force_net_value")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(170, 70, 281, 101))
        self.groupBox_6.setObjectName("groupBox_6")
        self.log = QtWidgets.QTextEdit(self.groupBox_6)
        self.log.setGeometry(QtCore.QRect(2, 12, 278, 87))
        self.log.setAcceptDrops(False)
        self.log.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.log.setUndoRedoEnabled(False)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.tabWidget.addTab(self.tab_2, "")
        Particledust.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Particledust)
        self.statusbar.setObjectName("statusbar")
        Particledust.setStatusBar(self.statusbar)

        self.retranslateUi(Particledust)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Particledust)

    def retranslateUi(self, Particledust):
        _translate = QtCore.QCoreApplication.translate
        Particledust.setWindowTitle(_translate("Particledust", "dust粒子生成模拟器"))
        self.randomgen.setTitle(_translate("Particledust", "随机颜色生成器"))
        self.groupBox_3.setTitle(_translate("Particledust", "转换"))
        self.groupBox.setTitle(_translate("Particledust", "RGB"))
        self.label.setText(_translate("Particledust", "Red:"))
        self.label_2.setText(_translate("Particledust", "Green:"))
        self.label_3.setText(_translate("Particledust", "Blue:"))
        self.rgbreturn.setText(_translate("Particledust", "随机还原"))
        self.tosharp.setText(_translate("Particledust", "#000000"))
        self.groupBox_4.setTitle(_translate("Particledust", "data-XYZ"))
        self.label_7.setText(_translate("Particledust", "dx:"))
        self.label_8.setText(_translate("Particledust", "dy:"))
        self.label_9.setText(_translate("Particledust", "dz:"))
        self.dcalculate.setText(_translate("Particledust", "计算"))
        self.realtimeprocess.setText(_translate("Particledust", "启用\n"
"实时\n"
"计算"))
        self.readfromopt.setText(_translate("Particledust", "从指令读取"))
        self.tocmdpopt.setText(_translate("Particledust", "输出"))
        self.random_d.setText(_translate("Particledust", "随机数"))
        self.groupBox_2.setTitle(_translate("Particledust", "指令输出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Particledust", "生成"))
        self.label_14.setText(_translate("Particledust", "施工中"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Particledust", "模拟"))
        self.groupBox_7.setTitle(_translate("Particledust", "图像预览"))
        self.label_15.setText(_translate("Particledust", "图像路径："))
        self.simu_img_select.setText(_translate("Particledust", "..."))
        self.label_16.setText(_translate("Particledust", "还原相似度："))
        self.label_17.setText(_translate("Particledust", "输出路径："))
        self.groupBox_8.setTitle(_translate("Particledust", "格式化"))
        self.label_18.setText(_translate("Particledust", "位浮点小数"))
        self.simu_format_float.setInputMask(_translate("Particledust", "0;_"))
        self.simu_format_float.setText(_translate("Particledust", "5"))
        self.label_19.setText(_translate("Particledust", "x距离缩放"))
        self.simu_format_scale.setText(_translate("Particledust", "0.2"))
        self.label_20.setText(_translate("Particledust", "Y轴偏移"))
        self.simu_format_yf.setInputMask(_translate("Particledust", "0;_"))
        self.simu_format_yf.setText(_translate("Particledust", "1"))
        self.label_21.setText(_translate("Particledust", "展开方向"))
        self.comboBox.setItemText(0, _translate("Particledust", "X+Y+"))
        self.simu_start.setText(_translate("Particledust", "开始还原"))
        self.simu_log.setText(_translate("Particledust", "等待中..."))
        self.simu_color_now.setText(_translate("Particledust", "Now"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Particledust", "图像"))
        self.cmdsetting.setTitle(_translate("Particledust", "指令参数设置"))
        self.label_4.setText(_translate("Particledust", "前缀"))
        self.prefix.setText(_translate("Particledust", "particle"))
        self.label_5.setText(_translate("Particledust", "粒子"))
        self.particleid.setText(_translate("Particledust", "minecraft:dust"))
        self.particlescale.setText(_translate("Particledust", "1"))
        self.label_6.setText(_translate("Particledust", "放缩"))
        self.particlepos.setText(_translate("Particledust", "~ ~1 ~"))
        self.label_10.setText(_translate("Particledust", "位置"))
        self.label_11.setText(_translate("Particledust", "延展"))
        self.particlespreadpos.setText(_translate("Particledust", "0.1 0.1 0.1"))
        self.label_12.setText(_translate("Particledust", "速度"))
        self.particlespeed.setText(_translate("Particledust", "1"))
        self.label_13.setText(_translate("Particledust", "数量"))
        self.particlenum.setText(_translate("Particledust", "10"))
        self.groupBox_5.setTitle(_translate("Particledust", "生成参数设置"))
        self.forcesimilar_enable.setText(_translate("Particledust", "强制相似度>="))
        self.forcesimilar_value.setText(_translate("Particledust", "0.85"))
        self.force_net_enable.setText(_translate("Particledust", "强制固定随机值"))
        self.groupBox_6.setTitle(_translate("Particledust", "日志"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Particledust", "设置"))
