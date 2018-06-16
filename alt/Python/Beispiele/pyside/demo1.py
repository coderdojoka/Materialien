import sys
from PyQt4.QtGui import *

__author__ = 'Mark Weinreuter'
# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)

class AbsolutePositioningExample(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''
    def __init__(self):
        # Initialize the object as a QWidget
        QWidget.__init__(self)

        # We have to set the size of the main window
        # ourselves, since we control the entire layout
        self.setMinimumSize(400, 185)
        self.setWindowTitle('Dynamic Greeter')

        # A vertical box layout

        layout = QVBoxLayout()
        # A vertical box layout
        lbl_1 = QLabel("ddd")
        lbl_2 = QLabel('left')
        lbl_3 = QLabel('right.')

        # Add the widgets to the layout
        layout.addWidget(lbl_1)

        sub_layout = QHBoxLayout()
        layout.addLayout(sub_layout)

        sub_layout.addWidget(lbl_2)
        sub_layout.addWidget(lbl_3)

        # Set layout as the layout for the window
        self.setLayout(layout)

    def run(self):
        # Show the form
        self.show()
        # Run the Qt application
        qt_app.exec_()

# Create an instance of the application window and run it
app = AbsolutePositioningExample()
app.run()