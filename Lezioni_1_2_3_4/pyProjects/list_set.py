# -*- encoding: utf-8 -*-
#Esempio che mostra cosa sono le liste, i set e i dictionary

l1 =['a','b','c','d','e','f']
l2 =['c','e','m','n']
l3 = [22,345,753,9,12,101]
l4 = ['ciao','a','tutti']

set1 = set(l1)
set2 = set(l2)

dict1 = {'Marco Tombari':7,'Sandro Silvestri':8, 'Alberto Sica':6}

if __name__ == '__main__':
    for x in l1:
        print x

    print set1.intersection(set2)
    print set1.union(set2)
    print set1.difference(set2)

    print "XXX".join(l4)

    for k in dict1:
        print "il voto di %s è %d"%(k,dict1[k])
