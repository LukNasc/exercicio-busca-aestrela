from src.classes.grafo import Grafo
from src.classes.busca_aestrela import BuscaAEstrela

grafo = Grafo()
busca_aestrela = BuscaAEstrela(grafo.curitiba)

grafo.inicia_grafo()
busca_aestrela.buscar(grafo.porto_uniao)



