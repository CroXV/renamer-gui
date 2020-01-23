# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renamegui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dir_label = QtWidgets.QLabel(self.centralwidget)
        self.dir_label.setObjectName("dir_label")
        self.horizontalLayout_4.addWidget(self.dir_label)
        self.dir_line = ClickableLineEdit(self.centralwidget)
        self.dir_line.setFrame(True)
        self.dir_line.setDragEnabled(False)
        self.dir_line.setReadOnly(True)
        self.dir_line.setClearButtonEnabled(False)
        self.dir_line.setObjectName("dir_line")
        self.horizontalLayout_4.addWidget(self.dir_line)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout_4.addWidget(self.browse_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tvshow_label = QtWidgets.QLabel(self.centralwidget)
        self.tvshow_label.setObjectName("tvshow_label")
        self.horizontalLayout_3.addWidget(self.tvshow_label)
        self.tvshow_line = QtWidgets.QLineEdit(self.centralwidget)
        self.tvshow_line.setToolTipDuration(-1)
        self.tvshow_line.setFrame(True)
        self.tvshow_line.setDragEnabled(False)
        self.tvshow_line.setObjectName("tvshow_line")
        self.horizontalLayout_3.addWidget(self.tvshow_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(21)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.anime_label = QtWidgets.QLabel(self.centralwidget)
        self.anime_label.setObjectName("anime_label")
        self.horizontalLayout_2.addWidget(self.anime_label)
        self.anime_line = QtWidgets.QLineEdit(self.centralwidget)
        self.anime_line.setToolTipDuration(-1)
        self.anime_line.setFrame(True)
        self.anime_line.setDragEnabled(False)
        self.anime_line.setObjectName("anime_line")
        self.horizontalLayout_2.addWidget(self.anime_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(14)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.subtitle_label = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_label.setObjectName("subtitle_label")
        self.horizontalLayout_5.addWidget(self.subtitle_label)
        self.subtitle_line = QtWidgets.QLineEdit(self.centralwidget)
        self.subtitle_line.setToolTipDuration(-1)
        self.subtitle_line.setFrame(True)
        self.subtitle_line.setDragEnabled(False)
        self.subtitle_line.setObjectName("subtitle_line")
        self.horizontalLayout_5.addWidget(self.subtitle_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.movies_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.movies_checkbox.setObjectName("movies_checkbox")
        self.verticalLayout.addWidget(self.movies_checkbox)
        self.tvshow_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.tvshow_checkbox.setObjectName("tvshow_checkbox")
        self.verticalLayout.addWidget(self.tvshow_checkbox)
        self.anime_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.anime_checkbox.setObjectName("anime_checkbox")
        self.verticalLayout.addWidget(self.anime_checkbox)
        self.subtitle_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.subtitle_checkbox.setFont(font)
        self.subtitle_checkbox.setObjectName("subtitle_checkbox")
        self.verticalLayout.addWidget(self.subtitle_checkbox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.proceed_button = QtWidgets.QPushButton(self.centralwidget)
        self.proceed_button.setObjectName("proceed_button")
        self.verticalLayout.addWidget(self.proceed_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.usr_txt_brwsr = QtWidgets.QTextBrowser(self.centralwidget)
        self.usr_txt_brwsr.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.usr_txt_brwsr.setObjectName("usr_txt_brwsr")
        self.horizontalLayout.addWidget(self.usr_txt_brwsr)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(336, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.confirmation_button = QtWidgets.QDialogButtonBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmation_button.sizePolicy().hasHeightForWidth())
        self.confirmation_button.setSizePolicy(sizePolicy)
        self.confirmation_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.confirmation_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.confirmation_button.setObjectName("confirmation_button")
        self.horizontalLayout_6.addWidget(self.confirmation_button)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Renamer"))
        self.dir_label.setText(_translate("MainWindow", "Folder"))
        self.dir_line.setPlaceholderText(_translate("MainWindow", "Browse Folder Location"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.tvshow_label.setText(_translate("MainWindow", "TV Show"))
        self.tvshow_line.setPlaceholderText(_translate("MainWindow", "Enter New Name"))
        self.anime_label.setText(_translate("MainWindow", "Anime"))
        self.anime_line.setPlaceholderText(_translate("MainWindow", "Enter New Name"))
        self.subtitle_label.setText(_translate("MainWindow", "Subtitle"))
        self.subtitle_line.setPlaceholderText(_translate("MainWindow", "Enter New Name"))
        self.movies_checkbox.setText(_translate("MainWindow", "Movies"))
        self.tvshow_checkbox.setText(_translate("MainWindow", "TV Shows"))
        self.anime_checkbox.setText(_translate("MainWindow", "Anime"))
        self.subtitle_checkbox.setText(_translate("MainWindow", "Subtitles"))
        self.proceed_button.setText(_translate("MainWindow", "Proceed"))
from clickable_line_edit import ClickableLineEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
