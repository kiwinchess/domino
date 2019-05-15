import os
import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from domino2d2 import *

from design import Ui_MainWindow

class Game(QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.xinput = ""
        self.allButtons = self.findChildren(QPushButton)
        self.piocheButtons = []
        for i in range(14):
            print(type(self.pushButton))
            self.piocheButtons.append(self.gridLayout_Pioche.itemAt(i).widget())
        self.j1Buttons = []
        for i in range(7):
            self.j1Buttons.append(self.gridLayout_J1.itemAt(i).widget())
        self.j2Buttons = []
        for i in range(7):
            self.j2Buttons.append(self.gridLayout_J2.itemAt(i).widget())
        self.plateauButtons = []
        for i in range(100):
            self.plateauButtons.append(self.gridLayout_Plateau.itemAt(i).widget())
        self.commandeButtons = []
        for i in range(6):
            self.commandeButtons.append(self.gridLayout_Commande.itemAt(i).widget())

     
    
    # def afficheCoord(self):
    #     button = self.sender()
    #     idx = self.gridLayout_Plateau.indexOf(button)
    #     pos = self.gridLayout_Plateau.getItemPosition(idx)
    #     print("La position de l'item selectionné est: ", (pos[0],pos[1]))
    #     print("L'index de l'item est : ", idx) 
    
        
       
       

    def changerPioche(self):
      
        j = 0  
        for domino in cr.pioche.contenu:
            xIconPath = os.path.join("Icons","petit-"+ str(domino.c1) + "-"+str(domino.c2)+".gif")
            self.Icon=QIcon(xIconPath)
            self.piocheButtons[j].setIcon(self.Icon)
            self.piocheButtons[j].setIconSize(QSize(500,100))        
            j += 1


       

    
    def changerJ1(self):
        j = 0  
        for buttons in self.j1Buttons:
            buttons.setIcon(QIcon())
        for domino in cr.j1.contenu:
            xIconPath = os.path.join("Icons","petit-"+ str(domino.c1) + "-"+str(domino.c2)+".gif")
            self.Icon=QIcon(xIconPath)
            self.j1Buttons[j].setIcon(self.Icon)
            self.j1Buttons[j].setIconSize(QSize(500,100))        
            j += 1



    def changerJ2(self):
        j = 0  
        for buttons in self.j2Buttons:
            buttons.setIcon(QIcon())
        for domino in cr.j2.contenu:
            xIconPath = os.path.join("Icons","petit-"+ str(domino.c1) + "-"+str(domino.c2)+".gif")
            self.Icon=QIcon(xIconPath)
            self.j2Buttons[j].setIcon(self.Icon)
            self.j2Buttons[j].setIconSize(QSize(500,100))        
            j += 1
    
    def changerPlateau(self):
        j = 0  
        for buttons in self.plateauButtons:
            buttons.setIcon(QIcon())
        for domino in cr.plateauv.contenu:
            xIconPath = os.path.join("Icons","petit-"+ str(domino.c1) + "-"+str(domino.c2)+".gif")
            self.Icon=QIcon(xIconPath)
            self.plateauButtons[j].setIcon(self.Icon)
            self.plateauButtons[j].setIconSize(QSize(500,100))        
            j += 1
        
    def choixJ1(self):
        pass    

        
    def affichagePlateau(self):
        self.changerPioche()
        self.changerJ1()
        self.changerJ2()
        self.changerPlateau()
    
    def j1Joue(self):
        while len(self.xinput) < 9 :
            for i in self.j1Buttons:
                i.clicked.connect(self.clicJ1)
            for i in self.plateauButtons:
                i.clicked.connect(self.clicPlateau)
            for i in self.commandeButtons:
                i.clicked.connect(self.clicCommande)
        x = self.xinput.split(',')
        self.xinput = ""
        print(x)
        if len(x)==5:
            if x[4]=='r':
                self.ajouteDomino(self.j1.contenu[int(x[0])].permute(),x[1],int(x[2]),int(x[3]))
            else:
                self.ajouteDomino(self.j1.contenu[int(x[0])],x[1],int(x[2]),int(x[3]))
        else:
            print('erreur saisie')
            return self.j1Joue()

            
    def clicJ1(self):
        button = self.sender()
        idx = self.gridLayout_J1.indexOf(button)
        pos = self.gridLayout_J1.getItemPosition(idx)       
        self.xinput += str(pos[1]) + "," 
    def clicPlateau(self):
        button = self.sender()
        idx = self.gridLayout_Plateau.indexOf(button)
        pos = self.gridLayout_Plateau.getItemPosition(idx)
        self.xinput += str(pos[0]) + "," + str(pos[1]) + ","
    def clicCommande(self):
        button = self.sender()
        com = button.text()
        self.xinput += str(com) + ","
        
    
    def simulation(self,a=-1,p=True):
        self.affichagePlateau()
        self.update()
        self.show()
        

        if cr.t==True:
            a = cr.premierTour()
            self.affichagePlateau()
            self.show()
            print("a: 0",a)
            cr.t=False


        if len(cr.pioche.contenu)==0 and cr.peutJouer(cr.j1)==False and cr.peutJouer(cr.j2)==False:
            print('la partie est terminée')

        if a==2:
              if cr.peutJouer(1)== True:
                self.j1Joue()
                self.affichagePlateau()

                if cr.peutJouer(2)== True:
                    cr.j2Joue()
                    self.affichagePlateau()
                else:
                  print("j2 a pioché ")
                  cr.piocher(cr.j2)
                  self.affichagePlateau()
                  a = 1
              else:
                print("YESSSSSSSSSSSSSSSSSSS")
                print("j1 a pioché ")
                cr.piocher(cr.j1)
                self.affichagePlateau()
                a = 2
        if a==1:
              if cr.peutJouer(2)== True:
                cr.j2Joue()
                self.affichagePlateau()
                if cr.peutJouer(1)== True:
                    self.j1Joue()
                    self.affichagePlateau()
                else:
                  print("OUUIIIIIIIIIIII")
                  print("j1 a pioché ")
                  cr.piocher(cr.j1)
                  self.affichagePlateau()
                  a = 2
              else:
                print("j2 a pioché ")
                cr.piocher(cr.j2)
                self.affichagePlateau()
                a = 1
        
        


        return (self.simulation(a,p))

app = QApplication(sys.argv)
cr=Croupier()
cr.distribution()
game = Game()
game.simulation()

app.exec_()
