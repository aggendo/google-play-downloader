from PyQt4 import QtCore, QtGui

import main as main

def playlists_home(ui):
    ui.backButton().hide()

import sys
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = main.Ui_MainWindow()
ui.backButton().connect(playlists_home)
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
