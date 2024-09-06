
from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()#title garante a impressão com a inicial maiúscula
        self._categoria = categoria.upper() #upper garante a impressão e todas as letras maiúsculas
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome}    |   {self.categoria}'
    
    @classmethod #Indica que o método pertence a class
    def listar_restaurantes(cls):#cls no parêntesis sempre que usar o @classmethod
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: # .cls para informara que se trata da lista que pertence  classe Restaurante
            print (f'{restaurante._nome.ljust(25)} | {str(restaurante.media_avaliacoes.ljust)} | {restaurante._ativo}')

    #o property nos permite pegar o atributo de uma classe e mudar a forma como ele vai ser lido.
    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'

    def alternar_estado(self): #não é um método da classe por isso não usamos o classmethod. É um metodo para os objetos
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        #O IF esta condicionando que o usuario deve escolher nota entre 0 e 5 para o codigo rodar
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    #o Property permite ler as informações deste metodo para cada restaurante cadastrado
    @property 
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        #sum esta somando as notas (avaliacao._nota) de cada avaliação(da lista avaliação) 
        #realizada em self._avaliacao
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        #len indica a quantidde de notas já recebidas
        quantidade_de_nota = len(self._avaliacao)

        #round é a funcao que vai ajudar a determinar que se imprima apenas uma casa decimal 
        #apos a virgula. O 1 no final informa a quantidade de digito apos a virgura
        media = round(soma_das_notas / quantidade_de_nota, 1)
        return media





    


