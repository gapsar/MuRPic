from PyQt5.QtWidgets import QHBoxLayout, QWidget
from picamera2.previews.qt import QGlPicamera2

# The class for the Preview window
class PreviewWindow(QWidget):
	def __init__(self, picam2):
		super(PreviewWindow, self).__init__()
		self.picam2 = picam2
		self.qpicamera2 = QGlPicamera2(self.picam2, width=800, height=480, keep_ar=False)
		self.layout_h = QHBoxLayout()
		self.layout_h.addWidget(self.qpicamera2)  # Add QGlPicamera2 to the layout
		self.setLayout(self.layout_h)
