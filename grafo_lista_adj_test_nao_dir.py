import unittest
from meu_grafo_lista_adj_nao_dir import *
from gerar_grafos_teste import vertices_pb
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo('test_json/grafo_pb2.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo('test_json/grafo_pb3.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb4.json', MeuGrafo())

        self.g_p_sem_paralelas = GrafoJSON.json_to_grafo('test_json/grafo_pb_simples.json', MeuGrafo())

        self.g_p_completo = GrafoJSON.json_to_grafo('test_json/grafo_pb_completo.json', MeuGrafo())

        # Grafos completos
        self.g_c = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(['J', 'C', 'E', 'P']).arestas(True).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()

        self.g_c1 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(1).build()

        # Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo('test_json/grafo_l1.json', MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo('test_json/grafo_l2.json', MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([v:=Vertice('D')]) \
            .arestas([Aresta('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([Aresta('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()
        

        self.g_c6 = GrafoBuilder().tipo(MeuGrafo()).vertices(['J', 'C', 'E']).arestas(True).build()

        self.g_c6_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a3',vertices_pb['C'], vertices_pb['E'])]).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T"]).arestas(True).build()

        self.g_c2_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a4',vertices_pb['C'], vertices_pb['E']),
             Aresta('a6',vertices_pb['E'], vertices_pb['T'])]).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T","P"]).arestas(True).build()

        self.g_c3_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T","P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a5', vertices_pb['C'], vertices_pb['E']),
             Aresta('a8', vertices_pb['E'], vertices_pb['T']),
             Aresta('a10', vertices_pb['T'],vertices_pb['P'])]).build()

        lista_aresta = [Aresta('a1',Vertice('C'),Vertice('J')),
                Aresta('a2',Vertice('J'),Vertice('E')),
                Aresta('a3',Vertice('C'),Vertice('T')),
                Aresta('a4',Vertice('C'),Vertice('P'))]
        self.g_c4 = grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T","P"]).arestas(lista_aresta).build()

        self.g_c4_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T","P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a3', vertices_pb['C'], vertices_pb['T']),
             Aresta('a4', vertices_pb['C'], vertices_pb['P']),
             Aresta('a2', vertices_pb['J'],vertices_pb['E'])]).build()

        self.g_c6_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2',vertices_pb['J'], vertices_pb['E'])]).build()

        self.g_c2_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2', vertices_pb['J'], vertices_pb['E']),
             Aresta('a3', vertices_pb['J'], vertices_pb['T'])]).build()

        self.g_c3_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T", "P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2', vertices_pb['J'], vertices_pb['E']),
             Aresta('a3', vertices_pb['J'], vertices_pb['T']),
             Aresta('a4', vertices_pb['J'], vertices_pb['P'])]).build()

        self.g_c4_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T", "P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2', vertices_pb['J'], vertices_pb['E']),
             Aresta('a3', vertices_pb['C'], vertices_pb['T']),
             Aresta('a4', vertices_pb['C'], vertices_pb['P'])]).build()
        
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        self.g_c5 = GrafoBuilder().tipo(MeuGrafo()).vertices(vertices).arestas(
            [
                Aresta('a1', Vertice('A'), Vertice('B')),
                Aresta('a2', Vertice('A'), Vertice('C')),
                Aresta('a3', Vertice('B'), Vertice('E')),
                Aresta('a4', Vertice('B'), Vertice('D')),
                Aresta('a5', Vertice('D'), Vertice('F')),
                Aresta('a6', Vertice('D'), Vertice('G')),
                Aresta('a7', Vertice('D'), Vertice('H'))
            ]
        ).build()

        self.g_c5_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(vertices).arestas(
            [
                Aresta('a1', Vertice('A'), Vertice('B')),
                Aresta('a3', Vertice('B'), Vertice('E')),
                Aresta('a4', Vertice('B'), Vertice('D')),
                Aresta('a5', Vertice('D'), Vertice('F')),
                Aresta('a6', Vertice('D'), Vertice('G')),
                Aresta('a7', Vertice('D'), Vertice('H')),
                Aresta('a2', Vertice('A'), Vertice('C'))
            ]
        ).build()

        self.g_c5_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(vertices).arestas(
            [
                Aresta('a1', Vertice('A'), Vertice('B')),
                Aresta('a2', Vertice('A'), Vertice('C')),
                Aresta('a4', Vertice('B'), Vertice('D')),
                Aresta('a3', Vertice('B'), Vertice('E')),
                Aresta('a5', Vertice('D'), Vertice('F')),
                Aresta('a6', Vertice('D'), Vertice('G')),
                Aresta('a7', Vertice('D'), Vertice('H'))
            ]
        ).build()

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertIsNone(self.g_r.remove_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_aresta('1'))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice('A')
        self.assertFalse(self.g_r.get_aresta('1'))
        self.assertEqual(self.g_r.arestas_sobre_vertice('B'), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_c6.dfs('J'), self.g_c6_dfs)
        self.assertEqual(self.g_c2.dfs('J'), self.g_c2_dfs)
        self.assertEqual(self.g_c3.dfs('J'), self.g_c3_dfs)
        self.assertEqual(self.g_c4.dfs('J'), self.g_c4_dfs)
        self.assertEqual(self.g_c5.dfs('A'), self.g_c5_dfs)

    def test_bfs(self):
        self.assertEqual(self.g_c6.bfs('J'), self.g_c6_bfs)
        self.assertEqual(self.g_c2.bfs('J'), self.g_c2_bfs)
        self.assertEqual(self.g_c3.bfs('J'), self.g_c3_bfs)
        self.assertEqual(self.g_c4.bfs('J'), self.g_c4_bfs)
        self.assertEqual(self.g_c5.bfs('A'), self.g_c5_bfs)
    
    def test_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a2', 'E', 'a3', 'C'])
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ['C', 'a4', 'T', 'a6', 'M', 'a5', 'C'])
        self.assertEqual(self.g_p_completo.ha_ciclo(), ['E', 'a12', 'P', 'a16', 'M', 'a13', 'E'])
        self.assertEqual(self.g_l1.ha_ciclo(), ['A', 'a1', 'A'])
        self.assertEqual(self.g_l2.ha_ciclo(), ['B', 'a2', 'B'])
        self.assertEqual(self.g_l3.ha_ciclo(), ['C', 'a2', 'C'])

        self.assertFalse(self.g_c1.ha_ciclo())
        self.assertFalse(self.g_d2.ha_ciclo())
        self.assertFalse(self.g_l1.dfs().ha_ciclo())
        self.assertFalse(self.g_d.ha_ciclo())
        self.assertFalse(self.g_c2_bfs.ha_ciclo())

    def test_caminho(self):
        self.assertEqual(self.g_d.caminho(1), ['A', 'asd', 'B'])
        self.assertIsNone(self.g_d2.caminho(1))
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a7', 'M'])
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertIsNone(self.g_p.caminho(5))
        self.assertEqual(self.g_p_completo.caminho(6), ['J', 'a1', 'C', 'a10', 'T', 'a14', 'E', 'a12', 'P', 'a16', 'M', 'a20', 'Z'])
        self.assertIsNone(self.g_p_completo.caminho(7))
        self.assertEqual(self.g_l1.caminho(1), ['A', 'a2', 'B'])
        self.assertIsNone(self.g_l1.caminho(4))        

    def test_conexo(self):
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_d2.conexo())
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p2.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_r.conexo())
