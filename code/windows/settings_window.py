from PyQt5.QtWidgets import QTabWidget, QWidget, QLabel, QComboBox, QSlider, QGridLayout, QApplication
from PyQt5.QtCore import Qt
import sys
import json

class SettingWindow(QTabWidget):
	def __init__(self, camera_controller, settings, method_map):
		super(SettingWindow, self).__init__()
		self.camera_controller = camera_controller
		self.settings = settings
		self.method_map = method_map
		self.layouts = {}  # Store layouts and their widgets
		self.init_ui()

	def init_ui(self):
		for tab_name, widgets in self.settings.items():
			self.layout = QGridLayout()
			self.tabs = {}
			
			for idx, (key, value) in enumerate(widgets.items()):
				if value['type'] == 'combobox':
					self.combo = QComboBox()
					self.combo.addItems(value['options'])
					
					# Connect the currentTextChanged signal to the appropriate method
					if key in self.method_map:
						self.method_name = self.method_map[key]
						self.method = getattr(self.camera_controller, self.method_name)
						self.combo.currentTextChanged.connect(self.method)
						
					self.layout.addWidget(QLabel(key), int(value['x']), int(value['y']))
					self.layout.addWidget(self.combo, int(value['x']), int(value['y']) + 1)
					self.tabs[key] = self.combo
				
				elif value['type'] == 'slider':
					self.slider = QSlider(Qt.Horizontal)
					self.slider.setRange(*value['range'])
					
					# Connect the valueChanged signal to the appropriate method
					if key in self.method_map:
						self.method_name = self.method_map[key]
						self.method = getattr(self.camera_controller, self.method_name)
						self.slider.valueChanged.connect(self.method)
						
					self.layout.addWidget(QLabel(key), int(value['x']), int(value['y']))
					self.layout.addWidget(self.slider, int(value['x']), int(value['y']) + 1)
					self.tabs[key] = self.slider
			
			self.tab = QWidget()
			self.tab.setLayout(self.layout)
			self.addTab(self.tab, tab_name)
			
			# Store the layout and its widgets
			self.layouts[tab_name] = self.tabs
			
	def update_settings(self, new_settings, new_method_map):
		self.settings = new_settings
		self.method_map = new_method_map
		self.clear_widgets()  # Clear existing widgets and layouts
		self.init_ui()  # Reinitialize the UI with new settings
	
	def clear_widgets(self):
		for i in reversed(range(self.count())):  # Iterate over all tabs in reverse order
			widget = self.widget(i)
			layout = widget.layout()
			if layout is not None:
				while layout.count():
					item = layout.takeAt(0)  # Remove each item from the layout
					widget = item.widget()
					if widget is not None:
						widget.deleteLater()  # Delete the widget
			self.removeTab(i)  # Remove the tab
