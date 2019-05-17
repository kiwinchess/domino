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
        self.clic = 1
        
        
        for i in self.cButton:
            i.clicked.connect(self.clicChiffre)
        for i in  self.comButton:
            i.clicked.connect(self.clicCommande)
            

                    
            
    

    def clicChiffre(self):
        button = self.sender()
        idx = self.gridLayout.indexOf(button)
        pos = self.gridLayout.getItemPosition(idx)       
        self.xinput += str(pos[0]) + "," + str(pos[1]) + ","
        print("clic   ", self.clic)
        self.clic += 1
        if self.indice == 1:
            return  self.j1Joue()
        if self.indice == 2:
            return self.j2Joue()


    def clicCommande(self):
        button = self.sender()
        com = button.text()
        self.xinput += str(com) 
        print("clic   ", self.clic)
        self.clic += 1 
        if self.indice == 1:
            return self.j1Joue()
        if self.indice == 2:
            return self.j2Joue()
        
    
    def j1Joue(self):
        if self.clic>=3:
        
            print("J1   ",self.xinput)
            self.xinput = ""
            self.clic = 1
            self.indice = 2
    
    def j2Joue(self):
        if self.clic>=3:
            print("J2    ",self.xinput)
            print(self.xinput)
            self.xinput = ""
            self.clic = 1
            self.indice = 1

    
    def simul(self):
        self.indice = 1
        self.indice = 2 
        
        

    def afficheCoord(self):
        button = self.sender()
        idx = self.gridLayout.indexOf(button)
        pos = self.gridLayout.getItemPosition(idx)
        
        
        print("La position de l'item selectionné est: ", (pos[0],pos[1]))


app = QApplication(sys.argv)
game = Game()

game.j1Joue()

game.show()
app.exec_()