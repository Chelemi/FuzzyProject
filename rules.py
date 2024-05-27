# Rules

RULES = []

# Days Worn Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS four)  AND  "
             "(Days_left_out IS one)  AND  "
             "(Activity IS none)  AND  "
             "(Stress IS none)  AND  "
             "(Temperature IS cold)  AND  "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS five)  AND  "
             "(Days_left_out IS one)  AND  "
             "(Activity IS none)  AND  "
             "(Stress IS none)  AND  "
             "(Temperature IS cold)  AND  "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days left out Variable
RULES.append("IF "
             "(Days_worn IS one)  AND  "
             "(Days_left_out IS two)  AND  "
             "(Activity IS none)  AND  "
             "(Stress IS none)  AND  "
             "(Temperature IS cold)  AND  "
             "(Hours IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one)  AND  "
             "(Days_left_out IS three)  AND  "
             "(Activity IS none)  AND  "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS four) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS five) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Activity Variable
# RULES.append("IF "
#              "(Days_worn IS one) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS some) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS somewhat clean)")
# RULES.append("IF "
#              "(Days_worn IS one) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS medium) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS somewhat dirty)")
# RULES.append("IF "
#              "(Days_worn IS one) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS a_lot) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS dirty)")
# RULES.append("IF "
#              "(Days_worn IS one) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS full) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS dirty)")

# Stress Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS some) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS medium) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS a_lot) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS full) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Temperature Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS fresh) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS temperate) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS warm) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS hot) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")

# Hours worn Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Days left out Variable
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS two) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS three) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS four) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS five) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Activity Variable
# RULES.append("IF "
#              "(Days_worn IS two) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS none) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS somewhat clean)")
# RULES.append("IF "
#              "(Days_worn IS two) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS some) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS somewhat dirty)")
# RULES.append("IF "
#              "(Days_worn IS two) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS medium) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS dirty)")
# RULES.append("IF "
#              "(Days_worn IS two) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS a_lot) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS dirty)")
# RULES.append("IF "
#              "(Days_worn IS two) AND "
#              "(Days_left_out IS one) AND "
#              "(Activity IS full) AND "
#              "(Stress IS none) AND "
#              "(Temperature IS cold) AND "
#              "(Hours IS two) "
#              "THEN "
#              "(Output IS dirty)")

# Days worn and Stress Variable
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS some) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS medium) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS a_lot) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS full) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Temperature Variable
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS fresh) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS temperate) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS warm) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS hot) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Hours Variable
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Days_left_out Variable
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat clean)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS two) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS three) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS four) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS five) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Activity Variable
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS some) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS medium) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS a_lot) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS full) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Stress Variable
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS some) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS medium) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS a_lot) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS full) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Temperature Variable
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS fresh) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS temperate) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS warm) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS hot) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Hours worn Variable
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) AND "
             "(Activity IS none) AND "
             "(Stress IS none) AND "
             "(Temperature IS cold) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

# Activity Variable
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

RULES.append("IF "
             "(Activity IS a_lot) OR "
             "(Activity IS full) "
             "THEN "
             "(Output IS dirty)")

# Days Worn variable
RULES.append("IF "
             "(Days_worn IS four) OR "
             "(Days_worn IS five) "
             "THEN "
             "(Output IS dirty)")

# from simpful import *
#
# FS = FuzzySystem()
#
# TLV = AutoTriangle(3, terms=['poor', 'average', 'good'], universe_of_discourse=[0,10])
# FS.add_linguistic_variable("service", TLV)
# FS.add_linguistic_variable("quality", TLV)
#
# O1 = TriangleFuzzySet(0,0,13,   term="low")
# O2 = TriangleFuzzySet(0,13,25,  term="medium")
# O3 = TriangleFuzzySet(13,25,25, term="high")
# FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,25]))
#
# FS.add_rules([
# 	"IF (quality IS poor) AND (service IS poor) THEN (tip IS low)",
# 	"IF (service IS average) THEN (tip IS medium)",
# 	"IF (quality IS good) AND (service IS good) THEN (tip IS high)"
# 	])
#
# FS.set_variable("quality", 6.5)
# FS.set_variable("service", 2.5)
#
# tip = FS.inference()
# print(tip)

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton, QHBoxLayout
# from PyQt6.QtCore import Qt
#
# class SliderExample(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Slider Example')
#
#         # Create a vertical layout
#         layout = QVBoxLayout()
#
#         # Create a label to display the slider value
#         self.label = QLabel('Slider Value: 0')
#         layout.addWidget(self.label)
#         self.value = 0
#
#         # Create a slider widget
#         self.slider = QSlider()
#         self.slider.setOrientation(Qt.Orientation.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setMaximum(500)
#         self.slider.setValue(250)
#         self.slider.setTickInterval(25)
#         self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
#         self.slider.valueChanged.connect(self.updateValue)
#         layout.addWidget(self.slider)
#
#         self.button = QPushButton()
#         self.button.clicked.connect(self.return_value)
#         self.button.setText('Save Value')
#         layout.addWidget(self.button)
#
#         self.setLayout(layout)
#         self.show()
#
#     def updateValue(self, value):
#         # Update the label text with the slider value
#         self.label.setText(f'Slider Value: {value}')
#         # Update the variable's value here or perform any other actions
#
#     def return_value(self):
#         self.value = self.slider.value()
#         print(self.value)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = SliderExample()
#     sys.exit(app.exec())
