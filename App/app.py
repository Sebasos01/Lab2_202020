"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Ordenar por ranking")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if lst['size']==0:
        print("La lista esta vacía")
        return 0
    
    else:
        elementos=lt.newList()
        iterator=it.newIterator(lst)
        columna=None
        if column=="1":
            columna="vote_average"
        else:
            columna="vote_count"
        while it.hasNext(iterator):
            elemento=it.next(iterator)
            lt.addLast(elementos,[float(elemento[columna]),int(elemento["id"]),elemento["original_title"]])                          
        if function=="1":
            t1_start = process_time()
            ss.selectionSort(elementos,lessfunction)
            t1_stop = process_time()
            print("Tiempo de ejecución del ordenamiento SELECTION_SORT es ",t1_stop-t1_start," segundos")
        elif function=="2":
            t1_start = process_time()
            Is.insertionSort(elementos,lessfunction)
            t1_stop = process_time()
            print("Tiempo de ejecución del ordenamiento INSERTION_SORT es ",t1_stop-t1_start," segundos")
        else:
            t1_start = process_time()
            shs.shellSort(elementos,lessfunction)
            t1_stop = process_time()
            print("Tiempo de ejecución del ordenamiento SHELL_SORT es ",t1_stop-t1_start," segundos")
        if elements=="1":
            top=lt.subList(elementos,elementos["size"]-9,10)
            iterator_top=it.newIterator(top)
            respuesta=[]
            i=10
            while it.hasNext(iterator_top):
                elemento_top=it.next(iterator_top)
                respuesta.append(str(i)+". "+elemento_top[2]+" con "+columna+" de "+str(elemento_top[0]))
                i-=1
            return respuesta
        else:
            top=lt.subList(elementos,1,10)
            iterator_top=it.newIterator(top)
            respuesta=[]
            i=1
            while it.hasNext(iterator_top):
                elemento_top=it.next(iterator_top)
                respuesta.append(str(i)+". "+elemento_top[2]+" con "+columna+" de "+str(elemento_top[0]))
                i+=1
            return respuesta[::-1]

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/test.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista["size"]==0: #obtener la longitud de la lista
                    print("La lista está vacía")
                else:
                    print("1. VOTE_AVERAGE\n2. VOTE_COUNT")
                    column=input("Ingrese un número: ")
                    while True:
                        if column.isnumeric():
                            if int(column) in range(1,3):
                                break
                        else:
                            function=input("Ingrese una opción válida: ")   
                    print("\n1. SELECTION_SORT\n2. INSERTION_SORT\n3. SHELL_SORT")
                    function=input("Ingrese un número: ")
                    while True:
                        if function.isnumeric():
                            if int(function) in range(1,4):
                                break
                        else:
                            function=input("Ingrese una opción válida: ")             
                    print("\n1. 10_MEJORES\n2. 10_PEORES")
                    elements=input("Ingrese un número: ")
                    while True:
                        if elements.isnumeric():
                            if int(function) in range(1,4):
                                break
                        else:
                            elements=input("Ingrese una opción válida: ")        
                    respuesta=orderElementsByCriteria(function, column, lista, elements)
                    print(respuesta) 
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

def lessfunction(element1, element2):
    if element1<element2:
        return True
    return False                
if __name__ == "__main__":
    main()
