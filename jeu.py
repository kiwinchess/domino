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
        for i in range(9):
            self.commandeButtons.append(self.gridLayout_Commande.itemAt(i).widget())
        
        self.indice = 1
        self.clic = 0
        self.pv = False

        for i in self.j2Buttons:
            i.clicked.connect(self.clicJ2)
        for i in self.j1Buttons:
            i.clicked.connect(self.clicJ1)
        for i in self.plateauButtons:
            i.clicked.connect(self.clicPlateau)
        for i in self.commandeButtons:
            i.clicked.connect(self.clicCommande)

    
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
        for buttons in self.plateauButtons:
            buttons.setIcon(QIcon())
        for i in range(10):
            for j in range(10):
                if cr.plateau.contenu[i][j] != 0: 
                    domino = cr.plateau.contenu[i][j]

                    xIconPath = os.path.join("Icons","petit-"+ str(domino.c1) + "-"+str(domino.c2)+".gif")
                    self.Icon=QIcon(xIconPath)
                    self.gridLayout_Plateau.itemAtPosition(i,j).widget().setIcon(self.Icon)
                    self.gridLayout_Plateau.itemAtPosition(i,j).widget().setIconSize(QSize(500,100))        
                    
        
    def choixJ1(self):
        pass    

        
    def affichagePlateau(self):
        self.changerPioche()
        self.changerJ1()
        self.changerJ2()
        self.changerPlateau()
    
            
    def clicJ1(self):
        button = self.sender()
        idx = self.gridLayout_J1.indexOf(button)
        pos = self.gridLayout_J1.getItemPosition(idx)       
        self.xinput += str(pos[1]) + "," 
        self.clic += 1
        return self.simulation()

    def clicJ2(self):
        button = self.sender()
        idx = self.gridLayout_J2.indexOf(button)
        pos = self.gridLayout_J2.getItemPosition(idx)       
        self.xinput += str(pos[1]) + "," 
        self.clic += 1
        return self.simulation()

    def clicPlateau(self):
        button = self.sender()
        idx = self.gridLayout_Plateau.indexOf(button)
        pos = self.gridLayout_Plateau.getItemPosition(idx)
        self.xinput += str(pos[0]) + "," + str(pos[1]) + ","
        self.clic += 1
        return self.simulation()

    def clicCommande(self):
        button = self.sender()
        com = button.text()
        self.xinput += str(com) + ","
        self.clic += 1
        return self.simulation()
            
    def j1Joue(self):
        print("J1:         ")
        if self.clic >= 4:
            x = self.xinput.split(',')
            del x[-1]
            print(x)
            self.xinput = ""
            self.clic = 0
            
            if len(x)==5:
                if x[4]=='r':
                    cr.ajouteDomino(cr.j1.contenu[int(x[0])].permute(),x[1],int(x[2]),int(x[3]))
                    self.indice = 2
                else:
                    cr.ajouteDomino(cr.j1.contenu[int(x[0])],x[1],int(x[2]),int(x[3]))
                    self.indice = 2
            
            else:
                print('erreur saisie')
                print(x)
                return self.simulation()
            
    def j2Joue(self):
        print("J2:         ")
        if self.clic >= 4:
            x = self.xinput.split(',')
            del x[-1]
            print(x)
            self.xinput = ""
            self.clic = 0
            
            if len(x)==5:
                if x[4]=='r':
                    cr.ajouteDomino(cr.j2.contenu[int(x[0])].permute(),x[1],int(x[2]),int(x[3]))
                    self.indice = 1
                else:
                    cr.ajouteDomino(cr.j2.contenu[int(x[0])],x[1],int(x[2]),int(x[3]))
                    self.indice = 1
            else:
                print('erreur saisie')
                print(x)
                return self.simulation()
    
    def premierTour(self):
            
            if cr.j1.monDoubleLePlusFort()>cr.j2.monDoubleLePlusFort(): 
                print(cr.j1)
                print("C'est au joueur 1 de commencer: ")
                if self.clic >= 1:
                    x = int(self.xinput[0])
                    print(x)
                    a=cr.j1.contenu[x]
                    cr.plateau.contenu[5][5]=a
                    cr.plateauv.contenu.append(a)
                    cr.j1.contenu[x].etat='plateau'
                    cr.j1.contenu.pop(x)
                    self.clic = 0 
                    self.xinput = ""
                    self.pv = True
                    cr.t = False

                    return 2

            if cr.j2.monDoubleLePlusFort()>cr.j1.monDoubleLePlusFort():
                print(cr.j2)
                print("C'est au joueur 2 de commencer: ")
                if self.clic >= 1:

                    x = int(self.xinput[0])

                    print(x)
                    a=cr.j2.contenu[x]
                    cr.plateau.contenu[5][5]=a
                    cr.plateauv.contenu.append(a)
                    cr.j2.contenu[x].etat='plateau'
                    cr.j2.contenu.pop(x)
                    self.pv = True
                    cr.t = False
                    self.clic = 0
                    self.xinput = ""
                    return 1
    



    # def j1Joue(self):
    #     print(cr.plateau)
    #     print(cr.plateauv)
    #     print(cr.j1)
    #     x = input()#numéro du domino, g/d/hg/hd/bg/bd , x , y, r/n
    #     x=x.split(',')
    #     print(x)
    #     if len(x)==5:
    #         if x[4]=='r':
    #             self.ajouteDomino(self.j1.contenu[int(x[0])].permute(),x[1],int(x[2]),int(x[3]))
    #         else:
    #             self.ajouteDomino(self.j1.contenu[int(x[0])],x[1],int(x[2]),int(x[3]))
    #     else:
    #         print('erreur saisie')
    #         return self.j1Joue()
            
        
    
    def simulation(self,p=True):
        self.affichagePlateau()
        self.update()
        self.show()
        

        if cr.t==True:
            self.affichagePlateau()
            
            self.indice = self.premierTour()
            self.show()
            print("l'indice est: ",self.indice)
            


        if self.indice == 1:
            self.j1Joue()
            self.affichagePlateau()

        if self.indice == 2:
            self.j2Joue()
            self.affichagePlateau()


        
        


        

app = QApplication(sys.argv)
cr=Croupier()
cr.distribution()
game = Game()
game.simulation()

app.exec_()
