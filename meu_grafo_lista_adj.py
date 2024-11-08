from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        """
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        """
        nao_adjacentes = set()

        tam = len(self.vertices)
        for i in range(tam):
            for j in range(i + 1, tam):
                u, v = self.vertices[i], self.vertices[j]
                for a in self.arestas:
                    if (self.arestas[a].v1 == v and self.arestas[a].v2 == u) or (self.arestas[a].v2 == v and self.arestas[a].v1 == u):
                        break
                else:
                    nao_adjacentes.add(f'{u}-{v}')

        return nao_adjacentes

    def ha_laco(self):
        """
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        """
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        """
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        """
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f'Não existe vértice com rótulo "{V}"')

        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                grau += 1
            if self.arestas[a].v2.rotulo == V:
                grau += 1

        return grau

    def ha_paralelas(self):
        """
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        """
        for a in self.arestas:
            for b in self.arestas:
                aresta_a = self.arestas[a]
                aresta_b = self.arestas[b]
                if ((aresta_a.v1 == aresta_b.v1 and aresta_a.v2 == aresta_b.v2) or (aresta_a.v1 == aresta_b.v2 and aresta_a._v2 == aresta_b.v1)) and not aresta_a.rotulo == aresta_b.rotulo and aresta_a.peso == aresta_b.peso:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        """
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        """
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f'Não existe vértice com rótulo "{V}"')

        rotulos = set()
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                rotulos.add(a)
        return rotulos

    def eh_completo(self):
        """
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        """
        pass
