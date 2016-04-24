# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Apr 22 14:44:31 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot

from gmusicapi import Mobileclient
import config
import download_helper as dwn_helper
conf = config.config()
working_device_id = conf.get_device_id()
del conf


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
    #custom functions start here
    def load_playlist(self):
        pass
    def load_playlist_list(self):
        #FIXME: this is really poorly written and memory intensive
        playlists = self.api.get_all_user_playlist_contents()
        model = QtGui.QStandardItemModel()
        self.playlistIds = []
        for playlist in playlists:                   
            item = QtGui.QStandardItem(playlist['name']) #% playlist['shareToken']
            self.playlistIds.append(playlist['name'])
            #TODO: .setIcon(some_QIcon)
            item.setCheckable(True)
            model.appendRow(item)
        #model.itemChanged.connect(on_item_changed) #TODO disable and enable download based on click
        self.playlistListWid = QtGui.QListView()
        self.playlistListWid.setObjectName(_fromUtf8("playlistView"))
        self.playlistListWid.setModel(model)
        self.playlistListWid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.verticalLayout_3.addWidget(self.playlistListWid)
        self.playlistListWid.show()

    @pyqtSlot()
    def select_all(self):
        model = self.playlistListWid.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)

    #NOT IMPLEMENTED
    def deselect_all(self):
        model = self.playlistListWid.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)

    @pyqtSlot()
    def begin_download(self):
        model = self.playlistListWid.model()
        pnames = [] #stores names of selected playlists
        #FIXME: MASSIVE ERROR: cannot support more than one playlists with the same name
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                pnames.append(self.playlistIds[index])
        dwn_helper.attempt_download(self.api, pnames, self.dialog) #start download (hopefully)
            

    
    @pyqtSlot()
    def playlists_back(self):
        if(self.isPlaylistSelected):
            pass
        else:
            self.backButton.hide()
            self.load_playlist_list()

    def __init__(self, dialog):
        self.dialog=dialog
        api = Mobileclient()

        logged_in = False
        attempts = 0

        while not logged_in and attempts < 3:
            conf = config.config()
            
            email = conf.get_email()#raw_input('Email: ')
            password = conf.get_password() #get_pass()

            logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
            attempts += 1

        self.api = api
        if not api.is_authenticated():
            print "Sorry, those credentials weren't accepted."
            message.set("Sorry, those credentials weren't accepted.")
            return
        print 'Successfully logged in.'
        print
    
    def setupUi(self, MainWindow):
        self.isPlaylistSelected=False
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.playlistTab = QtGui.QTabWidget(self.centralwidget)
        self.playlistTab.setObjectName(_fromUtf8("playlistTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.backButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.backButton.clicked.connect(self.playlists_back)
        self.verticalLayout_2.addWidget(self.backButton)
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 453))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.playlistname = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistname.sizePolicy().hasHeightForWidth())
        self.playlistname.setSizePolicy(sizePolicy)
        self.playlistname.setObjectName(_fromUtf8("playlistname"))
        self.verticalLayout_3.addWidget(self.playlistname)
        self.playlistentries = QtGui.QVBoxLayout()
        self.playlistentries.setObjectName(_fromUtf8("playlistentries"))
        playlistEntries = self.playlistentries
        self.verticalLayout_3.addLayout(self.playlistentries)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.playlistTab.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.playlistTab)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout.addWidget(self.downloadButton)
        self.downloadButton.clicked.connect(self.begin_download)
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        self.selectButton = QtGui.QPushButton(self.centralwidget)
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.selectButton.clicked.connect(self.select_all)
        self.horizontalLayout.addWidget(self.selectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAlbum = QtGui.QMenu(self.menubar)
        self.menuAlbum.setObjectName(_fromUtf8("menuAlbum"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionBy_album = QtGui.QAction(MainWindow)
        self.actionBy_album.setObjectName(_fromUtf8("actionBy_album"))
        self.actionBy_artist = QtGui.QAction(MainWindow)
        self.actionBy_artist.setObjectName(_fromUtf8("actionBy_artist"))
        self.actionBy_genre = QtGui.QAction(MainWindow)
        self.actionBy_genre.setObjectName(_fromUtf8("actionBy_genre"))
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionComing_soon = QtGui.QAction(MainWindow)
        self.actionComing_soon.setObjectName(_fromUtf8("actionComing_soon"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionComing_soon)
        self.menuAlbum.addAction(self.actionBy_album)
        self.menuAlbum.addAction(self.actionBy_artist)
        self.menuAlbum.addAction(self.actionBy_genre)
        self.menuAlbum.addSeparator()
        self.menuAlbum.addAction(self.actionSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAlbum.menuAction())

        self.playlists_back()

        self.retranslateUi(MainWindow)
        self.playlistTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.backButton.setText(_translate("MainWindow", "back", None))
        self.playlistname.setText(_translate("MainWindow", "playlist name", None))
        self.playlistTab.setTabText(self.playlistTab.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.downloadButton.setText(_translate("MainWindow", "download", None))
        self.deleteButton.setText(_translate("MainWindow", "delete", None))
        self.playButton.setText(_translate("MainWindow", "play", None))
        self.searchButton.setText(_translate("MainWindow", "search", None))
        self.selectButton.setText(_translate("MainWindow", "select all", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.menuAlbum.setTitle(_translate("MainWindow", "get", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))
        self.actionSettings.setText(_translate("MainWindow", "settings", None))
        self.actionQuit.setText(_translate("MainWindow", "quit", None))
        self.actionBy_album.setText(_translate("MainWindow", "by album", None))
        self.actionBy_artist.setText(_translate("MainWindow", "by artist", None))
        self.actionBy_genre.setText(_translate("MainWindow", "by genre", None))
        self.actionSearch.setText(_translate("MainWindow", "search", None))
        self.actionComing_soon.setText(_translate("MainWindow", "coming soon", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    MainWindow = QtGui.QMainWindow() #pass the dialog object because it has to be this way for some reason
    ui = Ui_MainWindow(dialog)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

