from gui_manager import GUIManager
from camera_controller import CameraController
from hardware_interface import HardwareInterface
from windows.mode_window import ModeChoice
from windows.preview_window import PreviewWindow
from windows.settings_window_json import SettingWindow
from modes.photo_mode import PhotoMode
from modes.video_mode import VideoMode
import os

class MainApp:
	def __init__(self):
		self.gui = GUIManager()
		self.camera_controller = CameraController()
		self.preview_window = PreviewWindow(self.camera_controller.picam2)
		
		self.photo_mode = PhotoMode(self.camera_controller.picam2)
		self.video_mode = VideoMode(self.camera_controller.picam2)
		
		self.setting_window = SettingWindow(self.camera_controller, self.photo_mode.settings, self.photo_mode.method_map)
		
		self.mode_window = ModeChoice()
		self.gui.add_widget(self.preview_window, "preview_window")
		self.gui.add_widget(self.mode_window, "mode_window")
		self.gui.add_widget(self.setting_window, "setting_window")
		
		self.mode_window.mode_changed.connect(self.update_mode)

		self.hardware_interface = HardwareInterface(self.gui.set_current_widget, self.photo_mode.capture)
		self.camera_controller.start_camera()
		self.gui.set_current_widget(0)

	def run(self):
		self.gui.show()
	
	def update_mode(self, new_mode_name):
		# Use a dictionary to map mode names to their respective instances
		mode_map = {
			"Photo_Mode": self.photo_mode,
			"Video_Mode": self.video_mode,
			# Add other modes here if needed...
		}
		# Retrieve the appropriate mode instance from the map
		mode = mode_map.get(new_mode_name)
		if mode is None:
			print(f"Mode {new_mode_name} is not yet supported!")
			return
		# Update the setting window with the new mode's settings and method map
		self.setting_window.update_settings(mode.settings, mode.method_map)
		self.hardware_interface.bind_buttons(mode.capture)

if __name__ == "__main__":
	app = MainApp()
	app.run()
