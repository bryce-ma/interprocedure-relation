from graphviz import Digraph

from ast_modifier import AstModifier
from visitor1 import Visitor1
from visitor2 import Visitor2

class Analyzer():
    def __init__(self, name='interpydefault'):
        self.name = name
        self.vistor1 = Visitor1()

    def analyze(self, tree):
        # get global name binding table
        self.vistor1.visit(tree)
        table = self.vistor1.table

        # interprete
        visitor2 = Visitor2(table)
        visitor2.visit(tree)

        # build relation graph in graphviz
        self.build_graph(visitor2.edges)

    def build_graph(self, edges: dict):
        g = Digraph(self.name, filename=self.name, format='png')
        for name in edges.keys():
            g.node(name, name)
        es = []
        for name, elist in edges.items():
            for name1 in elist:
                g.edge(name, name1)
        g.save()
        g.view()
        

if __name__ == "__main__":
    g = Digraph('hello', filename='hello', format='png')
    g.edge('hello', 'world')
    g.view()