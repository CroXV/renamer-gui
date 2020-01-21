from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QRegExpValidator
from renamer_gui import Ui_MainWindow
from os.path import expanduser
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


class MyWindow(Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

    def setupUi(self, mw):
        super().setupUi(mw)

        # Connect proceed button to start renamer
        self.proceed_button.clicked.connect(lambda: self.renamer())

        # Connect browse button to open folder browser
        self.browse_button.clicked.connect(lambda: self.browse_dir())

        # Connect checkboxes to display line edit
        self.tvshow_checkbox.clicked.connect(lambda: self.show_editline())
        self.anime_checkbox.clicked.connect(lambda: self.show_editline())
        self.subtitle_checkbox.clicked.connect(lambda: self.show_editline())

        # Connect movie checkbox
        self.movies_checkbox.clicked.connect(lambda: self.movie_checkbox_only())
        self.tvshow_checkbox.clicked.connect(lambda: self.movie_checkbox_only())
        self.anime_checkbox.clicked.connect(lambda: self.movie_checkbox_only())
        self.subtitle_checkbox.clicked.connect(lambda: self.movie_checkbox_only())

        # Connect returnPress for line edit
        self.tvshow_line.returnPressed.connect(lambda: self.name_on_visible_editline())
        self.anime_line.returnPressed.connect(lambda: self.name_on_visible_editline())
        self.subtitle_line.returnPressed.connect(lambda: self.name_on_visible_editline())

        # Hide proceed button when clicked
        self.tvshow_checkbox.clicked.connect(lambda: self.name_on_visible_editline(border=False))
        self.anime_checkbox.clicked.connect(lambda: self.name_on_visible_editline(border=False))
        self.subtitle_checkbox.clicked.connect(lambda: self.name_on_visible_editline(border=False))

        # Hide line label and line edit
        self.tvshow_label.hide()
        self.tvshow_line.hide()
        self.anime_label.hide()
        self.anime_line.hide()
        self.subtitle_label.hide()
        self.subtitle_line.hide()

        # Hide confirmation, and proceed button
        self.confirmation_button.hide()
        self.proceed_button.hide()

        # Clear dir line if clicked and open folder browser
        self.dir_line.clicked.connect(self.dir_line.clear)
        self.dir_line.clicked.connect(lambda: self.browse_dir())

        # Enable clear button in read only mode for "dir_line"
        # self.dir_line.findChild(QtWidgets.QToolButton).setEnabled(True)

        # Validate user input
        reg_ex = QtCore.QRegExp(r'[^\/?:*"|<>]*')
        self.tvshow_line.setValidator(QRegExpValidator(reg_ex, self.tvshow_line))
        self.anime_line.setValidator(QRegExpValidator(reg_ex, self.anime_line))
        self.subtitle_line.setValidator(QRegExpValidator(reg_ex, self.subtitle_line))

    def browse_dir(self):
        """Opens folder browser and writes chosen folder location to directory line edit."""
        location = QFileDialog.getExistingDirectory(
            None,
            "Select folder",
            expanduser('~'),
            QFileDialog.ShowDirsOnly
        )

        # Write "location" to line edit
        self.dir_line.setText(location)
        self.location_check_proceed()

    def location_check_proceed(self):
        checkboxes_checked = {
            'movie': self.movies_checkbox.isChecked(),
            'tvshow': self.tvshow_checkbox.isChecked(),
            'anime': self.anime_checkbox.isChecked(),
            'sub': self.subtitle_checkbox.isChecked(),
        }

        for checkbox, checked in checkboxes_checked.items():
            if checkbox == 'movie' and checked:
                self.movie_checkbox_only()
            elif checked:
                self.name_on_visible_editline(border=False)

    def movie_checkbox_only(self):
        """Checks if only movie is checked."""
        if self.movies_checkbox.isChecked() and not(self.tvshow_checkbox.isChecked()
                                                    or self.anime_checkbox.isChecked()
                                                    or self.subtitle_checkbox.isChecked()):
            self.show_prcd_btn(True)
        else:
            self.show_prcd_btn(False)

    def show_editline(self):
        """Shows and hides the label name and line edit."""
        checkboxes = {
            self.tvshow_checkbox: [self.tvshow_label, self.tvshow_line],
            self.anime_checkbox: [self.anime_label, self.anime_line],
            self.subtitle_checkbox: [self.subtitle_label, self.subtitle_line],
        }

        for checkbox, editline_items in checkboxes.items():
            if checkbox.isChecked():
                editline_items[0].show()
                editline_items[1].show()
            else:
                editline_items[0].hide()
                editline_items[1].hide()

                # Clears line edit's style sheet and text when unchecked
                editline_items[1].setText('')
                editline_items[1].setStyleSheet('')

    def name_on_visible_editline(self, border=True, hide_button=True):
        """Checks if name is entered on all visible line edits."""
        editlines = [self.tvshow_line, self.anime_line, self.subtitle_line]

        # find all visible line edits
        visible_editlines = []
        for line in editlines:
            if line.isVisible():
                visible_editlines.append(line)

        # Hides proceed button, if true
        if hide_button:
            # Show proceed button if text on visible line edits
            has_line_txt = self.txt_in_editline(visible_editlines)
            self.show_prcd_btn(has_line_txt)

        # Highlights line edit borders, if true
        if border:
            # Highlight empty line edits
            self.line_border(visible_editlines)

    @staticmethod
    def txt_in_editline(visible_editlines):
        """Check for text in all visible line edits."""
        for line in visible_editlines:
            if not line.text():
                return False
        return True

    @staticmethod
    def line_border(visible_editlines):
        """Changes the css-style(border) for the line edit."""
        for line in visible_editlines:
            if line.text():
                line.setStyleSheet('')
            else:
                line.setStyleSheet('border: 1.5px solid red;')

    def show_prcd_btn(self, show):
        """Shows and hides the proceed button."""
        if os.path.isdir(self.dir_line.text()):
            if show:
                self.proceed_button.show()
            else:
                self.proceed_button.hide()

    def renamer(self):
        """Read location and start rename script."""
        # Read dir location and new name on line edit
        print('here')
        print(self.name_on_visible_editline(hide_button=False))

        # TODO: Start rename script

    # TODO: Write to usr txt brwsr
    # TODO: Check confirmation button to cancel or rename


if __name__ == "__main__":
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
