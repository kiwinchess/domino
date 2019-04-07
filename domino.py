00#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:52:27 2019

@author: picardge
"""
import unittest
import random
class Domino():
    '''la classe Domino permet de créer un domino. Ses variables 
    d'instances sont c1 et c2 qui correspondent aux nombres écrits sur 
    le domino et son état qui peut être 'pioche', 'plateau', ou 'joueurx' 
    avec x compris entre 1 et 4.'''
    def __init__(self,c1,c2,etat='pioche'):
        self.c1=c1
        self.c2=c2
        self.etat= etat
        
    def __str__(self):
        return '['+str(self.c1)+' | '+str(self.c2)+']'
    
    def permute(self):
        '''permute sert à retourner un domino pour le placer dans le sens souhaité
        permute retourne le domino'''
        self.c1, self.c2 = self.c2, self.c1
        return self

        

        
class Joueur():
    '''la classe Joueur qui permet de créer un joueur, 
    le plateau et la pioche. Ses variables d'instance sont numéro 
    qui correspond au numéro du joueur ou qui vaut
    'plateau' pour créer un plateau ou 'pioche' pour créer la pioche.'''
    def __init__(self,numero,contenu):
        self.numero=numero
        self.contenu=contenu
        
    def __str__(self):
        s = ' le jeu du joueur ' +str(self.numero) + ' est :'
        for domino in self.contenu:
            s += str(domino) + '  '
        return(s)
        
    def monDoubleLePlusFort(self):
        '''La méthode monDouble le plus fort permet de déterminer le double 
        le plus fort d'un joueur.Elle retourne la valeur du double le plus fort.'''
        m=-1
        for domino in self.contenu:
            if domino.c1==domino.c2:
                if m<domino.c1:
                    m=domino.c1
        return m
    

   
class Croupier(list):
    '''la classe Croupier hérite de list pour pouvoir retourner 
    une liste quand on l'appelle. Ici il retournera la liste des dominos 
    présents sur le plateau. Croupier est la classe qui simulera toute 
    la partie de domino de la distribution, la gestion 
    des dominos à placer sur le plateau jusqu'à l'arrêt de la partie.'''
    def __init__(self):
        self.plateau=Joueur('plateau',[])
        self.j1 = Joueur(1,[])
        self.j2 = Joueur(2,[])
        self.pioche = Joueur('pioche',[])
        self.t=True
        
    
    
    
    
    def ajouteDomino(self,domino,s):
        '''La méthode ajouteDomino permet d'ajouter un domino et de
        le retirer du jeu du joueur qui joue ce domino. Cette méthode prend 
        en argument le domino à placer et la position ('g' pour gauche et '
        d' pour droite) dans laquelle il faut placer le domino. Elle 
        affichera "coup impossible" si le joueur veut placer 
        un domino qu'il n'est pas possible de placer à la position désirée. '''
        if s=='d':
            
            if domino.c1==self.plateau.contenu[-1].c2:
                self.plateau.contenu.append(domino)
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'
                
            else:
                print('coup impossible')
                return('coup impossible')
        
        if s=='g':
            
            if domino.c2==self.plateau.contenu[0].c1:
                
                self.plateau.contenu = [domino] + self.plateau.contenu
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'
                
            else:
                print('coup impossible')
                return('coup impossible')
                
      
       

        


    
    
#    def creerJoueurs(self,nb=2):
#        j1=Joueur(1,[])
#        j2=Joueur(2,[])
#        return [j1,j2]
    
    

    def distribution(self):
        '''La méthode distribution distribue crée les 28 dominos, 
        crée la pioche et distribue aléatoirement 7 dominos à
        chaque joueur. Elle ne prend aucun argument.'''
        #on crée la pioche
        for i in range(7):
            for j in range(i,7):
                self.c1=i
                self.c2=j
                d=Domino(self.c1,self.c2,'pioche')
                self.pioche.contenu.append(d)
        random.shuffle(self.pioche.contenu)
        N=random.sample(range(0,27), 14)
        N.sort(reverse=True)
        L=N[0:7]
        M=N[7:]

        for i in L:
            C1=self.j1.contenu
            a=self.pioche.contenu.pop(i)
            a.etat='j1'
            C1.append(a)
        for j in M:
            C2=self.j2.contenu
            b=self.pioche.contenu.pop(j)
            b.etat='j2'
            C2.append(b)
            

    def piocher(self,j):
        '''La méthode piocher permet à un joueur de 
        piocher un domino dans la pioche. Cette méthode ne retourne rien.'''
        domino=self.pioche.contenu.pop(-1)
        domino.etat=''+str(j)
        j.contenu.append(domino)
    
    
    def quiAgagne(self):
        l1=len(self.j1.contenu)
        l2=len(self.j1.contenu)
        s1=0
        s2=0
        if l1<l2:
            return('Le joueur 1 a gagné!')
            
        if l1>l2:
          
            return('Le joueur 2 a gagné!')
        if l1==l2:
            for domino in self.j1.contenu:
                s1+=domino.c1+domino.c2
            for domino in self.j2.contenu:
                s2+=domino.c1+domino.c2
            if s1>s2:
                
                return('Le joueur 1 a gagné!')
            if s2>s1:
                
                return('Le joueur 2 a gagné!')
            if s1==s2:
       
                return('Vous avez fait match nul!')   
        
    
    
    def peutJouer(self,j):
        '''La méthode peutJouer détermine si un joueur 
        peut jouer. Elle prend en paramètre le 
        numéro du joueur et retourne True s'il peut jouer et False sinon.'''
        if j == 1:
         
         L=self.j1.contenu
         s=0
         for domino in L:
           if self.ajouteDomino(domino,'g')=='coup impossible' and self.ajouteDomino(domino,'d')=='coup impossible' :
               s+=1
         if s==len(L):
            return False
         else:
            
            return True
     
        if j == 2:
         L=self.j2.contenu
         s=0
         for domino in L:
           if self.ajouteDomino(domino,'g')=='coup impossible' and self.ajouteDomino(domino,'d')=='coup impossible' :
               s+=1
         if s==len(L):
            return False
         return True
     
    def premierTour(self):
            if self.j1.monDoubleLePlusFort()>self.j2.monDoubleLePlusFort():
                print(cr.j1)
                print('Le joueur 1 commence la partie, tapez le numéro du domino à jouer: ')
                x=input()
                if x not in ['0','1','2','3','4','5','6']:
                    print('numéro invalide')
                    return self.premierTour()
                x = int(x)
                self.plateau.contenu.append(self.j1.contenu[x])
                self.j1.contenu[x].etat='plateau'
                self.j1.contenu.pop(x)
                return(1)
            if self.j2.monDoubleLePlusFort()>self.j1.monDoubleLePlusFort():
                print(cr.j2)
                print('Le joueur 2 commence la partie, tapez le numéro du domino à jouer: ')
                x=input()
                if x not in ['0','1','2','3','4','5','6']:
                    print('numéro invalide')
                    return self.premierTour()
                x = int(x)
                self.plateau.contenu.append(self.j2.contenu[x])
                self.j2.contenu[x].etat='plateau'
                self.j2.contenu.pop(x)
                return(2)
            if self.j1.monDoubleLePlusFort() == -1 and self.j1.monDoubleLePlusFort() == -1:
                nb = random.randint(1,2)
                if nb == 1:
                    print(cr.j1)
                    print('Le joueur 1 commence la partie, tapez le numéro du domino à jouer: ')
                    x=input()
                    if x not in ['0','1','2','3','4','5','6']:
                        print('numéro invalide')
                        return self.premierTour()
                    x = int(x)
                    self.plateau.contenu.append(self.j1.contenu[x])
                    self.j1.contenu[x].etat='plateau'
                    self.j1.contenu.pop(x)
                    return(1)
                if nb == 2:
                    print(cr.j2)
                    print('Le joueur 2 commence la partie, tapez le numéro du domino à jouer: ')
                    x=input()
                    if x not in ['0','1','2','3','4','5','6']:
                        print('numéro invalide')
                        return self.premierTour()
                    x = int(x)
                    self.plateau.contenu.append(self.j2.contenu[x])
                    self.j2.contenu[x].etat='plateau'
                    self.j2.contenu.pop(x)
                    return(2)

    def j1Joue(self):
         print(self.plateau)
         print(self.j1)
         print('rentrez le numéro du domino suivi de la direction. Ajoutez un r pour le placer retourner')
         x = input()
         x = list(x)
         if x[0] not in ['0','1','2','3','4','5','6']:
             print('numéro domino invalide')
             return (self.j1Joue())
         if x[1] not in ['g','d']:
             print('direction invalide')
             return (self.j1Joue())
         if len(x) == 3:
            a=self.ajouteDomino(self.j1.contenu[int(x[0])].permute(),x[1])
            if a=='coup impossible':
                return self.j1Joue()
         if len(x)>3:
            print('format non valide')
            return self.j1Joue(self)
                
         else:
            b=self.ajouteDomino(self.j1.contenu[int(x[0])],x[1])
            if b=='coup impossible':
                return self.j1Joue()
            
    def j2Joue(self):
         print(self.plateau)
         print(self.j2)
         print('rentrez le numéro du domino suivi de la direction. Ajoutez un r pour le placer retourner')
         x = input()
         x = list(x)
         if x[0] not in ['0','1','2','3','4','5','6']:
             print('numéro domino invalide')
             return (self.j2Joue())
         if x[1] not in ['g','d']:
             print('direction invalide')
             return (self.j2Joue())
         if len(x) == 3:
            a=self.ajouteDomino(self.j2.contenu[int(x[0])].permute(),x[1])
            if a=='coup impossible':
                return self.j2Joue()
         if len(x)>3:
             print('format invalide')
             return self.j2Joue()
                
         else:
            b=self.ajouteDomino(self.j2.contenu[int(x[0])],x[1])
            if b=='coup impossible':
                return self.j2Joue()

    def simulation(self):
        '''La méthode simulation permet de simuler entièrement une partie. 
        Elle demandera notamment à chaque joueur quel 
        domino il souhaite jouer. Cette fonction est récursive
        car à la fin de chaque tour, un autre tour doit commencer sauf 
        si la partie s'arrête. Cette méthode retourne donc simulation.'''
        if self.t==True:
            cr.premierTour()
            a=cr.premierTour()
            self.t=False
            
                
           
                    
                    
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
            
            
            
            
        if len(self.pioche.contenu)==0 and self.peutJouer(self.j1)==False and self.peutJouer(self.j2)==False:
            print('la partie est terminée')
            return(cr.quiAgagne())
            
        if self.peutJouer(1)==False and len(self.pioche.contenu)!=0:
            self.piocher(self.j1)
        if self.peutJouer(2)==False and len(self.pioche.contenu)!=0:
            self.piocher(self.j2)
        else:
            if a==2:
                self.j1Joue()
                self.j2Joue()
            if a==1:
                self.j2Joue()
                self.j1Joue()
        return (self.simulation())   
  
          











class TestDomino(unittest.TestCase):
    '''La classe testDomino permet de teester la méthode
    monDoubleLePlusFort de la classe Joueur et les méthodes ajouteDomino,
    piocher et peutJouer de Croupier'''
    def testDouble(self):
        j1=Joueur(1,[Domino(6,6),Domino(5,4),Domino(5,5),Domino(1,2)])
        self.assertEqual(j1.monDoubleLePlusFort(),6)
        j2=Joueur(1,[Domino(4,6),Domino(5,4),Domino(5,5),Domino(1,2)])
        self.assertEqual(j2.monDoubleLePlusFort(),5)
        
    
    def testAjoute(self):
        cr=Croupier()
        cr.distribution()
        cr.plateau.contenu.append(Domino(cr.j1.contenu[0].c2,6))
        cr.ajouteDomino(cr.j1.contenu[0],'g')
        self.assertEqual(len(cr.plateau.contenu),2)
        self.assertEqual(len(cr.j1.contenu),6)
        
        cr.plateau.contenu=[]
        cr.plateau.contenu.append(Domino(6,cr.j1.contenu[0].c1))
        cr.ajouteDomino(cr.j1.contenu[0],'d')
        self.assertEqual(len(cr.plateau.contenu),2)
        self.assertEqual(len(cr.j1.contenu),5)
      
        
    def testPeutJouer(self):
        cr=Croupier()
        cr.plateau.contenu.append(Domino(0,0))
        cr.j1.contenu=cr.j1.contenu + [Domino(2,1),Domino(6,5),Domino(1,3),Domino(5,2)]
        self.assertEqual(cr.peutJouer(1),False)
        cr.j1.contenu=cr.j1.contenu + [Domino(0,1),Domino(6,5),Domino(1,3),Domino(5,2)]
        self.assertEqual(cr.peutJouer(1),True)
        
        
    def testPiocher(self):
        cr=Croupier()
        cr.distribution()
        cr.piocher(cr.j1)
        self.assertEqual(len(cr.j1.contenu),8)
        self.assertEqual(len(cr.pioche.contenu),13)
        cr.piocher(cr.j1)
        self.assertEqual(len(cr.j1.contenu),9)
        self.assertEqual(len(cr.pioche.contenu),12)
        
        
        
    
        
        


    
    
            
        
    
if __name__ == "__main__":
    cr = Croupier()
    cr.distribution()
    cr.simulation()
    
    
    #unittest.main()
    
'''master'''

