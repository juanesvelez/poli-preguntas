# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class LoginRegisterForm(object):
    def setupUi(self, LoginRegisterForm):
        if not LoginRegisterForm.objectName():
            LoginRegisterForm.setObjectName(u"LoginRegisterForm")
        LoginRegisterForm.resize(506, 382)
        LoginRegisterForm.setAutoFillBackground(False)
        self.lbl_jugador = QLabel(LoginRegisterForm)
        self.lbl_jugador.setObjectName(u"lbl_jugador")
        self.lbl_jugador.setGeometry(QRect(40, 110, 221, 31))
        font = QFont()
        font.setPointSize(14)
        self.lbl_jugador.setFont(font)
        self.lbl_edad = QLabel(LoginRegisterForm)
        self.lbl_edad.setObjectName(u"lbl_edad")
        self.lbl_edad.setGeometry(QRect(40, 200, 221, 31))
        self.lbl_edad.setFont(font)
        self.frame_login = QFrame(LoginRegisterForm)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setGeometry(QRect(-210, -150, 921, 641))
        self.frame_login.setStyleSheet(u"image: url(./assets/img/fondo_login.png);")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.btn_jugar = QPushButton(LoginRegisterForm)
        self.btn_jugar.setObjectName(u"btn_jugar")
        self.btn_jugar.setGeometry(QRect(40, 300, 111, 41))
        self.btn_jugar.setFont(font)
        self.btn_jugar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jugar.setMouseTracking(False)
        self.btn_jugar.setFocusPolicy(Qt.WheelFocus)
        self.btn_jugar.setLayoutDirection(Qt.RightToLeft)
        self.btn_jugar.setAutoFillBackground(False)
        self.btn_jugar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"./assets/icon/icon_jugar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jugar.setIcon(icon)
        self.btn_jugar.setIconSize(QSize(30, 30))
        self.btn_jugar.setCheckable(False)
        self.btn_jugar.setAutoExclusive(False)
        self.btn_jugar.setAutoDefault(False)
        self.btn_jugar.setFlat(False)
        val_edad = QIntValidator(1, 99, self)
        self.txt_edad = QLineEdit(LoginRegisterForm)
        self.txt_edad.setValidator(val_edad)
        self.txt_edad.setObjectName(u"txt_edad")
        self.txt_edad.setGeometry(QRect(40, 240, 221, 31))
        self.txt_edad.setFont(font)
        self.txt_edad.setFocusPolicy(Qt.StrongFocus)
        self.txt_jugador = QLineEdit(LoginRegisterForm)
        self.txt_jugador.setObjectName(u"txt_jugador")
        self.txt_jugador.setGeometry(QRect(40, 150, 221, 31))
        self.txt_jugador.setFont(font)
        self.txt_jugador.setFocusPolicy(Qt.StrongFocus)
        self.txt_jugador.setFrame(True)
        self.lbl_titulo = QLabel(LoginRegisterForm)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(40, 60, 191, 31))
        self.frame_login.raise_()
        self.lbl_jugador.raise_()
        self.lbl_edad.raise_()
        self.btn_jugar.raise_()
        self.txt_edad.raise_()
        self.txt_jugador.raise_()
        self.lbl_titulo.raise_()
        QWidget.setTabOrder(self.txt_jugador, self.txt_edad)
        QWidget.setTabOrder(self.txt_edad, self.btn_jugar)

        self.retranslateUi(LoginRegisterForm)

        QMetaObject.connectSlotsByName(LoginRegisterForm)
    # setupUi

    def retranslateUi(self, LoginRegisterForm):
        LoginRegisterForm.setWindowTitle(QCoreApplication.translate("LoginRegisterForm", u"Poli-Preguntas Register", None))
        self.lbl_jugador.setText(QCoreApplication.translate("LoginRegisterForm", u"<html><head/><body><p><span style=\" color:#000000;\">Nombre</span></p></body></html>", None))
        self.lbl_edad.setText(QCoreApplication.translate("LoginRegisterForm", u"<html><head/><body><p><span style=\" color:#000000;\">Edad</span></p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.btn_jugar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_jugar.setText(QCoreApplication.translate("LoginRegisterForm", u"Jugar ", None))
        self.lbl_titulo.setText(QCoreApplication.translate("LoginRegisterForm", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Poli Preguntas</span></p></body></html>", None))
    # retranslateUi

