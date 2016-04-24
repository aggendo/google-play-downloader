# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created: Thu Apr 21 17:27:43 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 484)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.albumCover = QtGui.QFrame(self.frame)
        self.albumCover.setFrameShape(QtGui.QFrame.NoFrame)
        self.albumCover.setFrameShadow(QtGui.QFrame.Plain)
        self.albumCover.setObjectName(_fromUtf8("albumCover"))
        self.horizontalLayout.addWidget(self.albumCover)
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.artistLabel = QtGui.QLabel(self.groupBox)
        self.artistLabel.setObjectName(_fromUtf8("artistLabel"))
        self.verticalLayout.addWidget(self.artistLabel)
        self.albumLabel = QtGui.QLabel(self.groupBox)
        self.albumLabel.setObjectName(_fromUtf8("albumLabel"))
        self.verticalLayout.addWidget(self.albumLabel)
        self.songLabel = QtGui.QLabel(self.groupBox)
        self.songLabel.setObjectName(_fromUtf8("songLabel"))
        self.verticalLayout.addWidget(self.songLabel)
        self.songNumberLabel = QtGui.QLabel(self.groupBox)
        self.songNumberLabel.setObjectName(_fromUtf8("songNumberLabel"))
        self.verticalLayout.addWidget(self.songNumberLabel)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_5.addWidget(self.frame)
        self.overAllGroup = QtGui.QGroupBox(Dialog)
        self.overAllGroup.setObjectName(_fromUtf8("overAllGroup"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.overAllGroup)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pllaylistsBox = QtGui.QLabel(self.overAllGroup)
        self.pllaylistsBox.setObjectName(_fromUtf8("pllaylistsBox"))
        self.verticalLayout_4.addWidget(self.pllaylistsBox)
        self.overAllProgress = QtGui.QProgressBar(self.overAllGroup)
        self.overAllProgress.setProperty("value", 24)
        self.overAllProgress.setObjectName(_fromUtf8("overAllProgress"))
        self.verticalLayout_4.addWidget(self.overAllProgress)
        self.verticalLayout_5.addWidget(self.overAllGroup)
        self.playlistGroup = QtGui.QGroupBox(Dialog)
        self.playlistGroup.setObjectName(_fromUtf8("playlistGroup"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.playlistGroup)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.songsStatus = QtGui.QLabel(self.playlistGroup)
        self.songsStatus.setObjectName(_fromUtf8("songsStatus"))
        self.verticalLayout_3.addWidget(self.songsStatus)
        self.PlaylistProgress = QtGui.QProgressBar(self.playlistGroup)
        self.PlaylistProgress.setProperty("value", 24)
        self.PlaylistProgress.setObjectName(_fromUtf8("PlaylistProgress"))
        self.verticalLayout_3.addWidget(self.PlaylistProgress)
        self.verticalLayout_5.addWidget(self.playlistGroup)
        self.songGroup = QtGui.QGroupBox(Dialog)
        self.songGroup.setObjectName(_fromUtf8("songGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.songGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.songStatus = QtGui.QLabel(self.songGroup)
        self.songStatus.setObjectName(_fromUtf8("songStatus"))
        self.verticalLayout_2.addWidget(self.songStatus)
        self.songProgress = QtGui.QProgressBar(self.songGroup)
        self.songProgress.setProperty("value", 24)
        self.songProgress.setObjectName(_fromUtf8("songProgress"))
        self.verticalLayout_2.addWidget(self.songProgress)
        self.verticalLayout_5.addWidget(self.songGroup)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "metadata", None))
        self.artistLabel.setText(_translate("Dialog", "artist", None))
        self.albumLabel.setText(_translate("Dialog", "album", None))
        self.songLabel.setText(_translate("Dialog", "song", None))
        self.songNumberLabel.setText(_translate("Dialog", "song number", None))
        self.overAllGroup.setTitle(_translate("Dialog", "overall", None))
        self.pllaylistsBox.setText(_translate("Dialog", "(1/3) Playlists", None))
        self.playlistGroup.setTitle(_translate("Dialog", "playlist", None))
        self.songsStatus.setText(_translate("Dialog", "(1/3) songs", None))
        self.songGroup.setTitle(_translate("Dialog", "song", None))
        self.songStatus.setText(_translate("Dialog", "downloading song", None))

