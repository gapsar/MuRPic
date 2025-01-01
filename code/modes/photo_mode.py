import os
import datetime

class PhotoMode:
	def __init__(self, picam2):
		self.picam2 = picam2
		self.image_folder = "captured_images"
		if not os.path.exists(self.image_folder):
			os.makedirs(self.image_folder)
		self.settings = {
		'nettete_tab': {
			'resolution': {'type': 'combobox', 'options': ['8MPx', '12MPx', '16MPx', '32MPx', '48MPx', '64MPx'], 'x': '0', 'y': '0'},
			'analogue_gain': {'type': 'slider', 'range': (0, 1600), 'x': '1', 'y': '0'},
			'sharpness': {'type': 'slider', 'range': (0, 1600), 'x': '2', 'y': '0'},
			'noise_reduc_mode': {'type': 'combobox', 'options': ['Off', 'Fast', 'High Quality'], 'x': '3', 'y': '0'},
			'afmode': {'type': 'combobox', 'options': ['Manual', 'Auto', 'Continuous'], 'x': '0', 'y': '2'},
			'lens_pos': {'type': 'slider', 'range': (0, 3200), 'x': '1', 'y': '2'},
			'afspeed': {'type': 'combobox', 'options': ['Normal', 'Fast'], 'x': '2', 'y': '2'}
		},
		'couleur_tab': {
			'awb_mode': {'type': 'combobox', 'options': ['Auto', 'Tungsten', 'Fluorescent', 'Indoor', 'Daylight', 'Cloudy'], 'x': '0', 'y': '0'},
			'ae_constraint_mode': {'type': 'combobox', 'options': ['Normal', 'Highlight', 'Shadow'], 'x': '1', 'y': '0'},
			'ae_exposure_mode': {'type': 'combobox', 'options': ['Normal', 'Short', 'Long'], 'x': '2', 'y': '0'},
			'saturation': {'type': 'slider', 'range': (0, 3200), 'x': '0', 'y': '2'},
			'brightness': {'type': 'slider', 'range': (-100, 100), 'x': '1', 'y': '2'},
			'contrast': {'type': 'slider', 'range': (0, 3200), 'x': '2', 'y': '2'}
		}
	}
		
		self.method_map = {
			'resolution': 'resolution_changed',
			'analogue_gain': 'analogue_gain_changed',
			'sharpness': 'sharpness_changed',
			'noise_reduc_mode': 'noise_reduc_mode_changed',
			'afmode': 'afmode_changed',
			'lens_pos': 'lens_pos_changed',
			'afspeed': 'afspeed_changed',
			'awb_mode': 'awb_mode_changed',
			'ae_constraint_mode': 'ae_constraint_mode_changed',
			'ae_exposure_mode': 'ae_exposure_mode_changed',
			'saturation': 'saturation_changed',
			'brightness': 'brightness_changed',
			'contrast': 'contrast_changed',	
		}
		
	def capture(self):
		timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
		self.request = self.picam2.capture_request()
		self.request.save("main", './captured_images/%s.jpg' % timestamp)
		self.request.release()
		print("picture taken")
