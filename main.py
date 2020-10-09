from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from browser_tabbed import *
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # Control to Tabs
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+N'), self)
        self.shortcut_open.activated.connect(self.add_new_tab)
        # self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        # self.shortcut_close.activated.connect(self.close_tabs)
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+S'), self)
        self.shortcut_close.activated.connect(self.save_file)
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_close.activated.connect(self.open_file)

        # Navigation shortcurt
        self.shortcut_close = QShortcut(
            QKeySequence('Ctrl+Z'), self)
        self.shortcut_close.activated.connect(
            lambda: self.tabs.currentWidget().back())
        self.shortcut_close = QShortcut(
            QKeySequence('Ctrl+Shift+Z'), self)
        self.shortcut_close.activated.connect(
            lambda: self.tabs.currentWidget().forward())

        self.setCentralWidget(self.tabs)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navtb = QToolBar("Navegacion")
        navtb.setIconSize(QSize(23, 23))
        self.addToolBar(navtb)

        # Configuration action Widget
        back_btn = QAction(
            QIcon(os.path.join('images', 'arrow-180.png')), "Volver", self)
        back_btn.setStatusTip("Volver a la Pagina anterior")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(
            QIcon(os.path.join('images', 'arrow-000.png')), "Siguiente", self)
        next_btn.setStatusTip("Siguiente Pagina")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(
            QIcon(os.path.join('images', 'arrow-circle-315.png')), "Recargar", self)
        reload_btn.setStatusTip("Recargar Pagina")
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(
            QIcon(os.path.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("IR A Menu")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(
            QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(
            QIcon(os.path.join('images', 'cross-circle.png')), "Parar", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        file_menu = self.menuBar().addMenu("&Archivo")

        new_tab_action = QAction(
            QIcon(os.path.join('images', 'ui-tab--plus.png')), "Nueva ventana", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        file_menu.addAction(new_tab_action)

        open_file_action = QAction(
            QIcon(os.path.join('images', 'disk--arrow.png')), "Abrir Archivos...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(
            QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(
            QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&Ayuda")

        about_action = QAction(QIcon(os.path.join(
            'images', 'question.png')), "About Mozilla ITLA", self)
        about_action.setStatusTip(
            "Find out more about Mozilla ITLA")
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')),
                                            "Mozilla ITLA Homepage", self)
        navigate_mozarella_action.setStatusTip(
            "Go to Mozilla ITLA Homepage")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

        self.show()

        self.setWindowTitle("Mozilla ITLA")
        self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

    # def shortcut():
    #     self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
    #     self.shortcut_open.activated.connect(self.on_open)

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('http://www.google.com')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # if qurl.container(".com"):
        #     browser.setUrl(qurl)
        #     i = self.tabs.addTab(browser, label);
        # if qurl:
        #        browser.setUrl(f'qurl'+'.com')
        #     i = self.tabs.addTab(browser, label)
        # self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))
        # browser.QNetworkReply
        # browser.loadFinished.disconnect(lambda _, i=i, browser=browser:
        #                                 self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    # def close_tabs(self, nub):
    #     self.tabs.removeTab(nub)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - Mozilla ITLA" % title)

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://youtube.com"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir Archivos", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.tabs.currentWidget().setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Guarda Pagina como",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_home(self):

        self.tabs.currentWidget().setUrl(QUrl.fromPercentEncoding("http://www.google.com"))

    # def closeApp(self):
    #     self.tabs. setTabsClosable()
    #     # app.quit()

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('images', 'lock-ssl.png')))

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('images', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


# EJecutacion de la apliacaicon
app = QApplication(sys.argv)
app.setApplicationName("Mozilla ITLA")
app.setOrganizationName("Mozilla ITLA")
app.setOrganizationDomain("Mozilla ITLA")

window = MainWindow()

app.exec_()
