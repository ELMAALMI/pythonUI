# importing the required libraries 
import sys 
from PyQt5.QtWidgets import QApplication, QWidget

class Windows (QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("hello 2 ")
		self.setMouseTracking(True)
	def mousePressEvent(self,event):
		print("click one ")
	def mouseMoveEvent(self,event):
		print("X : "+str(event.x()) + " : Y:  " +str(event.y()))
	def mouseDoubleClickEvent(self, a0):
		print("double click")
app = QApplication.instance()
if not app:
	app = QApplication(sys.argv)
fen = Windows()
fen.show()

app.exec_()


