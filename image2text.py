import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# MainWindow class that sets up the GUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and geometry
        self.setWindowTitle("Image2Text")
        self.setGeometry(100, 100, 600, 500)
        self.setMinimumSize(300, 250)

        # Create header label and buttons for opening and converting
        self.label_header = QLabel("Image2Text", self)
        self.label_header.setAlignment(Qt.AlignCenter)
        font = self.label_header.font()
        font.setPointSize(20)
        self.label_header.setFont(font)
        self.open_button = QPushButton("Open Image", self)
        self.convert_button = QPushButton("Convert", self)

        # Create image label and text box
        self.label_image = QLabel(self)
        self.label_image.setAlignment(Qt.AlignCenter)
        self.text_box = QTextEdit(self)

        # Create horizontal layout for header
        layout_header = QHBoxLayout()
        layout_header.addWidget(self.label_header)

        # Create horizontal layout for open button
        layout_open = QHBoxLayout()
        layout_open.addWidget(self.open_button)

        # Create vertical layout for image label
        layout_image = QVBoxLayout()
        layout_image.addWidget(self.label_image)

        # Create horizontal layout for convert button
        layout_convert = QHBoxLayout()
        layout_convert.addWidget(self.convert_button)

        # Create main vertical layout and add other layouts and widgets
        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_header)
        layout_main.addLayout(layout_open)
        layout_main.addLayout(layout_image)
        layout_main.addLayout(layout_convert)
        layout_main.addWidget(self.text_box)

        # Create widget and set main layout
        widget = QWidget(self)
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)


# Create a QApplication
app = QApplication(sys.argv)
# Create the MainWindow instance
window = MainWindow()
# Show the window
window.show()
# Exit the application when the window is closed
sys.exit(app.exec_())