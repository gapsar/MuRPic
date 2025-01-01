from gpiozero import Button
from gui_manager import GUIManager

class HardwareInterface:
	def __init__(self, set_current_widget_callback, capture_callback):
		self.button_Page1 = Button(14)
		self.button_Page2 = Button(15)
		self.button_Page3 = Button(18)
		self.button_Page4 = Button(23)
		self.button_capture_and_quit = Button(24, pull_up = True, hold_time=2)
		self.set_current_widget_callback = set_current_widget_callback
		self.capture_callback = capture_callback
		
		self.bind_buttons(capture_callback)
		
	def bind_buttons(self, capture_mode):
		self.button_Page1.when_released = lambda: self.set_current_widget_callback(0)
		self.button_Page2.when_released = lambda: self.set_current_widget_callback(1)
		self.button_Page3.when_released = lambda: self.set_current_widget_callback(2)
		self.button_Page4.when_released = lambda: self.set_current_widget_callback(3)
		self.button_capture_and_quit.when_released = lambda: capture_mode()
