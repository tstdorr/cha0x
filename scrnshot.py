import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class Screenshot(QWebEngineView):
    app = QApplication(sys.argv)
    s = Screenshot()
    s.app = app
    def capture(self, url, output_file):
        self.output_file = output_file
        self.load(QUrl(url))
        self.loadFinished.connect(self.on_loaded)
        # Create hidden view without scrollbars
        self.setAttribute(Qt.WA_DontShowOnScreen)
        self.page().settings().setAttribute(
            QWebEngineSettings.ShowScrollBars, False)
        self.show()

    def on_loaded(self):
        size = self.page().contentsSize().toSize()
        self.resize(1920,1080)
        # Wait for resize
        QTimer.singleShot(1000, self.take_screenshot)

    def take_screenshot(self):
        self.grab().save(self.output_file, b'PNG')
        self.app.quit()


file_name = '/home/Arch0/Documents/lern/URLss.txt'
fopen=open(file_name, 'r')
def main():
    file_name = '/home/Arch0/Documents/lern/URLss.txt'
    fopen=open(file_name, 'r')
    for x in fopen.readlines():
        a=1
        a=a+1
        url = x.strip('\n')

        s.capture(url, '%s.png' %a)
        fopen.close()
if __name__ == '__main__':
    main()
sys.exit(app.exec_())
