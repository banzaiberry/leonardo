#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,time,datetime,os,logging
from pprint import pprint as pp
import random

INFILE='/Users/paolo/myhowto/edu/data/NomiCognomi.txt'
SEP = '\t'

MAIL = ['@gmail.com','@libero.it','@virgilio.it']
YEAR = [1998,1999,2000]
MATERIE=['matematica','italiano','storia','geografia','scienze','inglese','francese','latino']
MINVOTO=3
MAXVOTO=10
SUFF=6
PERCSUFF=50.0

NOMI_MASCHILI = set(['Luca','Mattia','Andrea','Elia','Gianluca'])


def randBuild(inList):
    i = random.randint(0,len(inList)-1)
    return inList[i]

def randData():
    valid = True
    retD = None
    while valid:
        y = randBuild(YEAR)
        m = random.randint(1,12)
        d = random.randint(1,31)
        try:
            retD = datetime.datetime(y,m,d)
            valid = False
        except:
            pass

    return retD.strftime("%Y-%m-%d")

def randMaterie():
    ret = dict()

    numSuff=0
    first = random.randint(MINVOTO,MAXVOTO)
    if first > 5:
        minV = 6
    else:
        minV = MINVOTO

    #print "FIRST:",minV
    for x in MATERIE:
        voto = random.randint(minV,MAXVOTO)
        ret[x]= str(voto)
        if voto >= SUFF:
            numSuff += 1

    percSuff = 100.0*float(numSuff)/float(len(MATERIE))

    retEsito = "promosso"
    esito = True
    if percSuff < PERCSUFF:
        retEsito = "non ammesso"
        esito = False
        #print "percSuff:%2.2f"%percSuff

    # trim voto
    if not esito:
        for x in MATERIE:
            if int(ret[x])>7:
                ret[x]='7'


    return ret,retEsito

def controllaSesso(nome):
   if nome.endswith('a') and nome not in NOMI_MASCHILI:
      return 'F'
   else:
      return 'M'
   
def doAll():
    fi = open(INFILE,'r')
    for line in fi:
        #print "----------------------------------------------------------------------------------------------"
        x = line.strip()
        tmp = x.split(',')
        if len(tmp) == 2:
            nome = tmp[0]
            cognome = tmp[1]

        mail = "%s.%s%s"%(nome.lower(),cognome.lower(),randBuild(MAIL))
        sesso = controllaSesso(nome)
        dob = randData()
        voti,esito = randMaterie()

        #votiStr = ''
        #for i in voti:
        v = SEP.join(voti.values())

        print "NULL"+SEP+nome+SEP+cognome+SEP+sesso+SEP+mail+SEP+dob+SEP+v+SEP+esito

    fi.close()



##########################################################################
if __name__ == "__main__":

    doAll()
