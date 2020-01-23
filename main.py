from PyQt5 import QtWidgets, QtCore, QtGui
from renamer_gui import Ui_MainWindow
from os.path import expanduser
import rename.main
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


class MyWindow(Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.files = None

    def setupUi(self, mw):
        super().setupUi(mw)

        # Connect all
        self.reconnect()

        # Hide line's label and line edit
        self.tvshow_label.hide()
        self.tvshow_line.hide()
        self.anime_label.hide()
        self.anime_line.hide()
        self.subtitle_label.hide()
        self.subtitle_line.hide()

        # Hide confirmation, and proceed button
        self.confirmation_button.hide()
        self.proceed_button.hide()

        # Enable clear button in read only mode for directory line edit
        # self.dir_line.findChild(QtWidgets.QToolButton).setEnabled(True)

        # Validate user input
        reg_ex = QtCore.QRegExp(r'[^\/?:*"|<>]*')
        self.tvshow_line.setValidator(QtGui.QRegExpValidator(reg_ex, self.tvshow_line))
        self.anime_line.setValidator(QtGui.QRegExpValidator(reg_ex, self.anime_line))
        self.subtitle_line.setValidator(QtGui.QRegExpValidator(reg_ex, self.subtitle_line))

        # Check confirmation button to rename or cancel
        self.confirmation_button.accepted.connect(lambda: rename.main.renamer(self, self.files))
        self.confirmation_button.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(
            lambda: self.clear_all())

    def reconnect(self):
        # Connect proceed button to start renamer
        self.proceed_button.clicked.connect(lambda: self.script())

        # Connect browse button to open folder browser
        self.browse_button.clicked.connect(lambda: self.browse_dir())

        # Connect checkboxes to display line edit
        self.tvshow_checkbox.clicked.connect(lambda: self.show_editline())
        self.anime_checkbox.clicked.connect(lambda: self.show_editline())
        self.subtitle_checkbox.clicked.connect(lambda: self.show_editline())

        # Connect returnPress for line edit
        self.tvshow_line.returnPressed.connect(lambda: self.visible_editline())
        self.anime_line.returnPressed.connect(lambda: self.visible_editline())
        self.subtitle_line.returnPressed.connect(lambda: self.visible_editline())

        # Hide proceed button when clicked
        self.tvshow_checkbox.clicked.connect(lambda: self.visible_editline(border=False))
        self.anime_checkbox.clicked.connect(lambda: self.visible_editline(border=False))
        self.subtitle_checkbox.clicked.connect(lambda: self.visible_editline(border=False))

        # Connect movie checkbox
        self.movies_checkbox.clicked.connect(lambda: self.movie_checkbox_only())
        self.tvshow_checkbox.clicked.connect(lambda: self.movie_checkbox_only())
        self.anime_checkbox.clicked.connect(lambda: self.movie_checkbox_only())
        self.subtitle_checkbox.clicked.connect(lambda: self.movie_checkbox_only())

        # Clear directory line edit when clicked and open folder browser
        self.dir_line.clicked.connect(self.dir_line.clear)
        self.dir_line.clicked.connect(lambda: self.browse_dir())

    def disconnect(self):
        # Disconnect
        self.dir_line.disconnect()
        self.browse_button.disconnect()

        self.movies_checkbox.disconnect()
        self.tvshow_checkbox.disconnect()
        self.anime_checkbox.disconnect()
        self.subtitle_checkbox.disconnect()

        self.tvshow_line.returnPressed.disconnect()
        self.anime_line.returnPressed.disconnect()
        self.subtitle_line.returnPressed.disconnect()

        self.proceed_button.disconnect()

    def clear_all(self):
        self.files = {}
        self.usr_txt_brwsr.clear()

        self.confirmation_button.hide()

        self.proceed_button.hide()
        self.proceed_button.setEnabled(True)

        self.dir_line.setText('')

        checkedboxes = self.is_checked(return_keys=False)
        for checkbox in checkedboxes:
            checkbox.setChecked(False)
        # Hide all editlines
        self.show_editline()
        # Reconnect all
        self.reconnect()

    def browse_dir(self):
        """Opens folder browser and writes chosen folder location to directory line edit."""
        location = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Select folder",
            expanduser('~'),
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        # Write "location" to line edit
        self.dir_line.setText(location)
        self.location_check_proceed()

    def location_check_proceed(self):
        checked_checkboxes = self.is_checked()

        for checkedbox in checked_checkboxes:
            if checkedbox.lower() == 'movies':
                self.movie_checkbox_only()
            else:
                self.visible_editline(border=False)

    def is_checked(self, return_keys=True):
        """Return checked checkboxes."""
        checkboxes = {
            'Movies': self.movies_checkbox,
            'TV Shows': self.tvshow_checkbox,
            'Animes': self.anime_checkbox,
            'Subtitles': self.subtitle_checkbox,
        }

        checked_checkboxes = []
        for checkbox, line in checkboxes.items():
            if line.isChecked():
                if return_keys:
                    checked_checkboxes.append(checkbox)
                else:
                    checked_checkboxes.append(checkboxes[checkbox])

        return checked_checkboxes

    def movie_checkbox_only(self):
        """Checks if only movie is checked."""
        if self.movies_checkbox.isChecked() and not(self.tvshow_checkbox.isChecked()
                                                    or self.anime_checkbox.isChecked()
                                                    or self.subtitle_checkbox.isChecked()):
            self.show_prcd_btn(True)
        else:
            self.visible_editline(border=False)

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

    def visible_editline(self, border=True, hide_button=True):
        """Checks if name is entered on all visible line edits."""
        visible_editlines = {
            'TV Shows': self.tvshow_line,
            'Animes': self.anime_line,
            'Subtitles': self.subtitle_line,
        }

        # Make copy of dictionary to iterate over and modify
        for item in list(visible_editlines):
            if not visible_editlines[item].isVisible():
                del visible_editlines[item]

        # Hides proceed button
        if hide_button:
            # Show proceed button if text is on all visible line edits
            if visible_editlines:
                line_txt = self.text_in_editline(visible_editlines.values())
                self.show_prcd_btn(line_txt)
            else:
                self.show_prcd_btn(False)

        # Changes line edit border
        if border:
            # Highlight empty line edits
            self.line_border(visible_editlines.values())

        return visible_editlines

    @staticmethod
    def text_in_editline(visible_editlines):
        """Check for text in all visible line edits."""
        for line in visible_editlines:
            if not line.text():
                return False
        return True

    @staticmethod
    def line_border(visible_editlines):
        """Changes the css-style of border for the line edit."""
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
        else:
            self.proceed_button.hide()

    def text_browser_print(self, msg):
        """Print the message to the text browser."""
        self.usr_txt_brwsr.append(msg)

    def get_editline_names(self):
        """get all names from edit line"""
        editlines = self.visible_editline(border=False, hide_button=False)

        for line in editlines:
            editlines[line] = editlines[line].text()

        return editlines

    @staticmethod
    def add_checkedbox_names(new_names, checkedboxes):
        for name in checkedboxes:
            if name not in new_names.keys():
                new_names[name] = None
        return new_names

    def script(self):
        """Start rename script."""
        visible_editlines = self.visible_editline(hide_button=False)
        text_in_visible_editlines = self.text_in_editline(visible_editlines.values())
        if text_in_visible_editlines:
            # Disable proceed button
            self.proceed_button.setDisabled(True)

            # Get rename items
            rename_items = self.add_checkedbox_names(self.get_editline_names(), self.is_checked())

            # Start rename script
            self.files = rename.main.start_main(self, rename_items)

            # show confirm button
            self.confirmation_button.show()

            self.disconnect()


if __name__ == "__main__":
    # # Back up the reference to the exceptionhook
    # sys._excepthook = sys.excepthook
    #
    # def my_exception_hook(exctype, value, traceback):
    #     # Print the error and traceback
    #     print(exctype, value, traceback)
    #     # Call the normal Exception hook after
    #     sys._excepthook(exctype, value, traceback)
    #     sys.exit(1)
    #
    # # Set the exception hook to our wrapping function
    # sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
