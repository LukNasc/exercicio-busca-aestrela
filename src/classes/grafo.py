from .cidade import Cidade
from .adjacente import Adjacente

class Grafo:
    porto_uniao = Cidade("Porto União", 203)
    paulo_frontin = Cidade("Paulo Frontin", 172)
    canoinhas = Cidade("Canoinhas", 141)
    tres_barras = Cidade("Tres Barras", 131)
    sao_mateus_do_sul = Cidade("São Mateus do Sul", 123)
    irati = Cidade("Irati", 139)
    curitiba = Cidade("Curitiba", 0)
    palmeira = Cidade("Palmeira", 59)
    mafra = Cidade("Mafra", 94)
    campo_largo = Cidade("Campo Largo", 27)
    balsa_nova = Cidade("Balsa Nova", 41)
    lapa = Cidade("Lapa", 74)
    tijucas_do_sul = Cidade("Tijucas do Sul", 56)
    araucaria = Cidade("Araucária", 23)
    sao_jose_dos_pinhais = Cidade("São José dos Pinhais", 13)
    contenda = Cidade("Contenda", 39)

    def inicia_grafo(self):
        #adicionando adjacentes de porto uniao
        self.porto_uniao.adiciona_adjacente(Adjacente(self.paulo_frontin, 46))
        self.porto_uniao.adiciona_adjacente(Adjacente(self.sao_mateus_do_sul, 83))
        self.porto_uniao.adiciona_adjacente(Adjacente(self.canoinhas, 78))

        #adicionando adjacentes de paulo frontin
        self.paulo_frontin.adiciona_adjacente(Adjacente(self.porto_uniao, 46))
        self.paulo_frontin.adiciona_adjacente(Adjacente(self.irati, 75))

        #adicionando adjacentes de canoinhas
        self.canoinhas.adiciona_adjacente(Adjacente(self.porto_uniao, 78))
        self.canoinhas.adiciona_adjacente(Adjacente(self.tres_barras, 12))
        self.canoinhas.adiciona_adjacente(Adjacente(self.mafra, 66))

        #adicionando adjacentes de tres barras
        self.tres_barras.adiciona_adjacente(Adjacente(self.canoinhas, 12))
        self.tres_barras.adiciona_adjacente(Adjacente(self.sao_mateus_do_sul, 43))

        #adicionando adjacentes de sao mateus do sul
        self.sao_mateus_do_sul.adiciona_adjacente(Adjacente(self.tres_barras, 43))
        self.sao_mateus_do_sul.adiciona_adjacente(Adjacente(self.porto_uniao, 83))
        self.sao_mateus_do_sul.adiciona_adjacente(Adjacente(self.irati, 57))
        self.sao_mateus_do_sul.adiciona_adjacente(Adjacente(self.palmeira, 77))
        self.sao_mateus_do_sul.adiciona_adjacente(Adjacente(self.lapa, 60))

        #adicionando adjacentes de irati
        self.irati.adiciona_adjacente(Adjacente(self.paulo_frontin, 75))
        self.irati.adiciona_adjacente(Adjacente(self.sao_mateus_do_sul, 57))
        self.irati.adiciona_adjacente(Adjacente(self.palmeira, 75))

        #adicionando adjacentes de curitiba
        self.curitiba.adiciona_adjacente(Adjacente(self.campo_largo, 29))
        self.curitiba.adiciona_adjacente(Adjacente(self.balsa_nova, 51))
        self.curitiba.adiciona_adjacente(Adjacente(self.araucaria, 37))
        self.curitiba.adiciona_adjacente(Adjacente(self.sao_jose_dos_pinhais, 15))

        #adicionando adjacentes de palmeira
        self.palmeira.adiciona_adjacente(Adjacente(self.irati, 75))
        self.palmeira.adiciona_adjacente(Adjacente(self.sao_mateus_do_sul, 77))
        self.palmeira.adiciona_adjacente(Adjacente(self.campo_largo, 55))

        #adicionando adjacentes de mafra
        self.mafra.adiciona_adjacente(Adjacente(self.canoinhas, 66))
        self.mafra.adiciona_adjacente(Adjacente(self.lapa, 57))
        self.mafra.adiciona_adjacente(Adjacente(self.tijucas_do_sul, 99))

        #adicionando adjacentes de campo largo
        self.campo_largo.adiciona_adjacente(Adjacente(self.palmeira, 55))
        self.campo_largo.adiciona_adjacente(Adjacente(self.balsa_nova, 22))
        self.campo_largo.adiciona_adjacente(Adjacente(self.curitiba, 29))

        #adicionando adjacentes de balsa nova
        self.balsa_nova.adiciona_adjacente(Adjacente(self.campo_largo, 22))
        self.balsa_nova.adiciona_adjacente(Adjacente(self.contenda, 19))
        self.balsa_nova.adiciona_adjacente(Adjacente(self.curitiba, 51))

        #adicionando adjacentes de lapa
        self.lapa.adiciona_adjacente(Adjacente(self.sao_mateus_do_sul, 60))
        self.lapa.adiciona_adjacente(Adjacente(self.contenda, 26))
        self.lapa.adiciona_adjacente(Adjacente(self.mafra, 57))

        #adicionando adjacentes de tijucas do sul
        self.tijucas_do_sul.adiciona_adjacente(Adjacente(self.mafra, 99))
        self.tijucas_do_sul.adiciona_adjacente(Adjacente(self.sao_jose_dos_pinhais, 49))

        #adicionando adjacentes de araucaria
        self.araucaria.adiciona_adjacente(Adjacente(self.contenda, 18))
        self.araucaria.adiciona_adjacente(Adjacente(self.curitiba, 37))

        #adicionando adjacentes de sao jose dos pinhais
        self.sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(self.curitiba, 15))
        self.sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(self.tijucas_do_sul, 49))

        #adicionando adjacentes de contenda
        self.contenda.adiciona_adjacente(Adjacente(self.balsa_nova, 19))
        self.contenda.adiciona_adjacente(Adjacente(self.araucaria, 18))
        self.contenda.adiciona_adjacente(Adjacente(self.lapa, 26))
        

    