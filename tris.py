#import needed object
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from trisBulles import BubbleSortView
from triInsertion import InsertionSortView
from triSelection import SelectionSortView
from triFusion import MergeSortView

class SortsView(QMainWindow):
    
    def __init__(self):
        super(SortsView, self).__init__()
        loadUi('Views/Tris.ui', self)
        self.move(300, 150)
        #link all button with their function
        self.bubbleSortButton.clicked.connect(self.on_bubbleSortButton_clicked)
        self.mergeSortButton.clicked.connect(self.on_mergeSortButton_clicked)
        self.insertionSortButton.clicked.connect(self.on_insertionSortButton_clicked)
        self.selectionSortButton.clicked.connect(self.on_selectionSortButton_clicked)

    def on_bubbleSortButton_clicked(self):
        self.bubbleSortWindow = BubbleSortView()
        self.bubbleSortWindow.show()
    
    def on_mergeSortButton_clicked(self):
        self.mergeSortWindow = MergeSortView()
        self.mergeSortWindow.show()
    
    def on_insertionSortButton_clicked(self):
        self.insertionSortWindow = InsertionSortView()
        self.insertionSortWindow.show()
    
    def on_selectionSortButton_clicked(self):
        self.selectionSortWindow = SelectionSortView()
        self.selectionSortWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = SortsView() # Create an instance of our class
    app.exec_() # Start the application