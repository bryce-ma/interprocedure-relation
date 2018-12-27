from graphviz import Digraph

class Analyzer():
    pass

if __name__ == "__main__":
    g = Digraph('hello', filename='hello', format='png')
    g.edge('hello', 'world')
    g.view()