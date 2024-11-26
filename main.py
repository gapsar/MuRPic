#!/usr/bin/python3

#############################################
#										    #
#   This code is for the µRPic project      #
#   								   	    #
#############################################


from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QStackedWidget, QLabel, QComboBox, QLineEdit, QTabWidget, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FfmpegOutput
from picamera2.previews.qt import QGlPicamera2
from libcamera import Transform, controls
from gpiozero import Button
import datetime, time

# Defining the picam2 and it's different streams
picam2 = Picamera2()
main_stream = {"size": (4624, 3472)}
lores_stream = {"size": (1920, 1080)}
video_config = picam2.create_video_configuration(main_stream, lores_stream, encode="lores")
picam2.configure(video_config)

# The class for the window allowing to change modes
class Mode_choice(QWidget):
	def __init__(self):
		super(Mode_choice, self).__init__()
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
		print(self.new_actual_mode)

# The class for the Preview window
class Camera_Page(QWidget):
	def __init__(self, Mode_choice):
		super(Camera_Page, self).__init__()

		self.mode_choice_window = Mode_choice
		
		self.picam2 = picam2

		self.qpicamera2 = QGlPicamera2(self.picam2, width=800, height=480, keep_ar=False)
		self.button_capture_and_quit = Button(24, pull_up = True, hold_time=2)

		layout_h = QHBoxLayout()
		layout_h.addWidget(self.qpicamera2)  # Add QGlPicamera2 to the layout
		self.setLayout(layout_h)

		#self.button_capture_and_focus_and_quit.when_held = self.autofocus_cycle
		self.button_capture_and_quit.when_held = app.quit
		self.button_capture_and_quit.when_released = self.on_button_release

		self.picam2.start()  # Start the camera preview
		self.picam2.set_controls({"AfMode": 2, "AfTrigger": 0})
		self.recording = False
	
	def on_button_release(self):
		self.actual_mode = self.mode_choice_window.new_actual_mode
		self.check_mode_and_capture(self.actual_mode)
	
	def check_mode_and_capture(self, mode=None):
		actual_mode = mode
		if actual_mode == "Photo_Mode":
			self.capture_photo()
		elif actual_mode == "Video_Mode":
			self.capture_video()
		else:
			print("Error, no mode detected and Gapsar's brain didn't want to adress the issue for now")
	
	def capture_photo(self):
		timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
		self.request = self.picam2.capture_request()
		self.request.save("main", '%s.jpg' % timestamp)
		self.request.release()
		print("picture taken")
		
	# MP4 Video Capture (no sound)		
	def capture_video(self):
		self.picam2.set_controls({"AfMode": 2, "AfTrigger": 0})
		timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
		if self.recording==False:
			print("encoder starting")
			self.encoder = H264Encoder()
			self.encoder.output = FfmpegOutput('%s.mp4' % timestamp)
			self.picam2.start_encoder(self.encoder, quality=Quality.HIGH)
			self.recording = True
		else:
			self.picam2.stop_encoder()
			print("encoder stopped")
			self.recording = False
			print("video saved")
		
# The class for the window allowing to change the settings of each modes
class Settings_page(QTabWidget):
	def __init__(self):
		super(Settings_page, self).__init__()
		
		self.picam2 = picam2
		self.nettete_tab = QWidget()
		self.couleur_tab = QWidget()
		self.addTab(self.nettete_tab, "Netteté")
		self.addTab(self.couleur_tab, "Couleurs")
		self.setCurrentIndex(0)
		
		#################
		#The Netteté tab#
		#################
		
		self.layout_nettete = QGridLayout()
		
		# Create the Resolution config
		self.resolution = QLabel("Resolution :")
		self.resolution_value = QComboBox()
		self.resolution_value.addItem("8MPx")
		self.resolution_value.addItem("12MPx")
		self.resolution_value.addItem("16MPx")
		self.resolution_value.addItem("32MPx")
		self.resolution_value.addItem("48MPx")
		self.resolution_value.addItem("64MPx")
		self.resolution_value.currentTextChanged.connect(self.resolution_value_changed)
		# By using the following, you can have the index of the chosen item and read it with almost the same function as above
		#self.resolution_value.currentIndexChanged.connect(self.resolution_value_changed)
		
		# Create the Analogue Gain config
		self.analogue_gain = QLabel("Analogue Gain :")
		self.analogue_gain_value = QSlider(Qt.Horizontal)
		self.analogue_gain_value.setRange(0, 1600)
		self.analogue_gain_value.setSingleStep(16)
		self.analogue_gain_value.valueChanged.connect(self.analogue_gain_value_edited)
		
		# Create the Sharpness config
		self.sharpness = QLabel("Sharpness :")
		self.sharpness_value = QSlider(Qt.Horizontal)
		self.sharpness_value.setRange(0, 1600)
		self.sharpness_value.setSingleStep(16)
		self.sharpness_value.valueChanged.connect(self.sharpness_value_edited)
		
		# Create the Noise Reduction Mode config
		self.noise_reduc_mode = QLabel("Noise Reduc Mode :")
		self.noise_reduc_mode_value = QComboBox()
		self.noise_reduc_mode_value.addItem("Off")
		self.noise_reduc_mode_value.addItem("Fast")
		self.noise_reduc_mode_value.addItem("High Quality")
		self.noise_reduc_mode_value.currentTextChanged.connect(self.noise_reduc_mode_value_changed)
		
		# Create the AfMode config
		self.afmode = QLabel("AfMode :")
		self.afmode_value = QComboBox()
		self.afmode_value.addItem("Manual")
		self.afmode_value.addItem("Auto")
		self.afmode_value.addItem("Continuous")
		self.afmode_value.currentTextChanged.connect(self.afmode_value_changed)
		
		# Create the Lens Position config
		self.lens_pos = QLabel("Lens Position :")
		self.lens_pos_value = QSlider(Qt.Horizontal)
		self.lens_pos_value.setRange(0, 3200)
		self.lens_pos_value.setSingleStep(32)
		self.lens_pos_value.valueChanged.connect(self.lens_pos_value_edited)
		
		
		# Create the AfSpeed config
		self.afspeed = QLabel("AfSpeed :")
		self.afspeed_value = QComboBox()
		self.afspeed_value.addItem("Normal")
		self.afspeed_value.addItem("Fast")
		self.afspeed_value.currentTextChanged.connect(self.afspeed_value_changed)

		# We add and organize them in the layout
		self.layout_nettete.addWidget(self.resolution, 0, 0)
		self.layout_nettete.addWidget(self.resolution_value, 0, 1)
		self.layout_nettete.addWidget(self.analogue_gain, 1, 0)
		self.layout_nettete.addWidget(self.analogue_gain_value, 1, 1)
		self.layout_nettete.addWidget(self.sharpness, 2, 0)
		self.layout_nettete.addWidget(self.sharpness_value, 2, 1)
		self.layout_nettete.addWidget(self.noise_reduc_mode, 3, 0)
		self.layout_nettete.addWidget(self.noise_reduc_mode_value, 3, 1)
		self.layout_nettete.addWidget(self.afmode, 0, 2)
		self.layout_nettete.addWidget(self.afmode_value, 0, 3)
		self.layout_nettete.addWidget(self.lens_pos, 1, 2)
		self.layout_nettete.addWidget(self.lens_pos_value, 1, 3)
		self.layout_nettete.addWidget(self.afspeed, 2, 2)
		self.layout_nettete.addWidget(self.afspeed_value, 2, 3)
		self.nettete_tab.setLayout(self.layout_nettete)
		
		##################
		#The Couleurs tab#
		##################

		self.layout_couleurs = QGridLayout()
		
		# Create the Auto White Balance Mode config
		self.awb_mode = QLabel("Awb Mode :")
		self.awb_mode_value = QComboBox()
		self.awb_mode_value.addItem("Auto")
		self.awb_mode_value.addItem("Tungsten")
		self.awb_mode_value.addItem("Fluorescent")
		self.awb_mode_value.addItem("Indoor")
		self.awb_mode_value.addItem("Daylight")
		self.awb_mode_value.addItem("Cloudy")
		self.awb_mode_value.currentTextChanged.connect(self.awb_mode_value_changed)
		
		# Create the Ae Constraint Mode config
		self.ae_constraint_mode = QLabel("Ae Constraint Mode :")
		self.ae_constraint_mode_value = QComboBox()
		self.ae_constraint_mode_value.addItem("Normal")
		self.ae_constraint_mode_value.addItem("Highlight")
		self.ae_constraint_mode_value.addItem("Shadow")
		self.ae_constraint_mode_value.currentTextChanged.connect(self.ae_constraint_mode_value_changed)
		
		# Create the Ae Exposure Mode config
		self.ae_exposure_mode = QLabel("Ae Exposure Mode :")
		self.ae_exposure_mode_value = QComboBox()
		self.ae_exposure_mode_value.addItem("Normal")
		self.ae_exposure_mode_value.addItem("Short")
		self.ae_exposure_mode_value.addItem("Long")
		self.ae_exposure_mode_value.currentTextChanged.connect(self.ae_exposure_mode_value_changed)
		
		# Create the Saturation config
		self.saturation = QLabel("Saturation :")
		self.saturation_value = QSlider(Qt.Horizontal)
		self.saturation_value.setRange(0, 3200)
		self.saturation_value.setSingleStep(32)
		self.saturation_value.valueChanged.connect(self.saturation_value_edited)
		
		# Create the Brightness config
		self.brightness = QLabel("Brightness :")
		self.brightness_value = QSlider(Qt.Horizontal)
		self.brightness_value.setRange(-100, 100)
		self.brightness_value.setSingleStep(2)
		self.brightness_value.valueChanged.connect(self.brightness_value_edited)
		
		# Create the Contrast config
		self.contrast = QLabel("Contrast :")
		self.contrast_value = QSlider(Qt.Horizontal)
		self.contrast_value.setRange(0, 3200)
		self.contrast_value.setSingleStep(32)
		self.contrast_value.valueChanged.connect(self.contrast_value_edited)
		
		# We add and organize them in the layout
		self.layout_couleurs.addWidget(self.awb_mode, 0, 0)
		self.layout_couleurs.addWidget(self.awb_mode_value, 0, 1)
		self.layout_couleurs.addWidget(self.ae_constraint_mode, 1, 0)
		self.layout_couleurs.addWidget(self.ae_constraint_mode_value, 1, 1)
		self.layout_couleurs.addWidget(self.ae_exposure_mode, 2, 0)
		self.layout_couleurs.addWidget(self.ae_exposure_mode_value, 2, 1)
		self.layout_couleurs.addWidget(self.saturation, 0, 2)
		self.layout_couleurs.addWidget(self.saturation_value, 0, 3)
		self.layout_couleurs.addWidget(self.brightness, 1, 2)
		self.layout_couleurs.addWidget(self.brightness_value, 1, 3)
		self.layout_couleurs.addWidget(self.contrast, 2, 2)
		self.layout_couleurs.addWidget(self.contrast_value, 2, 3)
		self.couleur_tab.setLayout(self.layout_couleurs)
		
	# All the QComboBox functions
	def resolution_value_changed(self, text):
		print("Resolution is now",text)
			
	def noise_reduc_mode_value_changed(self, text):
		if text == "Off":
			self.picam2.controls.NoiseReductionMode = controls.draft.NoiseReductionModeEnum.Off
		elif text == "Fast":
			self.picam2.controls.NoiseReductionMode = controls.draft.NoiseReductionModeEnum.Fast
		elif text == "High Quality":
			self.picam2.controls.NoiseReductionMode = controls.draft.NoiseReductionModeEnum.HighQuality
		print("Noise Reduction Mode is now",text)

	def afmode_value_changed(self, text):
		if text == "Fast":
			self.picam2.controls.AfMode = controls.AfModeEnum.Fast
		elif text == "Normal":
			self.picam2.controls.AfMode = controls.AfModeEnum.Normal
		print("AfMode is now",text)
			
	def afspeed_value_changed(self, text):
		if text == "Fast":
			self.picam2.controls.AfSpeed = controls.AfSpeedEnum.Fast
		elif text == "Normal":
			self.picam2.controls.AfSpeed = controls.AfSpeedEnum.Normal
		print("AfSpeed is now",text)
			
	def awb_mode_value_changed(self, text):
		if text == "Auto":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Auto
		elif text == "Tungsten":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Tungsten
		elif text == "Fluorescent":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Fluorescent
		elif text == "Indoor":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Indoor
		elif text == "Daylight":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Daylight
		elif text == "Cloudy":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Cloudy
		elif text == "Custom":
			self.picam2.controls.AwbMode = controls.AwbModeEnum.Custom
		print("Auto White Balance Mode is now",text)
			
	def ae_constraint_mode_value_changed(self, text):
		if text == "Normal":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Normal
		elif text == "Highlight":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Highlight
		elif text == "Shadows":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Shadows
		elif text == "Custom":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Custom
		print("Ae Constraint Mode is now",text)
			
	def ae_exposure_mode_value_changed(self, text): 
		if text == "Normal":
			controls.AeExposureMode = controls.AeExposureModeEnum.Normal
		elif text == "Short":
			controls.AeExposureMode = controls.AeExposureModeEnum.Short
		elif text == "Long":
			controls.AeExposureMode = controls.AeExposureModeEnum.Long
		elif text == "Custom":
			controls.AeExposureMode = controls.AeExposureModeEnum.Custom
		print("Ae Exposure Mode is now",text)

	# All the QLineEdit functions
	def analogue_gain_value_edited(self, text):
		self.picam2.controls.AnalogueGain = text/100
		print("Analogue Gain is now", text/100)
		
	def sharpness_value_edited(self, text):
		self.picam2.controls.Sharpness = text/100
		print("The Sharpness is now", text/100)

	def lens_pos_value_edited(self, text): 
		self.picam2.controls.LensPosition = text/100
		print("The Lens Position is now", text/100)
		
	def saturation_value_edited(self, text):
		self.picam2.controls.Saturation = text/100
		print("The Saturation is now", text/100)
		
	def brightness_value_edited(self, text):
		self.picam2.controls.Brightness = text/100
		print("The Brightness is now", text/100)
		
	def contrast_value_edited(self, text):
		self.picam2.controls.Contrast = text/100
		print("The Contrast is now", text/100)


# The class for the Miscelaneous window, that will (one day i promise) allow to find the extra data of each mode.
# It might range from just a gallery for the video, photo, panorama modes to the recognized faces or poses for the pose and face recognition modes.
class Camera_roll(QWidget):
	def __init__(self):
		super(Camera_roll, self).__init__()
		self.layout = QVBoxLayout()
		self.button = QPushButton("Page 4 Button")
		self.layout.addWidget(self.button)
		self.setLayout(self.layout)

#Le Main

if __name__ == '__main__':
	app = QApplication([])
	
	stacked_widget = QStackedWidget()
	Mode_choice = Mode_choice()
	Camera_Page = Camera_Page(Mode_choice)
	Settings_page = Settings_page()
	Camera_roll = Camera_roll()

	stacked_widget.addWidget(Camera_Page)
	stacked_widget.addWidget(Mode_choice)
	stacked_widget.addWidget(Settings_page)
	stacked_widget.addWidget(Camera_roll)
	
	stacked_widget.setCurrentWidget(Camera_Page)  # Set the initial page

	def switch_page(page_index):
		stacked_widget.setCurrentIndex(page_index)

	button_Page1 = Button(14)
	button_Page2 = Button(15)
	button_Page3 = Button(18)
	button_Page4 = Button(23)
		
	button_Page1.when_released = lambda: switch_page(0)
	button_Page2.when_released = lambda: switch_page(1)
	button_Page3.when_released = lambda: switch_page(2)
	button_Page4.when_released = lambda: switch_page(3)

	layout = QVBoxLayout()
	layout.addWidget(stacked_widget)

	main_widget = QWidget()
	main_widget.setLayout(layout)
	main_widget.setWindowTitle("Page Switching Example")
	main_widget.showFullScreen()

	app.exec()

	Camera_Page.picam2.stop()  # Stop the camera preview when the application exits
