from ..utils.vetor_ordenado import VetorOrdenado

class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, origem):
        print("--------------")
        print("Cidade Atual: {}".format(origem.rotulo))
        origem.visitado = True

        if(origem == self.objetivo):
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(origem.adjacentes))
            for adjacente in origem.adjacentes:
                if adjacente.cidade.visitado == False:
                    adjacente.cidade.visitado = True
                    vetor_ordenado.insere(adjacente)

            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].cidade)