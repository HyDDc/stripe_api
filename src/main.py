import sys
import PySide6.QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QtCore, QtWidgets, QtGui
                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World", alignment=Qt.Alignment.AlignCenter)
    label.show()
    print(PySide6.QtCore.__version__)
    sys.exit(app.exec())
