#import needed object
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from generalFunctions import tri_Insertion

class InsertionSortView(QMainWindow):
    
    def __init__(self):
        super(InsertionSortView, self).__init__()
        #load the window interface file 
        loadUi('Views/triInsertion.ui', self)
        #move the window on the screen center
        self.move(300, 200)
        #hide table view
        self.tableWidget.hide()

        #link all buttons with their functions
        self.addNumberButton.clicked.connect(self.on_addNumberButton_clicked)
        self.sortButton.clicked.connect(self.on_sortButton_clicked)
        self.reinitilaserButton.clicked.connect(self.on_ReinitialisateButton_clicked)

        #initialise needed object
        self.table=[]
    
    def updateTableView(self):
        self.userInput.hide()
        self.addNumberButton.setEnabled(False)
        #get size of the table
        tableSize = len(self.table)
        #define the size of table view
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(tableSize)
        self.tableWidget.setItem(0,1, QTableWidgetItem("100000"))
        self.tableWidget.setColumnWidth(1, 65)
        for element in range(len(self.table)):
            self.tableWidget.setItem(0,element, QTableWidgetItem(str(self.table[element])+""))
            self.tableWidget.setColumnWidth(element, 66.9)
        self.tableWidget.show()

    
    def on_addNumberButton_clicked(self):
        if len(self.table) == 10:
            self.fstInstructionLabel.setText('Le tableau est plein. Il contient 10 élémsents.')
            #color the text in red
            self.fstInstructionLabel.setStyleSheet("color: black;")
            self.scdInstructionLabel.setText('Veuillez cliquer sur "Trier" pour trier le tableau')
            #color the text in red
            self.scdInstructionLabel.setStyleSheet("color: black;")
        else:
            userInput = self.userInput.text()
            #counter = 0
            #Check if the user has not written anything
            if userInput == "":
                pass
            else:
                try:
                    #test if the user input is an integer
                    number = int(userInput)
                    #assert number is not negativ
                    assert number >= 0
                    #add number in the table
                    #self.counter +=1
                    self.table.append(number)
                    self.scdInstructionLabel.setText(str(number)+' a bien été ajouté')
                    #color the text in red
                    self.scdInstructionLabel.setStyleSheet("color: green;")
                    self.userInput.setText('')

                    if len(self.table) == 10 :
                        self.fstInstructionLabel.setText('Le tableau est plein. Il contient 10 élémsents.')
                        #color the text in red
                        self.fstInstructionLabel.setStyleSheet("color: black;")
                        self.scdInstructionLabel.setText('Veuillez cliquer sur "Trier" pour trier le tableau')
                        #color the text in red
                        self.scdInstructionLabel.setStyleSheet("color: black;")
                        self.updateTableView()
                        self.scdInstructionLabel.setText("Voici le tableau non trié :")
                        #color the text in red
                        self.scdInstructionLabel.setStyleSheet("color: black;")
                
                #get the error if the input is not an integer
                except ValueError :
                    #print the error on screen
                    self.scdInstructionLabel.setText('Désolé, veuillez entrer un entier!!')
                    #color the text in red
                    self.scdInstructionLabel.setStyleSheet("color: red;")

                #get the error if the input is less than 0
                except AssertionError :
                    #print the error on screen
                    self.scdInstructionLabel.setText('Désolé, veuillez entrer un entier positif!!')
                    #color the text in red
                    self.scdInstructionLabel.setStyleSheet("color: red;")
    def keyPressEvent(self, e):
        """
        """
        #verify if the user has clicked on one of the enter button
        if e.key() == 16777220 or e.key() == 16777221:
            #simule that user has clicked on button "Valider"
            self.on_addNumberButton_clicked()
    
    def on_sortButton_clicked(self):
        if len(self.table) < 2 :
            self.scdInstructionLabel.setText('Le tableau doit contenir au moins deux éléments!!!')
            #color the text in red
            self.scdInstructionLabel.setStyleSheet("color: green;")
        else:
            self.table = tri_Insertion(self.table)
            self.updateTableView()
            self.scdInstructionLabel.setText('Le tableau a bien été trié!!!')
            #color the text in red
            self.scdInstructionLabel.setStyleSheet("color: green;")
            self.sortButton.setEnabled(False)

    
    def on_ReinitialisateButton_clicked(self):
        self.table = []
        self.scdInstructionLabel.setText('Le tableau a bien été réinitialiser!!!')
        #color the text in red
        self.scdInstructionLabel.setStyleSheet("color: green;")
        self.sortButton.setEnabled(True)
        self.addNumberButton.setEnabled(True)
        self.tableWidget.hide()
        self.userInput.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = InsertionSortView() # Create an instance of our class
    app.exec_() # Start the application