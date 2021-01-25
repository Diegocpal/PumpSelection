# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *

class Ui_MainWindow(object):
    def calcular(self):

        mode = self.mfuncionamiento.text() #seregistra modo de funcionamiento seleccionado
        q = self.Caudal.text() #se registra el caudal deseado en l/min
        t = self.tambiental.text() #se registra la temperatura ambiental en °C
        ptk = self.presion.text() #Se registra la presión de los tanques en psi

        if q == '' or t == '' or ptk == '':
            self.bomba.setText('Por favor, introduzca todos los datos solicitados.')
        else:
            output = main(float(q), float(t), int(mode), float(ptk))

            self.bomba.setText(str(output[0]))
            self.rpm.setText(str(output[1]))
            self.diametro.setText(str(output[2]))
            self.caudalop.setText(str(output[3]))
            self.cabezaop.setText(str(output[4]))
            self.marge_npsh.setText(str(output[5]))


    def limpiar(self):
        self.Caudal.setText(' ')
        self.tambiental.setText(' ')
        self.presion.setText(' ')

        self.bomba.setText(' ')
        self.rpm.setText(' ')
        self.diametro.setText(' ')
        self.caudalop.setText(' ')
        self.cabezaop.setText(' ')
        self.marge_npsh.setText(' ')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1171, 661))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(80, 10, 451, 291))
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(570, 0, 571, 351))
        self.label_12.setStyleSheet("image: url(:/plano/plano_red.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 330, 321, 31))
        self.label_5.setObjectName("label_5")
        self.mfuncionamiento = QtWidgets.QSpinBox(self.tab)
        self.mfuncionamiento.setGeometry(QtCore.QRect(330, 330, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mfuncionamiento.setFont(font)
        self.mfuncionamiento.setMinimum(1)
        self.mfuncionamiento.setMaximum(4)
        self.mfuncionamiento.setObjectName("mfuncionamiento")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(390, 330, 41, 31))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 370, 251, 31))
        self.label.setObjectName("label")
        self.Caudal = QtWidgets.QLineEdit(self.tab)
        self.Caudal.setGeometry(QtCore.QRect(10, 410, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Caudal.setFont(font)
        self.Caudal.setObjectName("Caudal")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(130, 400, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 311, 31))
        self.label_4.setObjectName("label_4")
        self.tambiental = QtWidgets.QLineEdit(self.tab)
        self.tambiental.setGeometry(QtCore.QRect(10, 480, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tambiental.setFont(font)
        self.tambiental.setObjectName("tambiental")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(10, 510, 361, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(150, 470, 141, 31))
        self.label_21.setObjectName("label_21")
        self.presion = QtWidgets.QLineEdit(self.tab)
        self.presion.setGeometry(QtCore.QRect(10, 550, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.presion.setFont(font)
        self.presion.setObjectName("presión")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(130, 540, 51, 31))
        self.label_22.setObjectName("label_22")
        self.Calculate = QtWidgets.QPushButton(self.tab)
        self.Calculate.setGeometry(QtCore.QRect(440, 560, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Calculate.setFont(font)
        self.Calculate.setObjectName("Calculate")
        self.Calculate.clicked.connect(self.calcular)  # conectar el funcionamiento del boton a la función main()

        self.Limpiar = QtWidgets.QPushButton(self.tab)
        self.Limpiar.setGeometry(QtCore.QRect(590, 560, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Limpiar.setFont(font)
        self.Limpiar.setObjectName("Limpiar")
        self.Limpiar.clicked.connect(self.limpiar)  # conectar el funcionamiento del boton a la función limpiar()

        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(520, 370, 150, 31))
        self.label_23.setObjectName("label_23")
        self.bomba = QtWidgets.QTextBrowser(self.tab)
        self.bomba.setGeometry(QtCore.QRect(680, 370, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bomba.setFont(font)
        self.bomba.setObjectName("bomba")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(390, 420, 201, 31))
        self.label_24.setObjectName("label_24")
        self.caudalop = QtWidgets.QTextBrowser(self.tab)
        self.caudalop.setGeometry(QtCore.QRect(600, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.caudalop.setFont(font)
        self.caudalop.setObjectName("caudalop")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(690, 420, 141, 31))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(390, 460, 201, 31))
        self.label_26.setObjectName("label_26")
        self.cabezaop = QtWidgets.QTextBrowser(self.tab)
        self.cabezaop.setGeometry(QtCore.QRect(600, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cabezaop.setFont(font)
        self.cabezaop.setObjectName("cabezaop")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(690, 450, 101, 31))
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(450, 500, 141, 31))
        self.label_29.setObjectName("label_29")
        self.marge_npsh = QtWidgets.QTextBrowser(self.tab)
        self.marge_npsh.setGeometry(QtCore.QRect(600, 500, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.marge_npsh.setFont(font)
        self.marge_npsh.setObjectName("marge_npsh")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(690, 490, 101, 31))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(840, 420, 181, 31))
        self.label_31.setObjectName("label_31")
        self.rpm = QtWidgets.QTextBrowser(self.tab)
        self.rpm.setGeometry(QtCore.QRect(1020, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rpm.setFont(font)
        self.rpm.setObjectName("rpm")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(1110, 420, 41, 31))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(830, 460, 201, 31))
        self.label_33.setObjectName("label_33")
        self.diametro = QtWidgets.QTextBrowser(self.tab)
        self.diametro.setGeometry(QtCore.QRect(1030, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diametro.setFont(font)
        self.diametro.setObjectName("diametro")
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(1120, 460, 41, 31))
        self.label_34.setObjectName("label_34")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(150, 20, 801, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(180, 370, 47, 13))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 330, 801, 291))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pump Selection"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Modos de funcionamiento:<br/></span></p><p><span style=\" font-size:12pt;\">1. En serie desde el tanque A pasando por </span></p><p><span style=\" font-size:12pt;\">el tanque 1 y llegando al tanque C.</span></p><p><span style=\" font-size:12pt;\">2. En serie desde el tanque A pasando </span></p><p><span style=\" font-size:12pt;\">por el tanque 2 y llegando a D.</span></p><p><span style=\" font-size:12pt;\">3. En paralelo, ambos tanques funcionando y </span></p><p><span style=\" font-size:12pt;\">retornando a la descarga de la bomba.</span></p><p><span style=\" font-size:12pt;\">4. En paralelo, ambos tanques funcionando y </span></p><p><span style=\" font-size:12pt;\">depositando en los tanques de descarga C y D.</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Eliga el modo de funcionamiento</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">1-4</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Digite el caudal requerido:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">(litros/minuto)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Digite la temperatura ambiental:</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Digite la presión de los tanques 1 y 2:</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">(°C)</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">(psi)</span></p></body></html>"))
        self.Calculate.setText(_translate("MainWindow", "Calcular"))
        self.Limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Bomba elegida:</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Caudal de operación:</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">(litros/minuto)</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Cabeza de operación:</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">(m)</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Margen NPSH:</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">(m)</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Velocidad angular:</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">RPM</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Diámetro del rodete:</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">mm</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Información de las bombas:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Catalogo bombas Zulzer: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">https://www.sulzer.com/-/media/files/products/pumps/single-stage-pumps/brochures/transformeroilcirculationpumpsvmoa_e10121.ashx?la=en</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Catalogo bombas KSB:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">https://shop.ksb.com/ims_docs/00/00215A9B0E3D1EEAA8BCF063AA756417.pdf</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Además, el dashboard adjunto contiene mayor información sobre la base de datos de bombas empleada por el software. </span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Autores</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Julio Barraza Basa       juliojbarraza@mail.uniatlantico.edu.co </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Jehu Luna Arrieta        jehuluna@mail.uniatlantico.edu.co</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Diego Palomino Rodríguez           dcpalomino@mail.uniatlantico.edu.co</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Jhon Serrano Ariza      jhonaserrano@mail.uniatlantico.edu.co</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:16pt;\">Software realizado por estudiantes en el marco del curso Máquinas Hidráulicas 2020-1 de la Universidad del Atlántico. </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Información"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
