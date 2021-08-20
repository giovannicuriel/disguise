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

flag_values = {}
flag_values[0x0001] = 'CO_OPTIMIZED'
flag_values[0x0002] = 'CO_NEWLOCALS'
flag_values[0x0004] = 'CO_VARARGS'
flag_values[0x0008] = 'CO_VARKEYWORDS'
flag_values[0x0010] = 'CO_NESTED'
flag_values[0x0020] = 'CO_GENERATOR'
flag_values[0x0040] = 'CO_NOFREE'
flag_values[0x0080] = 'CO_COROUTINE'
flag_values[0x0100] = 'CO_ITERABLE_COROUTINE'
flag_values[0x0200] = 'CO_ASYNC_GENERATOR'
flag_values[0x20000] = 'CO_FUTURE_DIVISION'
flag_values[0x40000] = 'CO_FUTURE_ABSOLUTE_IMPORT'
flag_values[0x80000] = 'CO_FUTURE_WITH_STATEMENT'
flag_values[0x100000] = 'CO_FUTURE_PRINT_FUNCTION'
flag_values[0x200000] = 'CO_FUTURE_UNICODE_LITERALS'
flag_values[0x400000] = 'CO_FUTURE_BARRY_AS_BDFL'
flag_values[0x800000] = 'CO_FUTURE_GENERATOR_STOP'
flag_values[0x1000000] = 'CO_FUTURE_ANNOTATIONS'
flag_values[20] = 'CO_MAXBLOCKS'
def flag_to_string(flag): 
  ret = []
  if flag == 0xffffffff:
    return 'CO_CELL_NOT_AN_ARG'
  else:
    for key in flag_values.keys():
      if key & flag:
        ret.append(flag_values[key])
  return ','.join(ret)



def on_button_clicked():
    source_code = form.pteSourceCode.toPlainText()
    disassembly_output = ''
    try:
        compiled_obj = compile(source_code, 'temp', 'exec')
        with open('./output.S', 'w') as output_file:
            dis.dis(compiled_obj, file=output_file, depth=5)
        with open('./output.S', 'r') as output_file:
            disassembly_obj = output_file.read()
        disassembly_obj += f"""\n\n
co_argcount: {compiled_obj.co_argcount}
co_consts: {compiled_obj.co_consts}
co_flags: {flag_to_string(compiled_obj.co_flags)}
co_lnotab: {compiled_obj.co_lnotab}
co_nlocals: {compiled_obj.co_nlocals}
co_cellvars: {compiled_obj.co_cellvars}
co_filename: {compiled_obj.co_filename}
co_freevars: {compiled_obj.co_freevars}
co_name: {compiled_obj.co_name}
co_stacksize: {compiled_obj.co_stacksize}
co_code: {compiled_obj.co_code}
co_firstlineno: {compiled_obj.co_firstlineno}
co_kwonlyargcount: {compiled_obj.co_kwonlyargcount}
co_names: {compiled_obj.co_names}
co_varnames: {compiled_obj.co_varnames}
"""
        form.pteCompiledResults.setPlainText(disassembly_obj)
    except SyntaxError as e:
        form.pteCompiledResults.setPlainText(f"{e}")


form.btnCompile.clicked.connect(on_button_clicked)
window.show()
app.exec_()
