from collections import deque
from typing import Deque

class Pilha:
    def __init__(self):
        self.elementos = []

    def empilha(self, elemento):
        self.elementos.append(elemento)

    def desempilha(self):
        if self.vazio():
            raise IndexError("A pilha está vazia.")
        return self.elementos.pop()

    def vazio(self):
        return len(self.elementos) == 0

    def __str__(self):
        retorno = "\nPilha (Topo para Base)\n"
        for i, elemento in enumerate(reversed(self.elementos)):
            retorno += f"{len(self.elementos) - 1 - i} - {elemento}\n"
        return retorno


class Fila:
    def __init__(self):
        self.elementos: Deque[int] = deque()

    def incluirNaFila(self, elemento):
        self.elementos.append(elemento)

    def incluirMuitosNaFila(self, variosElementos: list):
        for elemento in variosElementos:
            self.elementos.append(elemento)

    def retirarDaFila(self):
        if self.vazio():
            raise IndexError("A fila está vazia.")
        return self.elementos.popleft()

    def vazio(self):
        return len(self.elementos) == 0

    def __str__(self):
        retorno = "\nFila (Frente para Trás)\n"
        for i, elemento in enumerate(self.elementos):
            retorno += f"{i} - {elemento}\n"
        return retorno


# Exemplo de uso
if __name__ == "__main__":
    # Testando a pilha
    pilha = Pilha()
    pilha.empilha("A")
    pilha.empilha("B")
    pilha.empilha("C")
    print(pilha)
    print("Desempilhado:", pilha.desempilha())
    print(pilha)

    # Testando a fila
    fila = Fila()
    fila.incluirNaFila("X")
    fila.incluirMuitosNaFila(["Y", "Z"])
    print(fila)
    print("Retirado da fila:", fila.retirarDaFila())
    print(fila)
