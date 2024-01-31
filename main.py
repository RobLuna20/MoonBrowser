import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        backBtn = QAction("Back", self)
        backBtn.triggered.connect(self.browser.back)
        navbar.addAction(backBtn)

        forwardBtn = QAction("Forward", self)
        forwardBtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardBtn)

        reloadBtn = QAction("Reload", self)
        reloadBtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadBtn)

        homeBtn = QAction("Home", self)
        homeBtn.triggered.connect(self.navigate_home)
        navbar.addAction(homeBtn)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def navigate_to_url(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.urlBar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("AstroMoon")
window = MainWindow()
app.exec_()