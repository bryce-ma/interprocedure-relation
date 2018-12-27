import ast
from visitor import Visitor

class AstModifier():
    def __init__(self, filename:str):
        self.file = filename
        self.visitor = Visitor0()
        self.origast = None
        self.simpast = None
    def dump(self, node):
        return ast.dump(node)
    def origin(self) -> ast.AST:
        with open(self.file, 'r') as sourcefile:
            tree = ast.parse(sourcefile.read())
        self.origast = tree
        return tree

    def simplify(self):
        if not self.origast is None:
            self.visitor.visit(self.origast)
            self.simpast = self.origast
        