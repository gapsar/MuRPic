from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget

class GUIManager:
	def __init__(self):
		self.app = QApplication([])
		self.stacked_widget = QStackedWidget()
		
	def add_widget(self, widget, name):
		self.stacked_widget.addWidget(widget)
		self.stacked_widget.setObjectName(name)
	
	def set_current_widget(self, index):
		self.stacked_widget.setCurrentIndex(index)
		
	def show(self):
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.stacked_widget)
		self.main_widget = QWidget()
		self.main_widget.setLayout(self.layout)
		self.main_widget.setWindowTitle("µRPic")
		self.main_widget.showFullScreen()
		self.app.exec()
