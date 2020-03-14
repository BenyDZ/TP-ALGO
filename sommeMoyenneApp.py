#import needed object
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from generalFunctions import sumTableElt, average

class SumAverageView(QMainWindow):
    
    def __init__(self):
        super(SumAverageView, self).__init__()
        #load the window interface file 
        loadUi('Views/sommeMoyenne.ui', self)
        #move the window on the screen center
        self.move(450, 200)
        #link the button "Ajouter le nombre" to the function on_addNumberButton_clicked
        self.addNumber.clicked.connect(self.on_addNumberButton_clicked)
        #link the button "Moyenne" to the function on_averageButton_clicked
        self.averageButton.clicked.connect(self.on_averageButton_clicked)
        self.table=[]
    
    def on_addNumberButton_clicked(self):
        #get the user input
        userInput = self.userInput.text()
        #Check if the user has not written anything
        if userInput == "":
            pass
        else:
            try:
                #test if the user input is an real
                number = float(userInput)
                #assert number is positif
                assert number >= 0
                #add number in the table
                self.table.append(number)
                self.instructionLabel.setText(str(number)+' a bien été ajouté')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: green;")
                self.userInput.setText('')
            
            #get the error if the input is not an integer
            except ValueError :
                #print the error on screen
                self.instructionLabel.setText('Désolé, veuillez entrer un réel!!')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: red;")

            #get the error if the input is less than 0
            except AssertionError :
                #print the error on screen
                self.instructionLabel.setText('Désolé, veuillez entrer un réel positif!!')
                #color the text in red
                self.instructionLabel.setStyleSheet("color: red;")
    
    def keyPressEvent(self, e):
        """
        """
        #verify if the user has clicked on one of the enter button
        if e.key() == 16777220 or e.key() == 16777221:
            #simule that user has clicked on button "Valider"
            self.on_addNumberButton_clicked()
    
    def on_averageButton_clicked(self):
        try:
            aver = average(sumTableElt(self.table), self.table)
            self.instructionLabel.setText('La moyenne est égale à : '+str(aver))
            #color the text in green
            self.instructionLabel.setStyleSheet("color: green;")
            self.table = []
        except ZeroDivisionError:
            pass
        
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = SumAverageView() # Create an instance of our class
    app.exec_() # Start the application