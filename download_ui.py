# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created: Sun Apr 24 13:16:24 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot

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

class Ui_Download(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 484)
        Dialog.setWindowOpacity(0.9)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.albumCover = QtGui.QFrame(self.frame)
        self.albumCover.setSizeIncrement(QtCore.QSize(1, 1))
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
        self.overAllProgress.setMinimum(0)
        self.overAllProgress.setMaximum(100)
        self.verticalLayout_4.addWidget(self.overAllProgress)
        self.verticalLayout_5.addWidget(self.overAllGroup)
        self.playlistGroup = QtGui.QGroupBox(Dialog)
        self.playlistGroup.setObjectName(_fromUtf8("playlistGroup"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.playlistGroup)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.playlistStatus = QtGui.QLabel(self.playlistGroup)
        self.playlistStatus.setObjectName(_fromUtf8("playlistStatus"))
        self.verticalLayout_3.addWidget(self.playlistStatus)
        self.PlaylistProgress = QtGui.QProgressBar(self.playlistGroup)
        self.PlaylistProgress.setProperty("value", 24)
        self.PlaylistProgress.setMinimum(0)
        self.PlaylistProgress.setMaximum(100)
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
        self.songProgress.setMinimum(0)
        self.songProgress.setMaximum(100)
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

    def set_overall_progress(self, progress):
        self.overAllProgress.setValue(progress)

    def set_song_progress(self, progress):
        self.songProgress.setValue(progress)

    def set_playlist_progress(self, progress):
        self.PlaylistProgress.setValue(progress)

    def set_overall_label(self, text):
        self.pllaylistsBox.setText(text)

    def set_playlist_label(self, text):
        self.playlistStatus.setText(text)

    def set_downloading_label(self, text):
        self.songStatus.setText("Downloading: " + text)

    def set_song_name(self, text):
        self.songLabel.setText(str(text))

    def set_album_name(self, text):
        self.albumLabel.setText(str(text))

    def set_artist_name(self, text):
        self.artistLabel.setText(str(text))

    def set_genre_name(self, text):
        self.songNumberLabel.setText(str(text))

    @pyqtSlot()
    def cancel_download(self):
        exit(0) #FIXME: end download not app!
    

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
        self.playlistStatus.setText(_translate("Dialog", "(1/3) songs", None))
        self.songGroup.setTitle(_translate("Dialog", "song", None))
        self.songStatus.setText(_translate("Dialog", "downloading song", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Download()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

