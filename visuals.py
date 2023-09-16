import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtGui import QIcon
from configparser import ConfigParser

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize config parser and read existing settings
        self.config = ConfigParser()
        self.config.read('settings.ini')

        # Set initial window size and position based on config values
        self.initUI()

    def initUI(self):
        # Set the dark theme stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2e2e2e;
                border: 1px solid #2e2e2e;
            }
            QMenuBar {
                background-color: #333333;
                color: #ffffff;
            }
            QMenu {
                background-color: #333333;
                color: #ffffff;
                border: 1px solid #555555;
            }
            QMenu::item:selected {
                background-color: #555555;
            }
            QAction {
                color: #ffffff;
            }
        """)

        menubar = self.menuBar()
        
        # Create File menu and add actions
        fileMenu = menubar.addMenu('File')
        
        newAction = QAction('New', self)
        openAction = QAction('Open', self)
        saveAction = QAction('Save', self)
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
        
        # Create Edit menu and add actions
        editMenu = menubar.addMenu('Edit')
        
        undoAction = QAction('Undo', self)
        redoAction = QAction('Redo', self)
        
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)
        
        # Create Help menu and add actions
        helpMenu = menubar.addMenu('Help')
        
        aboutAction = QAction('About', self)
        
        helpMenu.addAction(aboutAction)
        
        # Set main window properties
        self.setWindowTitle('Menu Example')
        self.setWindowIcon(QIcon('assets/logo-tm-wt.png'))
        self.setGeometry(
            int(self.config.get('Settings', 'x', fallback=300)),
            int(self.config.get('Settings', 'y', fallback=300)),
            int(self.config.get('Settings', 'width', fallback=300)),
            int(self.config.get('Settings', 'height', fallback=200))
        )
        
        self.show()

    def closeEvent(self, event):
        # Save settings to config file on close
        if not self.config.has_section('Settings'):
            self.config.add_section('Settings')
        
        self.config.set('Settings', 'x', str(self.x()))
        self.config.set('Settings', 'y', str(self.y()))
        self.config.set('Settings', 'width', str(self.width()))
        self.config.set('Settings', 'height', str(self.height()))

        with open('settings.ini', 'w') as configfile:
            self.config.write(configfile)
        
        event.accept()

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
