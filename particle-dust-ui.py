from particle_ui_pyuic import Ui_Particledust
from APIparticle_dustONLY import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import os


class simu_ret(QThread):
    def __init__(self, main_):
        super().__init__()
        self.haveprocess = False
        self._main = main_
        self.imgtarget = None

    def settarget(self, path, option):
        self.imgtarget = path
        self.option = option
        self.haveprocess = True
        self.startt = time.time()

    def run(self):
        while True:
            if self.haveprocess:
                try:
                    self.startt = time.time()
                    data = ProcessImage2dust_singleThread(self.imgtarget, self._main, self.option[0])
                    if not data[0]:
                        self._main.setsimulog(data[1])
                        self.haveprocess = False
                    else:
                        data = data[1]
                        write2mcfunction(data, self.option[1], self.option[2], self.option[3], self.option[4])
                        self._main.setsimulog('已完成！用时%.3f秒' % (time.time() - self.startt))
                        self._main.simu_start.setEnabled(True)
                        self.haveprocess = False
                except Exception as e:
                    self.haveprocess = False
                    self._main.setsimulog('[ERR]' + str(e))
            else:
                time.sleep(1)


class RGBLabel(QLabel):
    def __init__(self, parent=None):
        super(RGBLabel, self).__init__(parent)

    def setMain(self, main):
        self._main = main

    def mouseDoubleClickEvent(self, e):
        self.do()

    def mousePressEvent(self, e):
        self.do()

    def do(self):
        c = QColorDialog.getColor()
        r, g, b = hex2rgb(c.name())
        self._main.r_spin.setValue(r)
        self._main.g_spin.setValue(g)
        self._main.b_spin.setValue(b)
        self._main.log.append('从选择器选定目标颜色%s' % c.name())


class Random_RGBLabel(QLabel):
    def __init__(self, parent=None):
        super(Random_RGBLabel, self).__init__(parent)

    def setMain(self, main):
        self._main = main

    def mouseDoubleClickEvent(self, e):
        self.do()

    def mousePressEvent(self, e):
        self.do()

    def enterEvent(self, *args, **kwargs):
        try:
            hex_s = self.styleSheet().replace('background-color:', '')
            hex_d = self._main.tosharp.text()
            loss = map_r_g_b_distance(hex2rgb(hex_d), hex2rgb(hex_s))
            self._main.statusbar.showMessage(hex_d + ' ' + hex_s + '    ->' + str(round(loss, 7)) + 'Similar')
        except Exception as e:
            self._main.statusbar.showMessage(str(e))

    def do(self):
        r, g, b = hex2rgb(self.styleSheet().replace('background-color:', ''))
        self._main.r_spin.setValue(r)
        self._main.g_spin.setValue(g)
        self._main.b_spin.setValue(b)
        self._main.log.append('从生成器选定目标颜色%s' % rgb2hex(r, g, b))


class Dialog(QMainWindow, Ui_Particledust):
    def __init__(self):
        # 一切定义放在最前面
        super(Dialog, self).__init__()

        self._r = 0
        self._g = 0
        self._b = 0
        self.simuthr = simu_ret(self)
        self.simuthr.start()
        self.simu_max = 0
        self.simu_now = 0
        self.lastupdate = time.time()
        self._realtime = True
        self.setupUi(self)
        self.setupUi_custom()

    def setupUi_custom(self):

        self.targetcolor = RGBLabel(self.groupBox)
        self.targetcolor.setMain(self)
        self.targetcolor.setGeometry(QRect(100, 15, 21, 71))
        self.targetcolor.setStyleSheet("background-color:#000000;color:#FFFFFF")
        self.targetcolor.setFrameShape(QFrame.StyledPanel)
        self.targetcolor.setAlignment(Qt.AlignCenter)
        self.targetcolor.setObjectName("targetcolor")

        self.a_0 = Random_RGBLabel(self.randomgen)
        self.a_0.setGeometry(QRect(10, 20, 16, 16))
        self.a_0.setObjectName("a_0")
        self.a_1 = Random_RGBLabel(self.randomgen)
        self.a_1.setGeometry(QRect(30, 20, 16, 16))
        self.a_1.setObjectName("a_1")
        self.a_2 = Random_RGBLabel(self.randomgen)
        self.a_2.setGeometry(QRect(50, 20, 16, 16))
        self.a_2.setObjectName("a_2")
        self.a_3 = Random_RGBLabel(self.randomgen)
        self.a_3.setGeometry(QRect(70, 20, 16, 16))
        self.a_3.setObjectName("a_3")
        self.a_4 = Random_RGBLabel(self.randomgen)
        self.a_4.setGeometry(QRect(90, 20, 16, 16))
        self.a_4.setObjectName("a_4")
        self.a_5 = Random_RGBLabel(self.randomgen)
        self.a_5.setGeometry(QRect(110, 20, 16, 16))
        self.a_5.setObjectName("a_5")
        self.a_6 = Random_RGBLabel(self.randomgen)
        self.a_6.setGeometry(QRect(130, 20, 16, 16))
        self.a_6.setObjectName("a_6")
        self.a_7 = Random_RGBLabel(self.randomgen)
        self.a_7.setGeometry(QRect(150, 20, 16, 16))
        self.a_7.setObjectName("a_7")
        self.a_8 = Random_RGBLabel(self.randomgen)
        self.a_8.setGeometry(QRect(10, 40, 16, 16))
        self.a_8.setObjectName("a_8")
        self.a_9 = Random_RGBLabel(self.randomgen)
        self.a_9.setGeometry(QRect(30, 40, 16, 16))
        self.a_9.setObjectName("a_9")
        self.a_10 = Random_RGBLabel(self.randomgen)
        self.a_10.setGeometry(QRect(50, 40, 16, 16))
        self.a_10.setObjectName("a_10")
        self.a_11 = Random_RGBLabel(self.randomgen)
        self.a_11.setGeometry(QRect(70, 40, 16, 16))
        self.a_11.setObjectName("a_11")
        self.a_12 = Random_RGBLabel(self.randomgen)
        self.a_12.setGeometry(QRect(90, 40, 16, 16))
        self.a_12.setObjectName("a_12")
        self.a_13 = Random_RGBLabel(self.randomgen)
        self.a_13.setGeometry(QRect(110, 40, 16, 16))
        self.a_13.setObjectName("a_13")
        self.a_14 = Random_RGBLabel(self.randomgen)
        self.a_14.setGeometry(QRect(130, 40, 16, 16))
        self.a_14.setObjectName("a_14")
        self.a_15 = Random_RGBLabel(self.randomgen)
        self.a_15.setGeometry(QRect(150, 40, 16, 16))
        self.a_15.setObjectName("a_15")
        self.a_16 = Random_RGBLabel(self.randomgen)
        self.a_16.setGeometry(QRect(10, 60, 16, 16))
        self.a_16.setObjectName("a_16")
        self.a_17 = Random_RGBLabel(self.randomgen)
        self.a_17.setGeometry(QRect(30, 60, 16, 16))
        self.a_17.setObjectName("a_17")
        self.a_18 = Random_RGBLabel(self.randomgen)
        self.a_18.setGeometry(QRect(50, 60, 16, 16))
        self.a_18.setObjectName("a_18")
        self.a_19 = Random_RGBLabel(self.randomgen)
        self.a_19.setGeometry(QRect(70, 60, 16, 16))
        self.a_19.setObjectName("a_19")
        self.a_20 = Random_RGBLabel(self.randomgen)
        self.a_20.setGeometry(QRect(90, 60, 16, 16))
        self.a_20.setObjectName("a_20")
        self.a_21 = Random_RGBLabel(self.randomgen)
        self.a_21.setGeometry(QRect(110, 60, 16, 16))
        self.a_21.setObjectName("a_21")
        self.a_22 = Random_RGBLabel(self.randomgen)
        self.a_22.setGeometry(QRect(130, 60, 16, 16))
        self.a_22.setObjectName("a_22")
        self.a_23 = Random_RGBLabel(self.randomgen)
        self.a_23.setGeometry(QRect(150, 60, 16, 16))
        self.a_23.setObjectName("a_23")
        self.a_24 = Random_RGBLabel(self.randomgen)
        self.a_24.setGeometry(QRect(10, 80, 16, 16))
        self.a_24.setObjectName("a_24")
        self.a_25 = Random_RGBLabel(self.randomgen)
        self.a_25.setGeometry(QRect(30, 80, 16, 16))
        self.a_25.setObjectName("a_25")
        self.a_26 = Random_RGBLabel(self.randomgen)
        self.a_26.setGeometry(QRect(50, 80, 16, 16))
        self.a_26.setObjectName("a_26")
        self.a_27 = Random_RGBLabel(self.randomgen)
        self.a_27.setGeometry(QRect(70, 80, 16, 16))
        self.a_27.setObjectName("a_27")
        self.a_28 = Random_RGBLabel(self.randomgen)
        self.a_28.setGeometry(QRect(90, 80, 16, 16))
        self.a_28.setObjectName("a_28")
        self.a_29 = Random_RGBLabel(self.randomgen)
        self.a_29.setGeometry(QRect(110, 80, 16, 16))
        self.a_29.setObjectName("a_29")
        self.a_30 = Random_RGBLabel(self.randomgen)
        self.a_30.setGeometry(QRect(130, 80, 16, 16))
        self.a_30.setObjectName("a_30")
        self.a_31 = Random_RGBLabel(self.randomgen)
        self.a_31.setGeometry(QRect(150, 80, 16, 16))
        self.a_31.setObjectName("a_31")
        self.a_32 = Random_RGBLabel(self.randomgen)
        self.a_32.setGeometry(QRect(10, 100, 16, 16))
        self.a_32.setObjectName("a_32")
        self.a_33 = Random_RGBLabel(self.randomgen)
        self.a_33.setGeometry(QRect(30, 100, 16, 16))
        self.a_33.setObjectName("a_33")
        self.a_34 = Random_RGBLabel(self.randomgen)
        self.a_34.setGeometry(QRect(50, 100, 16, 16))
        self.a_34.setObjectName("a_34")
        self.a_35 = Random_RGBLabel(self.randomgen)
        self.a_35.setGeometry(QRect(70, 100, 16, 16))
        self.a_35.setObjectName("a_35")
        self.a_36 = Random_RGBLabel(self.randomgen)
        self.a_36.setGeometry(QRect(90, 100, 16, 16))
        self.a_36.setObjectName("a_36")
        self.a_37 = Random_RGBLabel(self.randomgen)
        self.a_37.setGeometry(QRect(110, 100, 16, 16))
        self.a_37.setObjectName("a_37")
        self.a_38 = Random_RGBLabel(self.randomgen)
        self.a_38.setGeometry(QRect(130, 100, 16, 16))
        self.a_38.setObjectName("a_38")
        self.a_39 = Random_RGBLabel(self.randomgen)
        self.a_39.setGeometry(QRect(150, 100, 16, 16))
        self.a_39.setObjectName("a_39")
        self.a_40 = Random_RGBLabel(self.randomgen)
        self.a_40.setGeometry(QRect(10, 120, 16, 16))
        self.a_40.setObjectName("a_40")
        self.a_41 = Random_RGBLabel(self.randomgen)
        self.a_41.setGeometry(QRect(30, 120, 16, 16))
        self.a_41.setObjectName("a_41")
        self.a_42 = Random_RGBLabel(self.randomgen)
        self.a_42.setGeometry(QRect(50, 120, 16, 16))
        self.a_42.setObjectName("a_42")
        self.a_43 = Random_RGBLabel(self.randomgen)
        self.a_43.setGeometry(QRect(70, 120, 16, 16))
        self.a_43.setObjectName("a_43")
        self.a_44 = Random_RGBLabel(self.randomgen)
        self.a_44.setGeometry(QRect(90, 120, 16, 16))
        self.a_44.setObjectName("a_44")
        self.a_45 = Random_RGBLabel(self.randomgen)
        self.a_45.setGeometry(QRect(110, 120, 16, 16))
        self.a_45.setObjectName("a_45")
        self.a_46 = Random_RGBLabel(self.randomgen)
        self.a_46.setGeometry(QRect(130, 120, 16, 16))
        self.a_46.setObjectName("a_46")
        self.a_47 = Random_RGBLabel(self.randomgen)
        self.a_47.setGeometry(QRect(150, 120, 16, 16))
        self.a_47.setObjectName("a_47")
        self.a_48 = Random_RGBLabel(self.randomgen)
        self.a_48.setGeometry(QRect(10, 140, 16, 16))
        self.a_48.setObjectName("a_48")
        self.a_49 = Random_RGBLabel(self.randomgen)
        self.a_49.setGeometry(QRect(30, 140, 16, 16))
        self.a_49.setObjectName("a_49")
        self.a_50 = Random_RGBLabel(self.randomgen)
        self.a_50.setGeometry(QRect(50, 140, 16, 16))
        self.a_50.setObjectName("a_50")
        self.a_51 = Random_RGBLabel(self.randomgen)
        self.a_51.setGeometry(QRect(70, 140, 16, 16))
        self.a_51.setObjectName("a_51")
        self.a_52 = Random_RGBLabel(self.randomgen)
        self.a_52.setGeometry(QRect(90, 140, 16, 16))
        self.a_52.setObjectName("a_52")
        self.a_53 = Random_RGBLabel(self.randomgen)
        self.a_53.setGeometry(QRect(110, 140, 16, 16))
        self.a_53.setObjectName("a_53")
        self.a_54 = Random_RGBLabel(self.randomgen)
        self.a_54.setGeometry(QRect(130, 140, 16, 16))
        self.a_54.setObjectName("a_54")
        self.a_55 = Random_RGBLabel(self.randomgen)
        self.a_55.setGeometry(QRect(150, 140, 16, 16))
        self.a_55.setObjectName("a_55")
        self.a_56 = Random_RGBLabel(self.randomgen)
        self.a_56.setGeometry(QRect(10, 160, 16, 16))
        self.a_56.setObjectName("a_56")
        self.a_57 = Random_RGBLabel(self.randomgen)
        self.a_57.setGeometry(QRect(30, 160, 16, 16))
        self.a_57.setObjectName("a_57")
        self.a_58 = Random_RGBLabel(self.randomgen)
        self.a_58.setGeometry(QRect(50, 160, 16, 16))
        self.a_58.setObjectName("a_58")
        self.a_59 = Random_RGBLabel(self.randomgen)
        self.a_59.setGeometry(QRect(70, 160, 16, 16))
        self.a_59.setObjectName("a_59")
        self.a_60 = Random_RGBLabel(self.randomgen)
        self.a_60.setGeometry(QRect(90, 160, 16, 16))
        self.a_60.setObjectName("a_60")
        self.a_61 = Random_RGBLabel(self.randomgen)
        self.a_61.setGeometry(QRect(110, 160, 16, 16))
        self.a_61.setObjectName("a_61")
        self.a_62 = Random_RGBLabel(self.randomgen)
        self.a_62.setGeometry(QRect(130, 160, 16, 16))
        self.a_62.setObjectName("a_62")
        self.a_63 = Random_RGBLabel(self.randomgen)
        self.a_63.setGeometry(QRect(150, 160, 16, 16))
        self.a_63.setObjectName("a_63")

        for i in range(0, 64):
            self.__getattribute__('a_' + str(i)).setMain(self)
        _translate = QCoreApplication.translate
        self.targetcolor.setText(_translate("MainWindow", "目\n标\n颜\n色"))

        self.r_spin.valueChanged.connect(lambda: self.spin_update('r'))
        self.g_spin.valueChanged.connect(lambda: self.spin_update('g'))
        self.b_spin.valueChanged.connect(lambda: self.spin_update('b'))
        self.rgbreturn.clicked.connect(lambda: self.rgb2dxyz())
        self.dcalculate.clicked.connect(lambda: self.startcalculate('d'))
        self.tocmdpopt.clicked.connect(lambda: self.print2opt())
        self.readfromopt.clicked.connect(lambda: self.readfromopt_f())
        self.realtimeprocess.stateChanged.connect(self.realtimestagechange)
        self.random_d.clicked.connect(lambda: self.random_d_f())
        self.dx.textChanged.connect(lambda: self.rtcalculate())
        self.dy.textChanged.connect(lambda: self.rtcalculate())
        self.dz.textChanged.connect(lambda: self.rtcalculate())
        self.forcesimilar_enable.stateChanged.connect(self.forcesimilar_value_set)
        self.force_net_enable.stateChanged.connect(self.force_net_value_set)
        self.simu_img_select.clicked.connect(lambda: self.simu_choose_img())
        self.simu_start.clicked.connect(lambda: self.startsimulate())

    def setsimulog(self, log):
        self.simu_log.setText(log)

    def setsimuall(self, all):
        # self.simu_proc_bar.setMaximum(all)
        self.simu_max = all

    def setsimunum(self, num):
        # if time.time() - self.lastupdate
        # self.simu_log.setText('还原中...%s' % (int(100 * (self.simu_now / self.simu_max))) + '%' + ' [%s/%s][#%s]' % (self.simu_now, self.simu_max,num))
        pass

    def setsimunow(self, now):
        # self.simu_proc_bar.setValue(now)
        self.simu_now = now
        self.simu_log.setText('还原中...%s' % (int(100 * (now / self.simu_max))) + '%' + ' [%s/%s]' % (now, self.simu_max))

    def startsimulate(self):
        self.simu_start.setEnabled(False)
        self.simuthr.settarget(self.simu_img_path.text(),
                               [float(self.simu_ret_forceseq.text()), self.simu_img_path_2.text(),
                                'particle minecraft:dust %.5f %.5f %.5f 1 ~%s ~%s ~%s 0 0 0 0 1',
                                float(self.simu_format_scale.text()), int(self.simu_format_yf.text())])

    def simu_choose_img(self):
        print('1')
        file_, filetype = QFileDialog.getOpenFileName(self,
                                                      "选取图片",
                                                      os.path.dirname(__file__),
                                                      "All Files (*);;Image Files (*.png *.jpg)")  # 设置文件扩展名过滤,注意用双分号间隔
        if file_ != '':
            self.simu_img_path.setText(file_)
            self.simu_img_path_2.setText(file_.replace('.png', '.mcfunction').replace('.jpg', '.mcfunction'))
        self.showsimuimg(file_)

    def showsimuimg(self, file_):
        a = QPixmap(file_)
        print(file_, a.height(), a.width())
        if a.height() > 171 or a.width() > 209:
            xbit = a.width() / 209
            ybit = a.height() / 171
            a = a.scaled(int(a.width() / max(xbit, ybit)), int(a.height() / max(xbit, ybit)))
        self.simu_img_pre.setPixmap(a)

    def force_net_value_set(self, state):
        self.force_net_value.setEnabled(bool(state))
        if bool(state):
            self.log.append('已禁用启用强制固定随机值')
        else:
            self.log.append('已禁用强制固定随机值')

    def forcesimilar_value_set(self, state):
        self.forcesimilar_value.setEnabled(bool(state))
        if bool(state):
            self.log.append('已启用强制相似度')
        else:
            self.log.append('已禁用强制相似度')

    def realtimestagechange(self, type):
        self._realtime = bool(type)
        self.statusbar.showMessage('实时计算已设置为%s' % str(bool(type)))
        self.log.append('实时计算已设置为%s' % str(bool(type)))

    def random_d_f(self):
        self._realtime = False
        self.dx.setText(str(round(random.uniform(-2.1, 2.1), 5)))
        self.dy.setText(str(round(random.uniform(-2.1, 2.1), 5)))
        self.dz.setText(str(round(random.uniform(-2.1, 2.1), 5)))
        self._realtime = bool(self.realtimeprocess.isChecked())
        self.startcalculate('d')
        self.statusbar.showMessage('设置随机data-XYZ成功')
        self.log.append('随机数设置<%s,%s,%s>' % (self.dx.text(), self.dy.text(), self.dz.text()))

    def readfromopt_f(self):
        try:
            spl = self.cmdout.text().split(' ')
            self._realtime = False
            fe = self.forcesimilar_enable.isChecked()
            self.forcesimilar_enable.setChecked(False)
            self.dx.setText(spl[2])
            self.dy.setText(spl[3])
            self.dz.setText(spl[4])
            self._realtime = bool(self.realtimeprocess.isChecked())
            self.startcalculate()
            self.statusbar.showMessage('从指令中读取data-XYZ成功')
            self.log.append('从指令读取成功<%s,%s,%s>' % (spl[2], spl[3], spl[4]))
            self.forcesimilar_enable.setChecked(fe)
        except:
            self.statusbar.showMessage('从指令中读取data-XYZ失败,请保证指令规范')

    def rtcalculate(self):
        if self._realtime:
            try:
                self.startcalculate('d')
                self.statusbar.showMessage('完成实时计算')
            except:
                self.statusbar.showMessage('实时计算失败')

    def startcalculate(self, from_='n'):
        if self.forcesimilar_enable.isChecked() and from_ != 'd':
            self._realtime = False
            notfinish = True
            trytime = 0
            max_similar = -1
            d = 0
            while notfinish:
                trytime += 1
                self.statusbar.showMessage('正在计算...%s' % trytime)
                if trytime >= 10000:
                    notfinish = False
                    self.statusbar.showMessage('计算失败:请降低相似度并再次尝试[最高相似度%.4f<%.4f %.4f %.4f>]' % (max_similar, *d))
                    self.log.append('还原计算失败[与%s最高相似度%.4f<%.4f %.4f %.4f>]' % (self.tosharp.text(), max_similar, *d))
                    self.dx.setText(float2str(round(d[0], 6)))
                    self.dy.setText(float2str(round(d[1], 6)))
                    self.dz.setText(float2str(round(d[2], 6)))
                    for i in range(0, 64):
                        self.__getattribute__('a_' + str(i)).setStyleSheet('background-color:%s' % rgb2hex(
                            *calculate_d2rgb(float(self.dx.text()), float(self.dy.text()), float(self.dz.text()))))
                    self.print2opt()
                    self._realtime = bool(self.realtimeprocess.isChecked())
                dx, dy, dz = calculate_rgb2d(self._r, self._g, self._b)
                u = mapcolordistance_and_wave(self.tosharp.text(), dx, dy, dz, False)
                if u[0] >= float(self.forcesimilar_value.text()):
                    centre_rgb, wave = mapcolor_wave_with_d(dx, dy, dz)
                    self.dx.setText(float2str(dx))
                    self.dy.setText(float2str(dy))
                    self.dz.setText(float2str(dz))
                    for i in range(0, 64):
                        self.__getattribute__('a_' + str(i)).setStyleSheet('background-color:%s' % rgb2hex(
                            *calculate_d2rgb(float(self.dx.text()), float(self.dy.text()), float(self.dz.text()))))
                    self.print2opt()
                    self.statusbar.showMessage('完成计算[相似度%.5f][与颜色中值%s差距%s]' % (u[0], rgb2hex(*centre_rgb), wave))
                    self.log.append('完成计算[目标颜色%s][尝试%s次][相似度%.5f]' % (self.tosharp.text(), trytime, u[0]))
                    self._realtime = bool(self.realtimeprocess.isChecked())
                    notfinish = False
                elif u[0] > max_similar:
                    max_similar = u[0]
                    d = (dx, dy, dz)
        else:
            try:
                for i in range(0, 64):
                    self.__getattribute__('a_' + str(i)).setStyleSheet('background-color:%s' % rgb2hex(
                        *calculate_d2rgb(float(self.dx.text()), float(self.dy.text()), float(self.dz.text()))))
                self.print2opt()
                if from_ == 'r':
                    p = mapcolordistance_and_wave(self.tosharp.text(), float(self.dx.text()), float(self.dy.text()),
                                                  float(self.dz.text()))
                    self.statusbar.showMessage('完成计算[相似度%.5f][与颜色中值%s差距%s]' % (p[0], rgb2hex(*p[1]), p[2]))
                    self.log.append('完成计算[相似度%.5f]' % p[0])
                if from_ == 'd':
                    self.statusbar.showMessage('完成单次计算')
            except ValueError:
                self.statusbar.showMessage('计算失败:请检查dx,dy,dz数据是否正常！')

    def print2opt(self):
        self.cmdout.setText('%s %s %s %s %s %s %s %s %s %s' % (
            self.prefix.text(), self.particleid.text(), self.dx.text(), self.dy.text(), self.dz.text(),
            self.particlescale.text(), self.particlepos.text(), self.particlespreadpos.text(),
            self.particlespeed.text(), self.particlenum.text()))

    def rgb2dxyz(self):
        if not self.forcesimilar_enable.isChecked():
            dx, dy, dz = calculate_rgb2d(self._r, self._g, self._b)
            self._realtime = False
            self.dx.setText(float2str(dx))
            self.dy.setText(float2str(dy))
            self.dz.setText(float2str(dz))
            self._realtime = bool(self.realtimeprocess.isChecked())
        self.startcalculate('r')

    def spin_update(self, type):
        if type == 'r':
            self._r = int(self.r_spin.value())
            self.update_rgb()
        if type == 'g':
            self._g = int(self.g_spin.value())
            self.update_rgb()
        if type == 'b':
            self._b = int(self.b_spin.value())
            self.update_rgb()

    def update_rgb(self):
        hex_ = rgb2hex(self._r, self._g, self._b)
        de_hex_ = rgb2hex(255 - self._r, 255 - self._g, 255 - self._b)
        self.targetcolor.setStyleSheet('background-color:%s;color:%s' % (hex_, de_hex_))
        self.tosharp.setText(hex_)


def exitprog(exitcode):
    sys.exit(exitcode)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    d = Dialog()
    d.show()

    exitprog(app.exec_())

# TODO ID#1 :mapcolordistance('#fefef5',-0.01,-0.01,1) ->0.97但却无法通过随机还原得到 ok

# TODO ID#2 :(2.39141 1.03023 -0.00473)效果与(2.39141 1.03023 -0.0473)效果预测值相同但是MC中表现完全不符
#            "-0.00473"在游戏中表现为0 ok

# TODO: ID#3 :使用异步线程！！在同线程中会造成UI卡顿
