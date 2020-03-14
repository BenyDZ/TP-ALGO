#import needed object
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from generalFunctions import isPrime

class PrimeNumberView(QMainWindow):
    
    def __init__(self):
        super(PrimeNumberView, self).__init__()
        loadUi('Views/nombrePremmier.ui', self)
        self.move(450, 200)
        self.validateButton.clicked.connect(self.on_validateButton_clicked)
    
    def on_validateButton_clicked(self):
        """
            Function to verify if a number is prime or not
        """
        #get the user input
        userInput = self.userInput.text()
        #Check if the user has not written anything
        if userInput == "":
            pass
        else:
            try :
                #test if the user input is an integer
                number = int(userInput)
                assert number >=0
                #test if the number is a prime number
                result = isPrime(number)
                if result:
                    #print the error on screen
                    self.instructionLabel.setText('Entrez un nombre entier')
                    #color the text in black
                    self.instructionLabel.setStyleSheet("color: black;")
                    #print the result on screen
                    self.resultatLabel.setText(str(number)+' est un nombre premier!!')
                    #color the text in green
                    self.resultatLabel.setStyleSheet("color: green;")
                else :
                    #print the error on screen
                    self.instructionLabel.setText('Entrez un nombre entier')
                    #color the text in black
                    self.instructionLabel.setStyleSheet("color: black;")
                    #print the result on screen
                    self.resultatLabel.setText(str(number)+" n'est pas un nombre premier!!")
                    #color the text in green
                    self.resultatLabel.setStyleSheet("color: red;")

            #get the error if the input is not an integer
            except ValueError :
                #print the error on screen
                self.instructionLabel.setText('Désolé, veuillez entrer un entier!!')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: red;")
                #print the error on screen
                self.resultatLabel.setText('')
            #get the error if the input is less than 0
            except AssertionError :
                #print the error on screen
                self.instructionLabel.setText('Désolé, veuillez entrer un entier positif!!')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: red;")
                #print the error on screen
                self.resultatLabel.setText('')
            
    def keyPressEvent(self, e):
        """
        """
        #verify if the user has clicked on one of the enter button
        if e.key() == 16777220 or e.key() == 16777221:
            #simule that user has clicked on button "Valider"
            self.on_validateButton_clicked()
            


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = PrimeNumberView() # Create an instance of our class
    app.exec_() # Start the application