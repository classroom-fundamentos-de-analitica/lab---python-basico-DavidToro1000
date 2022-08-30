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


# def pregunta_05():
#     """
#     Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
#     letra de la columa 1.

#     Rta/
#     [
#         ("A", 9, 2),
#         ("B", 9, 1),
#         ("C", 9, 0),
#         ("D", 8, 3),
#         ("E", 9, 1),
#     ]

#     """
#     return


# def pregunta_06():
#     """
#     La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
#     una clave y el valor despues del caracter `:` corresponde al valor asociado a la
#     clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
#     grande computados sobre todo el archivo.

#     Rta/
#     [
#         ("aaa", 1, 9),
#         ("bbb", 1, 9),
#         ("ccc", 1, 10),
#         ("ddd", 0, 9),
#         ("eee", 1, 7),
#         ("fff", 0, 9),
#         ("ggg", 3, 10),
#         ("hhh", 0, 9),
#         ("iii", 0, 9),
#         ("jjj", 5, 17),
#     ]

#     """
#     return


# def pregunta_07():
#     """
#     Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
#     valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
#     a dicho valor de la columna 2.

#     Rta/
#     [
#         (0, ["C"]),
#         (1, ["E", "B", "E"]),
#         (2, ["A", "E"]),
#         (3, ["A", "B", "D", "E", "E", "D"]),
#         (4, ["E", "B"]),
#         (5, ["B", "C", "D", "D", "E", "E", "E"]),
#         (6, ["C", "E", "A", "B"]),
#         (7, ["A", "C", "E", "D"]),
#         (8, ["E", "D", "E", "A", "B"]),
#         (9, ["A", "B", "E", "A", "A", "C"]),
#     ]

#     """
#     return


# def pregunta_08():
#     """
#     Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
#     de la segunda columna; la segunda parte de la tupla es una lista con las letras
#     (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
#     valor de la segunda columna.

#     Rta/
#     [
#         (0, ["C"]),
#         (1, ["B", "E"]),
#         (2, ["A", "E"]),
#         (3, ["A", "B", "D", "E"]),
#         (4, ["B", "E"]),
#         (5, ["B", "C", "D", "E"]),
#         (6, ["A", "B", "C", "E"]),
#         (7, ["A", "C", "D", "E"]),
#         (8, ["A", "B", "D", "E"]),
#         (9, ["A", "B", "C", "E"]),
#     ]

#     """
#     return


# def pregunta_09():
#     """
#     Retorne un diccionario que contenga la cantidad de registros en que aparece cada
#     clave de la columna 5.

#     Rta/
#     {
#         "aaa": 13,
#         "bbb": 16,
#         "ccc": 23,
#         "ddd": 23,
#         "eee": 15,
#         "fff": 20,
#         "ggg": 13,
#         "hhh": 16,
#         "iii": 18,
#         "jjj": 18,
#     }

#     """
#     return


# def pregunta_10():
#     """
#     Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
#     cantidad de elementos de las columnas 4 y 5.

#     Rta/
#     [
#         ("E", 3, 5),
#         ("A", 3, 4),
#         ("B", 4, 4),
#         ...
#         ("C", 4, 3),
#         ("E", 2, 3),
#         ("E", 3, 3),
#     ]


#     """
#     return


# def pregunta_11():
#     """
#     Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
#     columna 4, ordenadas alfabeticamente.

#     Rta/
#     {
#         "a": 122,
#         "b": 49,
#         "c": 91,
#         "d": 73,
#         "e": 86,
#         "f": 134,
#         "g": 35,
#     }


#     """
#     return


# def pregunta_12():
#     """
#     Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
#     los valores de la columna 5 sobre todo el archivo.

#     Rta/
#     {
#         'A': 177,
#         'B': 187,
#         'C': 114,
#         'D': 136,
#         'E': 324
#     }

#     """
#     return
