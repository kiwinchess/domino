import os
import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
from design import Ui_MainWindow

class Game(QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.setupUi(self)
        self.xinput= ""
        self.cButton = []
        for i in range(9):
            self.cButton.append(self.gridLayout.itemAt(i).widget())
        self.comButton = []
        for i in range(2):
            self.comButton.append(self.gridLayout_Com.itemAt(i).widget())
        self.indice = 1
        self.clic = 0


    def input(self):

            for i in self.cButton:
                
                i.clicked.connect(self.clicChiffre)
            for i in  self.comButton:
                i.clicked.connect(self.clicCommande)   

    def boutonClique(self):
        self.clic = 1

    def clicChiffre(self):
        button = self.sender()
        idx = self.gridLayout.indexOf(button)
        pos = self.gridLayout.getItemPosition(idx)       
        self.xinput += str(pos[0]) + "," + str(pos[1]) + ","

    def clicCommande(self):
        button = self.sender()
        com = button.text()
        self.xinput += str(com) 
        if len(self.xinput) == 5:
            self.indice = 0
            self.j1joue()

    def j1joue(self):
        if self.indice != 0: 
            return self.input()       
        if self.indice == 0:
            print(self.xinput)
            x = self.xinput.split(',')
            print(x)
            self.xinput = ""
            self.indice = 1
            return 10
    
    def simul(self):
        if self.j1joue():

            print(a)

        
        

    def afficheCoord(self):
        button = self.sender()
        idx = self.gridLayout.indexOf(button)
        pos = self.gridLayout.getItemPosition(idx)
        
        
        print("La position de l'item selectionné est: ", (pos[0],pos[1]))


app = QApplication(sys.argv)
game = Game()
game.simul()
game.show()

app.exec_()