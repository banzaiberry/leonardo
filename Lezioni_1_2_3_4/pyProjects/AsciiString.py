# -*- encoding: utf-8 -*-
#Esempio che mostra la generazione del codice ASCII di una stringa

inString = "Liceo Scientifico Leoardo Da Vinci."

print "[Glyph]:Dec\tBinary\n"
for c in inString:
    print "[%s]:\t%d\t%s"%(c,ord(c),bin(ord(c))[2:])