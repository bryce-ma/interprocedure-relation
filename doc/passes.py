from graphviz import Digraph

def main():
    g = Digraph('passes', filename='passes', format='png')
    g.node('a', 'src')
    g.node('b', 'ast')
    g.node('c', 'simplified ast')
    g.node('e', 'inter-procedure relations')
    g.node('d', 'global name bindings')
    g.edges(['ab', 'bc', 'cd','de'])
    g.render('passes', view=True, cleanup=True)

if __name__ == "__main__":
    main()