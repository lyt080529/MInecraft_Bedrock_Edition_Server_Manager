import os
import sys
import webbrowser as web
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_mcbemanager import Ui_McBeServerManager

class Manager(QMainWindow, Ui_McBeServerManager):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pbtn_st.clicked.connect(self.stserver)
		self.pbtn_lv.clicked.connect(self.leave)
		self.pbtn_sc.clicked.connect(self.command)
		self.Icon.clicked.connect(self.gotoweb)
		self.show()
	def stserver(self):
	    os.system("start.cmd")
	def leave(self):
	    sys.exit()
	def command(self):
		os.system("cmd")
	def gotoweb(self):
		web.open("minecraft.net")
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Manager()
	sys.exit(app.exec_())
