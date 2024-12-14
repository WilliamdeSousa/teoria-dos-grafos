from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
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
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
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
            raise VerticeInvalidoError(f'Não existe vértice com rótulo "{V}"')

        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                grau += 1
            if self.arestas[a].v2.rotulo == V:
                grau += 1

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.arestas:
            for b in self.arestas:
                aresta_a = self.arestas[a]
                aresta_b = self.arestas[b]
                if ((aresta_a.v1 == aresta_b.v1 and aresta_a.v2 == aresta_b.v2) or (aresta_a.v1 == aresta_b.v2 and aresta_a._v2 == aresta_b.v1)) and not aresta_a.rotulo == aresta_b.rotulo and aresta_a.peso == aresta_b.peso:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f'Não existe vértice com rótulo "{V}"')

        rotulos = set()
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                rotulos.add(a)
        return rotulos

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
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

    def dfs(self, V=''):
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
    
    def bfs(self, V=''):
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

    def ha_ciclo(self):
        """
        Verifica se há um ciclo no grafo e, se houver, retorna a sequência de vértices e arestas do ciclo.
        :return:
            False: se não houver ciclo no grafo.
            List: uma lista no formato [v1, a1, v2, a2, ..., vn, an, v1], representando o ciclo.
        """
        for v in self.vertices:
            retorno = [v.rotulo]
            v_visitados = {v.rotulo: False for v in self.vertices}
            a_visitadas = {a: False for a in self.arestas}

            while len(retorno) > 0:
                atual = retorno[-1]
                v_visitados[atual] = True

                for a in sorted(list(self.arestas)):  # para cada aresta
                    if a_visitadas[a]:  # se a aresta já foi visitada, pule essa iteração
                        continue

                    aresta = self.arestas[a]
                    
                    if aresta.v1.rotulo == atual:  # se o v1 é o vértice atual
                        retorno.append(aresta.rotulo)
                        retorno.append(aresta.v2.rotulo)
                        if not v_visitados[aresta.v2.rotulo]:  # se o v2 é um vértice não visitado: visitamos
                            v_visitados[aresta.v2.rotulo] = True
                            a_visitadas[a] = True
                            break  # termina o loop e reinicia para verificar as arestas de v2
                        else:  # se o vértice v2 já foi visitado, então é um vértice de retorno, 
                            return retorno[retorno.index(aresta.v2.rotulo):]  # devemos retornar da primeira aparição de v2 até o final.
                    
                    if aresta.v2.rotulo == atual:  # se o v2 é o vértice atual 
                        retorno.append(aresta.rotulo)
                        retorno.append(aresta.v1.rotulo)

                        if not v_visitados[aresta.v1.rotulo]:  # se o v1 é um vértice não visitado: visitamos
                            v_visitados[aresta.v1.rotulo] = True
                            a_visitadas[a] = True

                            break  # termina o loop e reinicia para verificar as arestas de v1
                        else:  # se o vértice v1 já foi visitado, então é um vértice de retorno, 
                            return retorno[retorno.index(aresta.v1.rotulo):]  # devemos retornar da primeira aparição de v1 até o final.
                        
                else:  # se não houver arestas a partir de do vértice atual
                    # retorno = []
                    retorno.pop()  # remove o último vértice
                    if len(retorno) == 0:  # se o retorno só tinha um vértice, então acabamos e não achamos ciclo.
                        continue
                    retorno.pop()  # remove a última aresta
        return False