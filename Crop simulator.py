import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PotatoClass import *
from WheatClass import *

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

    def create_view_crop_layout(self,crop_type):

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days")
        self.status_label = QLabel("Crop status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Grow manually")
        self.automatic_grow_button = QPushButton("Grow automatically")

        self.grow_grid = QGridlayout()
        self.status_grid = QGridlayout()

        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)


        


    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
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
    
