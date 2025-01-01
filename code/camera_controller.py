from picamera2 import Picamera2
from windows.settings_window_json import SettingWindow
import time

class CameraController:
	def __init__(self):
		self.picam2 = Picamera2()
		self.main_stream = {"size": (4624, 3472)}
		self.lores_stream = {"size": (1920, 1080)}
		self.config = self.picam2.create_preview_configuration(main_stream, lores_stream, display="lores", encode="lores")
		self.picam2.set_controls({"AfMode": 2, "AfTrigger": 0})
		self.picam2.configure(self.config)

	def start_camera(self):
		self.picam2.start()
		
	# All the QComboBox functions
	def resolution_changed(self, text):
		print("Resolution is now",text)
			
	def noise_reduc_mode_changed(self, text):
		if text == "Off":
			self.picam2.controls.NoiseReductionMode = controls.draft.NoiseReductionModeEnum.Off
		elif text == "Fast":
			self.picam2.controls.NoiseReductionMode = controls.draft.NoiseReductionModeEnum.Fast
		elif text == "High Quality":
			self.picam2.controls.NoiseReductionMode = controls.draft.NoiseReductionModeEnum.HighQuality
		print("Noise Reduction Mode is now",text)

	def afmode_changed(self, text):
		if text == "Fast":
			self.picam2.controls.AfMode = controls.AfModeEnum.Fast
		elif text == "Normal":
			self.picam2.controls.AfMode = controls.AfModeEnum.Normal
		print("AfMode is now",text)
			
	def afspeed_changed(self, text):
		if text == "Fast":
			self.picam2.controls.AfSpeed = controls.AfSpeedEnum.Fast
		elif text == "Normal":
			self.picam2.controls.AfSpeed = controls.AfSpeedEnum.Normal
		print("AfSpeed is now",text)
			
	def awb_mode_changed(self, text):
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
			
	def ae_constraint_mode_changed(self, text):
		if text == "Normal":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Normal
		elif text == "Highlight":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Highlight
		elif text == "Shadows":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Shadows
		elif text == "Custom":
			self.picam2.controls.AeConstraintMode = controls.AeConstraintModeEnum.Custom
		print("Ae Constraint Mode is now",text)
			
	def ae_exposure_mode_changed(self, text): 
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
	def analogue_gain_changed(self, text):
		self.picam2.controls.AnalogueGain = text/100
		print("Analogue Gain is now", text/100)
		
	def sharpness_changed(self, text):
		self.picam2.controls.Sharpness = text/100
		print("The Sharpness is now", text/100)

	def lens_pos_changed(self, text): 
		self.picam2.controls.LensPosition = text/100
		print("The Lens Position is now", text/100)
		
	def saturation_changed(self, text):
		self.picam2.controls.Saturation = text/100
		print("The Saturation is now", text/100)
		
	def brightness_changed(self, text):
		self.picam2.controls.Brightness = text/100
		print("The Brightness is now", text/100)
		
	def contrast_changed(self, text):
		self.picam2.controls.Contrast = text/100
		print("The Contrast is now", text/100)
