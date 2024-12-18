from meu_grafo_lista_adj_nao_dir import MeuGrafo
from bibgrafo.grafo_json import GrafoJSON

grafo = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

print(grafo)
for i in range(1, 8):
    print(f'caminho de tamanho {i}: {grafo.caminho(i)}')

