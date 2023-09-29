
import os
import random
from functools import reduce

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    def jugar(self):
        # Lógica para jugar
        pass

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        mapa, inicio, fin = self.cargar_mapa()
        super().__init__(mapa, inicio, fin)

    def cargar_mapa(self):
        archivos = os.listdir(self.path_a_mapas)
        archivo_elegido = random.choice(archivos)
        path_completo = f"{self.path_a_mapas}/{archivo_elegido}"
        
        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
            dimensiones = lineas[0].strip().split('x')
            ancho, alto = int(dimensiones[0]), int(dimensiones[1])
            inicio = tuple(map(int, lineas[1].strip().split(',')))
            fin = tuple(map(int, lineas[2].strip().split(',')))
            mapa_cadena = reduce(lambda x, y: x + y, lineas[3:])
            mapa = list(map(list, mapa_cadena.strip().split('\n')))
        
        return mapa, inicio, fin

if __name__ == "__main__":
    juego = JuegoArchivo("path_a_tus_mapas")
    juego.jugar()