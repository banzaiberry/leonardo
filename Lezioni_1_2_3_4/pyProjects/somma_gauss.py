# -*- encoding: utf-8 -*-
#Esempio che mostra il calcolo della somma Gaussiana calcolata in due modi diversi

N = 100


def calcSommaGauss(n):
    somma = n*(n+1)/2
    return somma

if __name__ == '__main__':

    print

    somma = 0
    for i in range(0,N+1):
        somma += i
        print i,somma

    print "somma: %d"%somma

    x = calcSommaGauss(N)
    print "somma Gauss: %d"%x