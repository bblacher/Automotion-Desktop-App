from csv import reader
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from GUI.win_main import Ui_win_main

windowtitle = "RC-Car Viewer"


class WinMain(QMainWindow, Ui_win_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(windowtitle)
        self.actionBeenden.triggered.connect(self.close)
        self.action_ffnen.triggered.connect(self.openfile)
        self.actionVollbild.triggered.connect(self.toggle_fullscreen)
        self.actionOverview.triggered.connect(lambda: self.pageswitcher.setCurrentIndex(0))
        self.actionTable_View.triggered.connect(lambda: self.pageswitcher.setCurrentIndex(1))

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def openfile(self):
        filepath = QFileDialog.getOpenFileName(self, self.tr("Open Data"), "/home", self.tr("*.txt *.csv"))
        try:
            datafile = open(filepath[0], 'r')
            data = list(reader(datafile))
        except:
            print("Error reading file (No File selected?)")


desktop_app = QApplication()
win_main = WinMain()
win_main.show()
desktop_app.exec()
