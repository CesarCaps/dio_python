'''João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie ujm programa onde João informe: cor, modelo, ano, e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.'''

from time import sleep
class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
 
    def buzinar(self):
        print("plim plim...")
        sleep(2)
    
    def parar(self):
        print("parando a bicicleta...")
        sleep(2)
        print("bicicleta parada!")
        sleep(1)

    def correr(self):
        print("iniciando movimento...")
        sleep(2)
        print("bicicleta em movimento!")
        print("vruuuuuum...")
        sleep(2)


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor
                                                             in self.__dict__.items()])}"

bike1 = bicicleta('vermelha', 'caloi', 2022, 600)
bike1.buzinar()
bike1.correr()
bike1.parar()
print(bike1)