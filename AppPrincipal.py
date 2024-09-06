#arquivo principal para rodar os códigos desenvolidos na classe Restaurante.
#o From importa a classe Restaurante de dentro do arquivo restaurante 
#que está dentro da pasta modelo(modelo.restaurante)

from Modelos.restaurante import Restaurante

#criando os restaurantes
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Janaina', 5)
restaurante_praca.receber_avaliacao('Nicolas', 3)
restaurante_praca.receber_avaliacao('Rogerio', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()  