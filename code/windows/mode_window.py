from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import pyqtSignal

# The class for the window allowing to change modes
class ModeChoice(QWidget):
	mode_changed = pyqtSignal(str)  # Define a custom signal that takes a string argument
	def __init__(self):
		super(ModeChoice, self).__init__()
		# We create the layout
		self.layout = QGridLayout()
		self.setStyleSheet("QPushButton { background: transparent; width: 90px; height: 95px; border: 1px solid transparent; border-radius: 20px;}")
		# We define each button
		self.button_photo = QPushButton(objectName='button_photo', clicked=lambda: self.change_mode("Photo_Mode"))
		self.button_video = QPushButton(objectName='button_video', clicked=lambda: self.change_mode("Video_Mode"))
		self.button_night = QPushButton(objectName='button_night', clicked=lambda: self.change_mode("Night_Mode"))
		self.button_pano = QPushButton(objectName='button_pano', clicked=lambda: self.change_mode("Pano_Mode"))
		self.button_timelapse = QPushButton(objectName='button_timelapse', clicked=lambda: self.change_mode("Timelapse_Mode"))
		self.button_slowmo = QPushButton(objectName='button_slowmo', clicked=lambda: self.change_mode("Slowmo_Mode"))
		self.button_expos = QPushButton(objectName='button_expos', clicked=lambda: self.change_mode("Expos_Mode"))
		self.button_astro = QPushButton(objectName='button_astro', clicked=lambda: self.change_mode("Astro_Mode"))
		self.button_stabilized = QPushButton(objectName='button_stabilized', clicked=lambda: self.change_mode("Stabilized_Mode"))
		self.button_face_reco = QPushButton(objectName='button_face_reco', clicked=lambda: self.change_mode("Facereco_Mode"))
		self.button_pose_reco = QPushButton(objectName='button_pose_reco', clicked=lambda: self.change_mode("Posereco_Mode"))
		self.button_hand_reco = QPushButton(objectName='button_hand_reco', clicked=lambda: self.change_mode("Handreco_Mode"))
		self.button_controlled = QPushButton(objectName='button_controlled', clicked=lambda: self.change_mode("Algorithmic_Mode"))
		self.button_star_positioning = QPushButton(objectName='button_star_positioning', clicked=lambda: self.change_mode("Starpos_Mode"))
		self.button_motion_detect = QPushButton(objectName='button_motion_detect', clicked=lambda: self.change_mode("Motiondetect_Mode"))
		# Now we add them to the layout
		self.layout.addWidget(self.button_photo, 0, 0)
		self.layout.addWidget(self.button_video, 1, 0)
		self.layout.addWidget(self.button_night, 2, 0)
		self.layout.addWidget(self.button_pano, 0, 1)
		self.layout.addWidget(self.button_timelapse, 1, 1)
		self.layout.addWidget(self.button_slowmo, 2, 1)
		self.layout.addWidget(self.button_expos, 0, 2)
		self.layout.addWidget(self.button_astro, 1, 2)
		self.layout.addWidget(self.button_stabilized, 2, 2)
		self.layout.addWidget(self.button_face_reco, 0, 3)
		self.layout.addWidget(self.button_pose_reco, 1, 3)
		self.layout.addWidget(self.button_hand_reco, 2, 3)
		self.layout.addWidget(self.button_controlled, 0, 4)
		self.layout.addWidget(self.button_star_positioning, 1, 4)
		self.layout.addWidget(self.button_motion_detect, 2, 4)
		self.layout.setContentsMargins(40, 30, 40, 30)
		self.layout.setVerticalSpacing(33)
		self.layout.setHorizontalSpacing(45)
		self.setLayout(self.layout)
		self.background_image = QPixmap("Gui_mode_choice_resized.png")
		self.new_actual_mode = "Photo_Mode"

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(0, 0, self.background_image)
		super().paintEvent(event)
		
	def change_mode(self, button_hit):
		self.new_actual_mode = button_hit
		print(f"Mode changed to: {self.new_actual_mode}")
		self.mode_changed.emit(button_hit)  # Emit the custom signal with the new mode
