#import needed object
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from nombrePremierApp import PrimeNumberView
from sommeMoyenneApp import SumAverageView
from copainApp import FriendsView
from tris import SortsView
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

class MainView(QMainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        loadUi('Views/MainView.ui', self).show()
        #link all button with their function
        self.primeNumberButton.clicked.connect(self.on_PrimeNumberButton_clicked)
        self.sumAverageButton.clicked.connect(self.on_sumAverageButton_clicked)
        self.friendsButton.clicked.connect(self.on_FriendsButton_clicked)
        self.sortButton.clicked.connect(self.on_SortButton_clicked)

        self.move(300, 150)
    
    def on_PrimeNumberButton_clicked(self):
        """
            Functin to open the "Nombre Premier" windows
        """
        self.numberPrimeWindow = PrimeNumberView()
        self.numberPrimeWindow.show()
    
    def on_sumAverageButton_clicked(self):
        """
            Functin to open the "Moyenne" windows
        """
        self.sumAverageWindow = SumAverageView()
        self.sumAverageWindow.show()
    
    def on_FriendsButton_clicked(self):
        """
            Functin to open the "Copains" windows
        """
        self.friendsWindow = FriendsView()
        self.friendsWindow.show()
    
    def on_SortButton_clicked(self):
        """
            Functin to open the "Copains" windows
        """
        self.sortsWindow = SortsView()
        self.sortsWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = MainView() # Create an instance of our class
    app.exec_() # Start the application