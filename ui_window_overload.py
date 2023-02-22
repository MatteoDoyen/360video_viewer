from PySide2.QtCore import (Qt, Slot, Signal)
from PySide2.QtGui import (QIcon, QPixmap, QMovie, QColor, QImage)
from PySide2.QtWidgets import (QWidget, QMainWindow, QSizePolicy, QFileDialog, QMessageBox)
from PY_UI.viewer_ui import Ui_MainWindow
import numpy as np
from utils import resource_path
import cv2

# ----------------------------------------------------------------------------------------------------------------------
class viewerWindow(QMainWindow, Ui_MainWindow):
    update_img = Signal(np.ndarray)
    def __init__(self, parent=None):
        
        super(viewerWindow, self).__init__(parent)
        self.setupUi(self)
        grey = QPixmap(736, 368)
        grey.fill(QColor('darkGray'))
        # set the image image to the grey pixmap
        self.label_view.setPixmap(grey)
        self.update_img.connect(self.update_image)
        
    @Slot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.label_view.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(736,368, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)