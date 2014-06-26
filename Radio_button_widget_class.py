from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """Create a group of radio buttons"""
    def __init__(self,label,instructions,button_list):
        super().__init__()

        self.title_label = QLabel(label)
        self.radio_group_box = (instruction)
        self.radio_button_group = QButtonGroup()

        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        self.radio_button_list[0].setChecked(True)

        self.radio_button_layout = QBoxLayout()

        counter = 1
        for each in radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each,counter)
            counter += 1

        
        self.radio_group_box.setLayout(self.radio_button_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        self.setLayout(self.main_layout)

    def selecteId_button(self):
        return self.radio_button_group.checkedId()
