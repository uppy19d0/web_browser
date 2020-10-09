from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Documentacion de Ayudar")
        font = title.font()
        font.setPointSize(30)
        title.setFont(font)

        layout.addWidget(title)

        # logo = QLabel()
        # logo.setPixmap(QPixmap(os.path.join(
        #     'images', 'ma-icon-128.png'), QPixmap(120, 120)))
        # layout.addWidget(logo)

        # layout.addWidget(QLabel("Luis Aneuris Tavarez De Jesus 2018-6927"))
        # layout.addWidget(QLabel("Version 2020"))
        # layout.addWidget(QLabel("Mozilla ITLA."))

        layout.addWidget(QLabel("Como volver a la pagina anterior."))
        layout.addWidget(
            QLabel("Presiones la flecha <= o Presiones la tecla Ctrl + Z"))
        layout.addWidget(QLabel("Como Regresar a la pagina siguiente"))
        layout.addWidget(
            QLabel("Presiones la flecha => o Presiones la tecla Ctrl + Z"))
        layout.addWidget(QLabel("Para guardar Archivos "))
        layout.addWidget(
            QLabel("vaya a archivo y dele a guardar archivo o Presiones la tecla Ctrl + S"))
        layout.addWidget(QLabel("Para Abrir un archivo "))
        layout.addWidget(
            QLabel("Para Abrir un archivo presiones vaya archivo y dele a abrir archivo o presiones Ctrl + O"))
        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)
            layout.addWidget(self.buttonBox)
            self.setLayout(layout)
