import matplotlib.pylab as grafico
import networkx as bibliotecaNetworkx

grafo = bibliotecaNetworkx.Graph()


grafo.add_node("a")
grafo.add_node("b")
grafo.add_node("c")
grafo.add_node("d")
grafo.add_node("e")
grafo.add_node("f")

grafo.add_edge("a", "b")
grafo.add_edge("b", "c")
grafo.add_edge("c", "d")    
grafo.add_edge("d", "e")
grafo.add_edge("e", "f")
grafo.add_edge("f", "a")

posicionamento = bibliotecaNetworkx.circular_layout(grafo)
bibliotecaNetworkx.draw_networkx_edge_labels(grafo, posicionamento, 
                                             edge_labels = {('a', 'b'): 'aresta a-b',
                                                            ('b', 'c'): 'aresta b-c',
                                                            ('c', 'd'): 'aresta c-d',
                                                            ('d', 'e'): 'aresta d-e',
                                                            ('e', 'f'): 'aresta e-f',
                                                            ('f', 'a'): 'aresta f-a'}
                                                            font_color = "green")
bibliotecaNetworkx.draw(grafo, with_labels = true
                        pos = posicionamento,
                        node_color = "red",
                        edge_color = "blue")
grafico.show()
