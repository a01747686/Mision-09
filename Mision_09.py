#Samantha Martínez Franco A01747686
#Ejercicios utilizando listas parte dos


#función que regresa nueva lista con solo los pares
def extraerPares(lista):
    listaPares = []
    if lista==[]:
        return lista
    else:
        for dato in lista:
            if dato%2==0:
                listaPares.append(dato)
        return listaPares


#regresa nueva lista con los datos mayores al anterior
def extraerMayoresPrevio(lista):
    nuevaLista=[]
    if lista==[]:
        return lista
    else:
        for k in range(1,len(lista)):
            if lista[k]>lista[k-1]:
                nuevaLista.append(lista[k])
        return nuevaLista


#regresa una nueva lista con cada pareja de datos cambiada
def intercambiarParejas(lista):
    nuevaLista=[]
    if lista==[]:
        return nuevaLista
    elif len(lista)==1:
        nuevaLista.append(lista[0])
        return nuevaLista
    elif len(lista)>1:
        for k in range(1,len(lista),2):
            nuevaLista.append(lista[k])
            nuevaLista.append(lista[k-1])
            if len(lista)%2==1:
                nuevaLista.append(lista[-1])
        return nuevaLista


#regresa la misma lista pero con los datos mayores y menores intercambiados de lugar
def intercambiarMM(lista):
    if lista==[]:
        return []
    minimo=min(lista)
    maximo=max(lista)
    indiceMax=lista.index(maximo)
    indiceMin=lista.index(minimo)
    lista.remove(maximo)
    lista.remove(minimo)
    lista.insert(indiceMin,maximo)
    lista.insert(indiceMax,minimo)
    return lista



def promediarCentro(lista):  #si funciona
    if len(lista)<=2:
        promedio=0
    else:
        copia=lista.copy()
        copia.remove(max(lista))
        copia.remove(min(lista))
        promedio=sum(copia)//len(copia)
    return promedio




def calcularEstadistica(lista):  #si funciona
    suma=0
    if lista==[]:
        return (0,0)
    else:
        for dato in lista:
            promedio = sum(lista) / len(lista)
            divisor=(dato-promedio)**2
            suma+=divisor
        dividendo=len(lista)-1
        desviacion=(suma/dividendo)**0.5
        return promedio,desviacion


def calcularSuma(lista):
    if 13 in lista:
        while lista.count(13)>0:
            indice13=lista.index(13)
            if indice13==0:
                if len(lista)>1:
                    lista.pop(0)
                    lista.pop(0)
                else:
                    lista.pop(0)
            elif indice13==len(lista)-1:
                lista.pop()
                lista.pop()
            else:
                lista.remove(13)
                lista.pop(indice13)
                lista.pop(indice13-1)
            suma=sum(lista)

    elif lista==[]:
        return 0
    else:
        suma=sum(lista)
    return suma


def main():
    print("Ejercicio 1: regresa una lista con los números pares de la lista")
    a1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("La lista ", a1, "regresa ", extraerPares(a1))
    b1 = [5,8,3]
    print("La lista ", b1, "regresa ", extraerPares(b1))
    c1 = []
    print("La lista ", c1, "regresa ", extraerPares(c1))
    d1 = [1, 3, 5, 7]
    print("La lista ", d1, "regresa ", extraerPares(d1))

    print("Ejercicio 2: regresa una lista con los mayores previos de la lista")
    a2 = [1, 2, 3, 2,4,60, 5, 8,3,22,44,55]
    print("Lista original", a2, ", regresa", extraerMayoresPrevio(a2))
    b2 = []
    print("Lista original", b2, ", regresa", extraerMayoresPrevio(b2))
    c2 = [5,4,3,2,1]
    print("Lista original", c2, ", regresa", extraerMayoresPrevio(c2))
    d2 = [34, 55, 35, 65, 3]
    print("Lista original", d2, ", regresa", extraerMayoresPrevio(d2))


    print("ejercicio 3: intercambia cada pareja de de la lista")
    a3 = [1, 2, 3, 2,4,60, 5, 8,3,22,44,55]
    print("¿Los datos de la lista ", a3, "regresa", intercambiarParejas(a3))
    b3 = [1,2,3]
    print("¿Los datos de la lista ", b3, "regresa", intercambiarParejas(b3))
    c3 = [1]
    print("¿Los datos de la lista ", c3, "regresa", intercambiarParejas(c3))
    d3 = []
    print("¿Los datos de la lista ", d3, "regresa", intercambiarParejas(d3))

    print("Ejercicio 4: intercambia los lugares del mayor y el menor  ")
    a4 = [5,9,3,22,19,31,10,7]
    a4c=a4.copy()
    print("La lista ", a4c, "regresa", intercambiarMM(a4))
    b4=[1,2,3]
    b4c=b4.copy()
    print("La lista ", b4c, "regresa", intercambiarMM(b4))
    c4=[]
    c4c=c4.copy()
    print("La lista ", c4c, "regresa", intercambiarMM(c4))
    d4=[1,3,4,5,8,55,23,9]
    d4c=d4.copy()
    print("La lista ", d4c, "regresa", intercambiarMM(d4))

    print("Ejercicio 5: calcula el promedio centro de la lista quitando el mayor y el menor ")
    a5 = [95,21,73,24,15,69,71,80,49,100,85]
    print("La lista ", a5, "su promedio centro es ", promediarCentro(a5))
    b5 = [20,55,30,5,55,5]
    print("La lista ", b5, "su promedio centro es ", promediarCentro(b5))
    c5 = [5,9,1,8]
    print("La lista ", c5, "su promedio centro es ", promediarCentro(c5))
    d5 = [5,8]
    print("La lista ", d5, "su promedio centro es ", promediarCentro(d5))
    e5 = [1]
    print("La lista ", e5, "su promedio centro es ", promediarCentro(e5))
    f5 = []
    print("La lista ", f5, "su promedio centro es ", promediarCentro(f5))


    print("Ejercicio 6: calcula la media y la desviación estandar ")
    a6 = [1,2,3,4,5,6]
    print("La lista ", a6, "su promedio y desviación estandar son ", calcularEstadistica(a6))
    b6 = [95,21,73,24,15,69,71,80,49,100,85]
    print("La lista ", b6, "su promedio y desviación estandar son ", calcularEstadistica(b6))
    c6 = []
    print("La lista ", c6, "su promedio y desviación estandar son ", calcularEstadistica(c6))
    d6 = [5,7,44,9,22]
    print("La lista ", d6, "su promedio y desviación estandar son ", calcularEstadistica(d6))

    print("Ejercicio Extra: suma la lista excepto los que estan al lado del 13")
    a7=[1,2,3,4,5,6]
    a7c=a7.copy()
    print("La lista",a7c,"suma ", calcularSuma(a7))
    b7 = [5,2,13,4,1,6,1,8,4,1,5]
    b7c=b7.copy()
    print("La lista", b7c, "suma ", calcularSuma(b7))
    c7 = [5,2,13,4,1,6,1,8,4,13,1]
    c7c=c7.copy()
    print("La lista", c7c, "suma ", calcularSuma(c7))
    d7 = [13,49,34,4,5,13]
    d7c=d7.copy()
    print("La lista", d7c, "suma ", calcularSuma(d7))
    e7 = []
    e7c=e7.copy()
    print("La lista", e7c, "suma ", calcularSuma(e7))


main()


