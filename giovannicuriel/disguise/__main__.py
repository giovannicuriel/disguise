"""
Main entry point for disguise application
"""

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


Form, Window = uic.loadUiType('giovannicuriel/disguise/ui/MainWindow.ui')
app = QApplication([])
window = Window()

form = Form()
form.setupUi(window)
form.btnCompile.clicked.connect(on_button_clicked)
window.show()
app.exec_()