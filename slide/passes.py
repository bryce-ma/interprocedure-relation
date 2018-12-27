from graphviz import Digraph

def main():
    g = Digraph('passes', filename='passes', format='png')
    g.node('a', 'src')
    g.node('b', 'ast')
    g.node('c', 'simplified ast')
    g.node('d', 'inter-procedure relations')
    g.edges(['ab', 'bc', 'cd'])
    g.render('passes', view=True, cleanup=True)

if __name__ == "__main__":
    main()