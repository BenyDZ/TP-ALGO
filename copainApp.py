#import needed object
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from generalFunctions import sumOfDividers

class FriendsView(QMainWindow):
    
    def __init__(self):
        super(FriendsView, self).__init__()
        #load the interface file
        loadUi('Views/Copains.ui', self)
        #move the window
        self.move(450, 200)
        #self.validateButton.clicked.connect(self.on_validateButton_clicked)
    
    def on_testButton_clicked(self):
        #get user inputs
        firstNumber = self.firstUserInput.text()
        scdNumber = self.scdUserInput.text()

        if firstNumber != "" and scdNumber != "":
            try:
                #test if the input is an integer
                firstNumber = int(firstNumber)
                #assert the input is more than 1
                assert firstNumber > 0

                try:
                    #test if the input is an integer
                    scdNumber = int(scdNumber)
                    #assert the input is more than 1
                    assert scdNumber > 0

                    #get the sums of all dividers of the two user inputs
                    sumsOfDividers1 = sumOfDividers(firstNumber)
                    sumsOfDividers2 = sumOfDividers(scdNumber)

                    #compare the two sums of dividers with the two user inputs
                    if sumsOfDividers1 == scdNumber and sumsOfDividers2 == firstNumber:
                        #print the result on screen
                        self.instructionLabel.setText('Les nombres '+str(firstNumber)+' et '+str(scdNumber)+' sont copains!!')
                        #color the text in green
                        self.instructionLabel.setStyleSheet("color: green;")
                    else:
                        #print the result on screen
                        self.instructionLabel.setText('Les nombres '+str(firstNumber)+' et '+str(scdNumber)+' ne sont pas copains!!')
                        #color the text in red
                        self.instructionLabel.setStyleSheet("color: red;")

                #get the error if the input is not an integer
                except ValueError :
                    #print the error on screen
                    self.instructionLabel.setText('Désolé, veuillez entrer un entier!!')
                    #color the text in red
                    self.instructionLabel.setStyleSheet("color: red;")
                #get the error if the input is less than 0
                except AssertionError :
                    #print the error on screen
                    self.instructionLabel.setText('Désolé, veuillez entrer un entier positif!!')
                    #color the text in red
                    self.instructionLabel.setStyleSheet("color: red;")

            #get the error if the input is not an integer
            except ValueError :
                #print the error on screen
                self.instructionLabel.setText('Désolé, veuillez entrer un entier!!')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: red;")
            #get the error if the input is less than 0
            except AssertionError :
                #print the error on screen
                self.instructionLabel.setText('Désolé, veuillez entrer un entier positif!!')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: red;")
        else:
            #print the error on screen
            self.instructionLabel.setText('Veuillez remplir les deux cases!!')
            #color the text in red
            self.instructionLabel.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = FriendsView() # Create an instance of our class
    app.exec_() # Start the application