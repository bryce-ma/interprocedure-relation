import ast

class AstModifier():
    def __init__(self, filename:str):
        self.file = filename
        self.originast = None
    def origin(self) -> ast.AST:
        with open(self.file, 'r') as sourcefile:
            tree = ast.parse(sourcefile.read())
        self.originast = tree
        return tree

    def simplify(self):
        pass
        