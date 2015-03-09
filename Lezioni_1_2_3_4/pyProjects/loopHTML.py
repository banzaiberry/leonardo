# -*- encoding: utf-8 -*-
#Esempio che mostra il loop e le chiamate a finzioni esterne

import math
import time


NLOOP=1000;

HEADER="""
<!DOCTYPE html>
<html>

<head>
<style>


table {
    width:40%;
    margin-left:auto;
    margin-right:auto;
}

table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    text-align: left;
}
table#t01 tr:nth-child(even) {
    background-color: #eee;
    //background-color:rgb(255,251,217);
}
table#t01 tr:nth-child(odd) {
   background-color:#fff;

}
table#t01 th	{
    background-color: black;
    color: white;
}
</style>
</head>

<body>

<center><h1>Tabella</h1></center>
<table id="t01">

  <tr>
    <th>Input</th>
    <th>Quadrato</th>
    <th>Cubo</th>
    <th>Radice</th>
  </tr>
"""


FOOTER="""
</table>
</body>
</html>
"""

OUTFILE="index.html"

if __name__ == '__main__':

    print "Begin loop"
    fo = open(OUTFILE,'w')
    fo.write(HEADER)

    start = time.time()*1000.0

    for i in range(1,NLOOP+1):
        p2 = long(math.pow(i,2.0))
        p3 = long(math.pow(i,3.0))
        sq = math.sqrt(i)
        print "%d\t%d\t%d\tRADICE:%5.3f"%(i,p2,p3,sq)
        print "-"*80
        line = "<tr> <td>%d</td> <td>%d</td> <td>%d</td> <td>%5.3f</td> </tr>"%(i,p2,p3,sq)
        fo.write("%s\n"%line)

    print "End loop"
    fo.write(FOOTER)
    fo.close()
    stop = time.time()*1000.0
    time_spent = stop - start
    print "Created output file %s"%OUTFILE
    print "Done in %3.2f millsec"%time_spent