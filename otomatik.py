from PyQt5.QtWidgets import *
from PyQt5.uic import *

import sys


class pencere(QDialog):
    def __init__(self):
        super(pencere, self).__init__()
        loadUi("anasayfa.ui", self)


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    arayuz = pencere()
    arayuz.show()
    uygulama.exec()
