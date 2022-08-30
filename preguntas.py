"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------
base=open("data.csv")
Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
base=open("data.csv")

def pregunta_01():
    suma=0
    for fila in base:
        suma+=int(fila[2])
    return suma


def pregunta_02():
    A=0
    B=0
    C=0
    D=0
    E=0
    for fila in base:
        if fila[0]=="A":
            A+=1
        elif fila[0]=="B":
            B+=1
        elif fila[0]=="C":
            C+=1
        elif fila[0]=="D":
            D+=1
        else:
            E+=1
    return([("A", A), ("B", B), ("C", C), ("D", D), ("E", E)])


def pregunta_03():
    A=0
    B=0
    C=0
    D=0
    E=0
    for fila in base:
        if fila[0]=="A":
            A+=int(fila[2])
        elif fila[0]=="B":
            B+=int(fila[2])
        elif fila[0]=="C":
            C+=int(fila[2])
        elif fila[0]=="D":
            D+=int(fila[2])
        else:
            E+=int(fila[2])
    return([("A", A), ("B", B), ("C", C), ("D", D), ("E", E)])


def pregunta_04():
    A=0
    B=0
    C=0
    D=0
    E=0
    F=0
    G=0
    H=0
    I=0
    J=0
    K=0
    L=0
    for fila in base:
        if fila[9:11]=="01":
            A+=1
        elif fila[9:11]=="02":
            B+=1
        elif fila[9:11]=="03":
            C+=1
        elif fila[9:11]=="04":
            D+=1
        elif fila[9:11]=="05":
            E+=1
        elif fila[9:11]=="06":
            F+=1
        elif fila[9:11]=="07":
            G+=1
        elif fila[9:11]=="08":
            H+=1
        elif fila[9:11]=="09":
            I+=1
        elif fila[9:11]=="10":
            J+=1
        elif fila[9:11]=="11":
            K+=1
        elif fila[9:11]=="12":
            L+=1
    return([("01", A), ("02", B), ("03", C), ("04", D), ("05", E), ("06", F), ("07", G), ("08", H), ("09", I), ("10", J), ("11", K), ("12", L)])


def pregunta_05():
    maxA=0
    minA=50
    maxB=0
    minB=50
    maxC=0
    minC=50
    maxD=0
    minD=50
    maxE=0
    minE=50
    for fila in base:
        if fila[0]=="A":
            if int(fila[2])>maxA:
                maxA=int(fila[2])
            if int(fila[2])<minA:
                minA=int(fila[2])
        elif fila[0]=="B":
            if int(fila[2])>maxB:
                maxB=int(fila[2])
            if int(fila[2])<minB:
                minB=int(fila[2])
        elif fila[0]=="C":
            if int(fila[2])>maxC:
                maxC=int(fila[2])
            if int(fila[2])<minC:
                minC=int(fila[2])
        elif fila[0]=="D":
            if int(fila[2])>maxD:
                maxD=int(fila[2])
            if int(fila[2])<minD:
                minD=int(fila[2])
        else:
            if int(fila[2])>maxE:
                maxE=int(fila[2])
            if int(fila[2])<minE:
                minE=int(fila[2])
    return([("A", maxA, minA), ("B", maxB, minB), ("C", maxC, minC), ("D", maxD, minD), ("E", maxE, minE)])

def pregunta_06():
    import re
    maxA=0
    minA=50
    maxB=0
    minB=50
    maxC=0
    minC=50
    maxD=0
    minD=50
    maxE=0
    minE=50
    maxF=0
    minF=50
    maxG=0
    minG=50
    maxH=0
    minH=50
    maxI=0
    minI=50
    maxJ=0
    minJ=50
    for fila in base:
        x=re.findall("[a-z]{3}:[0-9]*", fila)
        for i in x:
            i=i.split(':')
            if i[0]=="aaa":
                if int(i[1])>maxA:
                    maxA=int(i[1])
                if int(i[1])<minA:
                    minA=int(i[1])
            elif i[0]=="bbb":
                if int(i[1])>maxB:
                    maxB=int(i[1])
                if int(i[1])<minB:
                    minB=int(i[1])
            elif i[0]=="ccc":
                if int(i[1])>maxC:
                    maxC=int(i[1])
                if int(i[1])<minC:
                    minC=int(i[1])
            elif i[0]=="ddd":
                if int(i[1])>maxD:
                    maxD=int(i[1])
                if int(i[1])<minD:
                    minD=int(i[1])
            elif i[0]=="eee":
                if int(i[1])>maxE:
                    maxE=int(i[1])
                if int(i[1])<minE:
                    minE=int(i[1])
            elif i[0]=="fff":
                if int(i[1])>maxF:
                    maxF=int(i[1])
                if int(i[1])<minF:
                    minF=int(i[1])
            elif i[0]=="ggg":
                if int(i[1])>maxG:
                    maxG=int(i[1])
                if int(i[1])<minG:
                    minG=int(i[1])
            elif i[0]=="hhh":
                if int(i[1])>maxH:
                    maxH=int(i[1])
                if int(i[1])<minH:
                    minH=int(i[1])
            elif i[0]=="iii":
                if int(i[1])>maxI:
                    maxI=int(i[1])
                if int(i[1])<minI:
                    minI=int(i[1])
            elif i[0]=="jjj":
                if int(i[1])>maxJ:
                    maxJ=int(i[1])
                if int(i[1])<minJ:
                    minJ=int(i[1])
    return([("aaa", minA, maxA), ("bbb", minB, maxB), ("ccc", minC, maxC), ("ddd", minD, maxD), ("eee", minE, maxE), ("fff", minF, maxF), ("ggg", minG, maxG), ("hhh", minH, maxH), ("iii", minI, maxI), ("jjj", minJ, maxJ)])


def pregunta_07():
    cero=[]
    uno=[]
    dos=[]
    tres=[]
    cuatro=[]
    cinco=[]
    seis=[]
    siete=[]
    ocho=[]
    nueve=[]
    for fila in base:
        if int(fila[2])==0:
            cero.append(fila[0])
        elif int(fila[2])==1:
            uno.append(fila[0])
        elif int(fila[2])==2:
            dos.append(fila[0])
        elif int(fila[2])==3:
            tres.append(fila[0])
        elif int(fila[2])==4:
            cuatro.append(fila[0])
        elif int(fila[2])==5:
            cinco.append(fila[0])
        elif int(fila[2])==6:
            seis.append(fila[0])
        elif int(fila[2])==7:
            siete.append(fila[0])
        elif int(fila[2])==8:
            ocho.append(fila[0])
        elif int(fila[2])==9:
            nueve.append(fila[0])
    return([(0, cero), (1, uno), (2, dos), (3, tres), (4, cuatro), (5, cinco), (6, seis), (7, siete), (8, ocho), (9, nueve)])


def pregunta_08():
    cero=[]
    uno=[]
    dos=[]
    tres=[]
    cuatro=[]
    cinco=[]
    seis=[]
    siete=[]
    ocho=[]
    nueve=[]
    for fila in base:
        if int(fila[2])==0:
            if fila[0] not in cero:
                cero.append(fila[0])
        elif int(fila[2])==1:
            if fila[0] not in uno:
                uno.append(fila[0])
        elif int(fila[2])==2:
            if fila[0] not in dos:
                dos.append(fila[0])
        elif int(fila[2])==3:
            if fila[0] not in tres:
                tres.append(fila[0])
        elif int(fila[2])==4:
            if fila[0] not in cuatro:
                cuatro.append(fila[0])
        elif int(fila[2])==5:
            if fila[0] not in cinco:
                cinco.append(fila[0])
        elif int(fila[2])==6:
            if fila[0] not in seis:
                seis.append(fila[0])
        elif int(fila[2])==7:
            if fila[0] not in siete:
                siete.append(fila[0])
        elif int(fila[2])==8:
            if fila[0] not in ocho:
                ocho.append(fila[0])
        elif int(fila[2])==9:
            if fila[0] not in nueve:
                nueve.append(fila[0])
    return([(0, sorted(cero)), (1, sorted(uno)), (2, sorted(dos)), (3, sorted(tres)), (4, sorted(cuatro)), (5, sorted(cinco)), (6, sorted(seis)), (7, sorted(siete)), (8, sorted(ocho)), (9, sorted(nueve))])


def pregunta_09():
    import re
    A=0
    B=0
    C=0
    D=0
    E=0
    F=0
    G=0
    H=0
    I=0
    J=0
    for fila in base:
        x=re.findall("[a-z]{3}:[0-9]*", fila)
        for i in x:
            i=i.split(':')
            if i[0]=="aaa":
                A+=1
            elif i[0]=="bbb":
                B+=1
            elif i[0]=="ccc":
                C+=1
            elif i[0]=="ddd":
                D+=1
            elif i[0]=="eee":
                E+=1
            elif i[0]=="fff":
                F+=1
            elif i[0]=="ggg":
                G+=1
            elif i[0]=="hhh":
                H+=1
            elif i[0]=="iii":
                I+=1
            elif i[0]=="jjj":
                J+=1
    return({"aaa":A, "bbb":B, "ccc":C, "ddd":D, "eee":E, "fff":F, "ggg":G, "hhh":H, "iii":I, "jjj":J})


def pregunta_10():
    import re
    respuesta=[]
    for fila in base:
        x=re.findall("[a-z]{3}:[0-9]*", fila)
        y=re.findall("[a-z][,\s]", fila)
        respuesta.append((fila[0], len(y), len(x)))
    return(respuesta)


def pregunta_11():
    import re
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    for fila in base:
        y=re.findall("[a-z][,\s]", fila)
        for i in y:
            if i[0]=="a":
                a+=int(fila[2])
            elif i[0]=="b":
                b+=int(fila[2])
            elif i[0]=="c":
                c+=int(fila[2])
            elif i[0]=="d":
                d+=int(fila[2])
            elif i[0]=="e":
                e+=int(fila[2])
            elif i[0]=="f":
                f+=int(fila[2])
            elif i[0]=="g":
                g+=int(fila[2])
    return({"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g})


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import re
    a=0
    b=0
    c=0
    d=0
    e=0
    for fila in base:
        x=re.findall("[a-z]{3}:[0-9]*", fila)
        for i in x:
            i=i.split(':')
            if fila[0]=='A':
                a+=int(i[1])
            elif fila[0]=='B':
                b+=int(i[1])
            elif fila[0]=='C':
                c+=int(i[1])
            elif fila[0]=='D':
                d+=int(i[1])
            elif fila[0]=='E':
                e+=int(i[1])
    return({'A':a, 'B':b, 'C':c, 'D':d, 'E':e})
