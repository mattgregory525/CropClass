import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Radio_button_widget_class import *

class CropWindow(QMainWindow):
    """This class creates the main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop simulator")
        self.create_select_crop_layout()


    def create_select_crop_layout(self):

        self.crop_radio_buttons = RadioButtonWidget("Crop simulation", "Please select a choice", ("Wheat", "Potato"))
        self.instantiate_button = QPushButton("Create crop")


        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.selected_crop_widget = QWidget()
        self.selected_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.selected_crop_widget)

        self.instantiate_button.clicked.connect(self.instantiate_crop)


    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type ==1:
            self.simulated_crop = Wheat()
        elif crop_type ==2:
            self.simulated_crop = Potato()
        print(self.simulated_crop)

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()
    
