from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        vertices_nao_adj = set()

        for v in range(len(self.vertices)):
            for w in range(v + 1, len(self.vertices)):
                if len(self.matriz[v][w]) == 0:
                    vertices_nao_adj.add(f'{self.vertices[v].rotulo}-{self.vertices[w].rotulo}')
        return vertices_nao_adj
                    

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.vertices)):
            if len(self.matriz[i][i]) > 0:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        soma = 0
        index_de_v = self.indice_do_vertice(self.get_vertice(V))
        linha = self.matriz[index_de_v]
        for i in range(len(self.vertices)):
            soma += len(linha[i])
            if index_de_v == i:
                soma += len(linha[i])
        return soma

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for v in range(len(self.vertices)):
            for w in range(len(self.vertices)):
                if len(self.matriz[v][w]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        arestas = set()
        index = self.indice_do_vertice(self.get_vertice(V))
        for v in range(len(self.vertices)):
            for key in self.matriz[v][index]:
                arestas.add(key)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for v in range(len(self.vertices)):
            for u in range(len(self.vertices)):
                if (u == v and len(self.matriz[v][u]) != 0) or (u != v and len(self.matriz[v][u]) != 1):
                    return False
        return True