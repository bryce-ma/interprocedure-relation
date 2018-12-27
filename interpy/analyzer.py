from graphviz import Digraph

from ast_modifier import AstModifier
from visitor1 import Visitor1

class Analyzer():
    def __init__(self):
        self.vistor = Visitor1()

    def analyze(self, tree):
        self.vistor.visit(tree)


if __name__ == "__main__":
    g = Digraph('hello', filename='hello', format='png')
    g.edge('hello', 'world')
    g.view()