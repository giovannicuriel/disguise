"""
Main entry point for disguise application
"""

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import dis

Form, Window = uic.loadUiType('giovannicuriel/disguise/ui/MainWindow.ui')
app = QApplication([])
window = Window()

form = Form()
form.setupUi(window)

def on_button_clicked():
    source_code = form.pteSourceCode.toPlainText()
    try:
        compiled_obj = compile(source_code, 'temp', 'exec')
        with open('./output.S', 'w') as output_file:
            dis.dis(compiled_obj, file=output_file)
        with open('./output.S', 'r') as output_file:
            disassembly_obj = output_file.read()
            form.pteCompiledResults.setPlainText(disassembly_obj)
    except SyntaxError as e:
        form.pteCompiledResults.setPlainText(f"{e}")


form.btnCompile.clicked.connect(on_button_clicked)
window.show()
app.exec_()
