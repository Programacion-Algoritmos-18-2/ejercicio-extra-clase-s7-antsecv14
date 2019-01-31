class OrdenamientoSeleccion(object):

    def ordenarSeleccion(self, array):
        for x in range(0, len(array)-1):
            maspequenio =x
            for i in range(x+1, len(array)):
                if array[i] < array[maspequenio]:
                    maspequenio = i
            if maspequenio != x:
                temp = array[x]
                array[x] = array[maspequenio]
                array[maspequenio] = temp
                print(array)
        print(array)

    def ordenarInsercion(self, array):
        for x in range(1, len(array)):
            aux = array[x]
            posicion = x
            while posicion > 0 and array[posicion-1] > aux:
                array[posicion] = array[posicion-1]
                posicion = posicion -1
            array[posicion] = aux
            print(array)

        print(array)
