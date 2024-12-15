from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
from bibgrafo.vertice import Vertice

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self) -> set:
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

    def ha_laco(self) -> bool:
        """
        Verifica se existe algum laço no grafo.

        :return: Um valor booleano que indica se existe algum laço.
        """
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V: str ='') -> int:
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

    def ha_paralelas(self) -> bool:
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

    def arestas_sobre_vertice(self, V: str = '') -> set:
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

    def eh_completo(self) -> bool:
        """
        Verifica se o grafo é completo.

        :return: Um valor booleano que indica se o grafo é completo
        """
        if self.ha_laco() or self.ha_paralelas():
            return False

        tam = len(self.vertices)
        for i in range(tam):
            for j in range(i + 1, tam):
                u, v = self.vertices[i], self.vertices[j]
                for a in self.arestas:
                    if (self.arestas[a].v1 == u and self.arestas[a].v2 == v) or (self.arestas[a].v2 == u and self.arestas[a].v1 == v):
                        break
                else:
                    return False
        return True

    def dfs(self, V: str ='') -> 'MeuGrafo':
        """
        Realiza a busca em profundidade (DFS) a partir do vértice passado como parâmetro e retorna a árvore DFS.

        :param V: Uma string com o rótulo do vértice raiz da árvore DFS.
        :return: Um grafo do tipo MeuGrafo contendo apenas as arestas que fazem parte da árvore DFS.
        :raises: VerticeInvalidoException se o vértice não existe no grafo.
        """
        pilha_atual = [V]
        solucao = MeuGrafo()

        solucao.adiciona_vertice(V)
        while len(pilha_atual) > 0:
            for aresta in self.arestas:
                if self.arestas[aresta].v1.rotulo == pilha_atual[-1] and not solucao.existe_rotulo_vertice(self.arestas[aresta].v2.rotulo):
                    # visitar V2
                    solucao.adiciona_vertice(self.arestas[aresta].v2.rotulo)
                    solucao.adiciona_aresta(self.arestas[aresta])
                    pilha_atual.append(self.arestas[aresta].v2.rotulo)
                    break

                if self.arestas[aresta].v2.rotulo == pilha_atual[-1] and not solucao.existe_rotulo_vertice(self.arestas[aresta].v1.rotulo):
                    # visitar V1
                    solucao.adiciona_vertice(self.arestas[aresta].v1.rotulo)
                    solucao.adiciona_aresta(self.arestas[aresta])
                    pilha_atual.append(self.arestas[aresta].v1.rotulo)
                    break
            else:
                pilha_atual.pop()
        
        return solucao
    
    def bfs(self, V: str ='') -> 'MeuGrafo':
        """
        Realiza a busca em largura (BFS) a partir do vértice passado como parâmetro e retorna a árvore BFS.

        :param V: Uma string com o rótulo do vértice raiz da árvore BFS.
        :return: Um grafo do tipo MeuGrafo contendo apenas as arestas que fazem parte da árvore BFS.
        :raises: VerticeInvalidoError se o vértice não existe no grafo.
        """
        fila_atual = [V]
        solucao = MeuGrafo()

        solucao.adiciona_vertice(V)
        while len(fila_atual) > 0:
            for aresta in self.arestas:
                if self.arestas[aresta].v1.rotulo == fila_atual[0] and not solucao.existe_rotulo_vertice(self.arestas[aresta].v2.rotulo):
                    solucao.adiciona_vertice(self.arestas[aresta].v2.rotulo)
                    solucao.adiciona_aresta(self.arestas[aresta])
                    fila_atual.append(self.arestas[aresta].v2.rotulo)

                if self.arestas[aresta].v2.rotulo == fila_atual[0] and not solucao.existe_rotulo_vertice(self.arestas[aresta].v1.rotulo):
                    solucao.adiciona_vertice(self.arestas[aresta].v1.rotulo)
                    solucao.adiciona_aresta(self.arestas[aresta])
                    fila_atual.append(self.arestas[aresta].v1.rotulo)

            fila_atual = fila_atual[1:]
        
        return solucao

    def ha_ciclo(self) -> (bool | list):
        """
        Verifica se há um ciclo no grafo e, se houver, retorna a sequência de vértices e arestas do ciclo.
        :return:
            False: se não houver ciclo no grafo.
            List: uma lista no formato [v1, a1, v2, a2, ..., vn, an, v1], representando o ciclo.
        """
        for v in self.vertices:
            solucao = [v.rotulo]
            v_visitados = {v.rotulo: False for v in self.vertices}
            a_visitadas = {a: False for a in self.arestas}

            while len(solucao) > 0:
                atual = solucao[-1]
                v_visitados[atual] = True

                for a in sorted(list(self.arestas)):
                    if a_visitadas[a]:
                        continue

                    aresta = self.arestas[a]
                    
                    if aresta.v1.rotulo == atual:
                        solucao.append(aresta.rotulo)
                        solucao.append(aresta.v2.rotulo)
                        if not v_visitados[aresta.v2.rotulo]:
                            v_visitados[aresta.v2.rotulo] = True
                            a_visitadas[a] = True
                            break
                        else: 
                            return solucao[solucao.index(aresta.v2.rotulo):]
                    
                    if aresta.v2.rotulo == atual: 
                        solucao.append(aresta.rotulo)
                        solucao.append(aresta.v1.rotulo)

                        if not v_visitados[aresta.v1.rotulo]:
                            v_visitados[aresta.v1.rotulo] = True
                            a_visitadas[a] = True

                            break
                        else: 
                            return solucao[solucao.index(aresta.v1.rotulo):]
                        
                else:
                    solucao.pop()
                    if len(solucao) == 0:
                        continue
                    solucao.pop()
        return False
    
    def vizinho(self, vertice: str, aresta: str) -> str:
        """
        Retorna o vértice vizinho conectado ao vértice passado pela aresta especificada.

        :param vertice: O rótulo do vértice atual.
        :param aresta: O rótulo da aresta que conecta o vértice a um vizinho.
        :return: O rótulo do vértice vizinho.
        :raises: ArestaInvalidaError se a aresta não existir no grafo.
        :raises: VerticeInvalidoError se o vértice não estiver conectado à aresta.
        """
        if aresta not in self.arestas.keys():
            raise ArestaInvalidaError(f"Aresta '{aresta}' não existe no grafo.")

        v1 = self.arestas[aresta].v1.rotulo
        v2 = self.arestas[aresta].v2.rotulo

        if vertice == v1:
            return v2
        elif vertice == v2:
            return v1
        else:
            raise VerticeInvalidoError(f"Vértice '{vertice}' não está conectado à aresta '{aresta}'.")

    def caminho(self, n: int) -> (None | list):
        """
        Encontra um caminho de comprimento n (número de arestas) no grafo.

        :param n: Um inteiro que representa o comprimento do caminho desejado.
        :return:
            - Uma lista no formato [v1, a1, v2, a2, ...], representando o caminho.
            - None, se não houver caminho com o comprimento desejado.
        """

        def maior_caminho_entre(v1: str, v2: str) -> list:
            """
            Encontra o maior caminho entre dois vértices.

            :param v1: Rótulo do vértice inicial.
            :param v2: Rótulo do vértice final.
            :return: Lista com o maior caminho encontrado.
            """

            def dfs(atual: str, visitados: list) -> list:
                """
                Realiza uma busca em profundidade para encontrar o maior caminho possível a partir de um vértice.

                :param atual: Rótulo do vértice atual.
                :param visitados: Lista de rótulos dos vértices visitados.
                :return: Lista com o maior caminho encontrado.
                """
                maior_caminho = visitados[:]
                for aresta in sorted(self.arestas_sobre_vertice(atual)):
                    vizinho = self.vizinho(atual, aresta)
                    if vizinho not in visitados:
                        novo_caminho = dfs(vizinho, visitados + [aresta, vizinho])
                        if len(novo_caminho) > len(maior_caminho):
                            maior_caminho = novo_caminho
                return maior_caminho

            return dfs(v1, [v1])

        for v1 in self.vertices:
            for v2 in self.vertices:
                maior = maior_caminho_entre(v1.rotulo, v2.rotulo)
                if maior is not None and len(maior) >= 2 * n + 1:
                    return maior[:2 * n + 1]

        return None
    
    def conexo(self) -> bool:
        """
        Verifica se o grafo é conexo.
        :return: True se o grafo for conexo, False caso contrário.
        """
        return sorted([v.rotulo for v in self.bfs(self.vertices[0].rotulo).vertices]) == sorted([v.rotulo for v in self.vertices])
