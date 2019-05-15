import unittest
import random
class Domino():
    def __init__(self,c1,c2,etat='pioche'):
        self.c1=c1
        self.c2=c2
        self.etat= etat

    def __str__(self):
        return '['+str(self.c1)+' | '+str(self.c2)+']'

    def permute(self):
        self.c1, self.c2 = self.c2, self.c1
        return self




class Joueur():
    def __init__(self,numero,contenu):
        self.numero=numero
        self.contenu=contenu

    def __str__(self):
        s = str(self.numero) + ':      '
        for domino in self.contenu:
            s += str(domino) + '  '
        return(s)

    def monDoubleLePlusFort(self):
        m=0
        for domino in self.contenu:
            if domino.c1==domino.c2:
                if m<domino.c1:
                    m=domino.c1
        return m



class Croupier(list):

    def __init__(self):
        self.plateauv=Joueur('plateauv',[])
        self.plateau=Joueur('plateau',[[0 for i in range(14)]for j in range(14)] )
        self.j1 = Joueur(1,[])
        self.j2 = Joueur(2,[])
        self.pioche = Joueur('pioche',[])
        self.t=True




    def ajouteDomino(self,domino,s,x,y):
        '''La méthode ajouteDomino permet d'ajouter un domino et de
        le retirer du jeu du joueur qui joue ce domino. Cette méthode prend
        en argument le domino à placer et la position ('g' pour gauche et '
        d' pour droite) dans laquelle il faut placer le domino. Elle
        affichera "coup impossible" si le joueur veut placer
        un domino qu'il n'est pas possible de placer à la position désirée. '''
        if s=='d':
            if domino.c1==self.plateau.contenu[x][y-1].c2:
                self.plateauv.contenu.append(domino)
                self.plateau.contenu[x][y]=domino
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

            if domino.c2==self.plateau.contenu[x][y+1].c1:
                self.plateauv.contenu=[domino]+self.plateauv.contenu
                self.plateau.contenu[x][y] = domino
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'
            else:
                print('coup impossible')
                return('coup impossible')

        if s=='hg':
            if domino.c2==self.plateau.contenu[x+1][y].c1:
                self.plateauv.contenu=[domino]+self.plateauv.contenu
                self.plateau.contenu[x][y] = domino
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'

            else:
                print('coup impossible')
                return('coup impossible')

        if s=='bg':
            if domino.c2==self.plateau.contenu[x-1][y].c1:
                self.plateauv.contenu=[domino]+self.plateauv.contenu
                self.plateau.contenu[x][y] = domino
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'

            else:
                print('coup impossible')
                return('coup impossible')

        if s=='hd':
            if domino.c1==self.plateau.contenu[x+1][y].c2:
                self.plateauv.contenu.append(domino)
                self.plateau.contenu[x][y] = domino
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'

            else:
                print('coup impossible')
                return('coup impossible')

        if s=='bd':
            if domino.c1==self.plateau.contenu[x-1][y].c2:
                self.plateauv.contenu.append(domino)
                self.plateau.contenu[x][y] = domino
                j=domino.etat
                if j=='j1':
                    self.j1.contenu.remove(domino)
                if j=='j2':
                    self.j2.contenu.remove(domino)
                j='plateau'

            else:
                print('coup impossible')
                return('coup impossible')

        else:
            return('erreur saisie')

    def testAjouteDomino(self,domino,s):
        if s=='d':
          if domino.c1!=self.plateauv.contenu[-1].c2:
            return('coup impossible')

        if s=='g':
            if domino.c2!=self.plateauv.contenu[0].c1:
                return('coup impossible')
        if s=='hg':
            if domino.c2!=self.plateauv.contenu[0].c1:
                return('coup impossible')
        if s=='bg':
            if domino.c2!=self.plateauv.contenu[0].c1:
                return('coup impossible')
        if s=='hd':
            if domino.c1!=self.plateauv.contenu[-1].c2:
                return('coup impossible')
        if s=='bd':
            if domino.c1!=self.plateauv.contenu[-1].c2:
                return('coup impossible')







#    def creerJoueurs(self,nb=2):
#        j1=Joueur(1,[])
#        j2=Joueur(2,[])
#        return [j1,j2]



    def distribution(self):
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
        domino=self.pioche.contenu.pop(-1)
        domino.etat=''+str(j)
        j.contenu.append(domino)





    def peutJouer(self,j):
        if j == 1:

            L=self.j1.contenu
            s=0
            for domino in L:
                if self.testAjouteDomino(domino,'g')=='coup impossible' and self.testAjouteDomino(domino,'d')=='coup impossible' and self.testAjouteDomino(domino,'hd')=='coup impossible' and self.testAjouteDomino(domino,'bd')=='coup impossible' and self.testAjouteDomino(domino,'hg')=='coup impossible'and self.testAjouteDomino(domino,'bg')=='coup impossible' and self.testAjouteDomino(domino,'g')=='coup impossible' and self.testAjouteDomino(domino.permute(),'d')=='coup impossible' and self.testAjouteDomino(domino.permute(),'hd')=='coup impossible' and self.testAjouteDomino(domino.permute(),'bd')=='coup impossible' and self.testAjouteDomino(domino.permute(),'hg')=='coup impossible'and self.testAjouteDomino(domino.permute(),'bg')=='coup impossible':
                    s+=1
            if s==len(L):
                return False
            else:

                return True

        if j == 2:
            L=self.j2.contenu
            s=0
            for domino in L:
                if self.testAjouteDomino(domino,'g')=='coup impossible' and self.testAjouteDomino(domino,'d')=='coup impossible' and self.testAjouteDomino(domino,'hd')=='coup impossible' and self.testAjouteDomino(domino,'bd')=='coup impossible' and self.testAjouteDomino(domino,'hg')=='coup impossible'and self.testAjouteDomino(domino,'bg')=='coup impossible' and self.testAjouteDomino(domino,'g')=='coup impossible' and self.testAjouteDomino(domino.permute(),'d')=='coup impossible' and self.testAjouteDomino(domino.permute(),'hd')=='coup impossible' and self.testAjouteDomino(domino.permute(),'bd')=='coup impossible' and self.testAjouteDomino(domino.permute(),'hg')=='coup impossible'and self.testAjouteDomino(domino.permute(),'bg')=='coup impossible':
                    s+=1
            if s==len(L):
                return False
            return True

    def premierTour(self):

            if self.j1.monDoubleLePlusFort()>self.j2.monDoubleLePlusFort():
                print(self.j1)
                print("C'est au joueur 1 de commencer: ")
                x=input()
                x = int(x)
                a=self.j1.contenu[x]
                self.plateau.contenu[7][7]=a
                self.plateauv.contenu.append(a)
                self.j1.contenu[x].etat='plateau'
                self.j1.contenu.pop(x)

                return 1

            if self.j2.monDoubleLePlusFort()>self.j1.monDoubleLePlusFort():
                print(self.j2)
                print("C'est au joueur 2 de commencer: ")
                x=input()
                x = int(x)
                a=self.j2.contenu[x]
                self.plateau.contenu[7][7]=a
                self.plateauv.contenu.append(a)
                self.j2.contenu[x].etat='plateau'
                self.j2.contenu.pop(x)
                return 2


    # def j1Joue(self):
    #     print(self.plateau)
    #     print(self.plateauv)
    #     print(self.j1)
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


    def j2Joue(self):
        print(self.plateau)
        print(self.plateauv)
        print(self.j2)
        x = input()
        x=x.split(',')
        print(x)
        if len(x)==5:
            if x[4]=='r':
                self.ajouteDomino(self.j2.contenu[int(x[0])].permute(),x[1],int(x[2]),int(x[3]))
            else:
                self.ajouteDomino(self.j2.contenu[int(x[0])],x[1],int(x[2]),int(x[3]))
        else:
            print('erreur saisie')
            return self.j2Joue()


    


class TestDomino(unittest.TestCase):
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
        print(cr.plateau)


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

        cr=Croupier()
        cr.distribution()
        
  #unittest.main()