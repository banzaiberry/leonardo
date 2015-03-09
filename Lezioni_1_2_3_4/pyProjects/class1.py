# -*- encoding: utf-8 -*-
#Esempio che mostra come si crea una classe

class Personaggio:
    def __init__(self, nome, cognome, eta, professione, hobby):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.professione = professione
        self.hobby = hobby

    def presentati(self):
        print "Ciao a tutti,\n mi chiamo %s %s, ho %d anni e sono un %s. Il mio hobby è %s.\n"%(self.nome,self.cognome,self.eta,self.professione,self.hobby)

    def menti(self):
        print("Sono un %s e la mia età è %d anni"%(self.professione,self.eta-5))

if __name__ == '__main__':

    pers1 = Personaggio("Matteo", "Renzi",41,"politico","la fotografia")
    pers2 = Personaggio("Francesco", "Totti",36,"calciatore","la cucina")
    pers3 = Personaggio("Gatto", "Silvestro",10,"gatto","mangiare i topi")

    allPers = [pers1,pers2,pers3]

    for x in allPers:
        x.presentati()

    pers1.menti()