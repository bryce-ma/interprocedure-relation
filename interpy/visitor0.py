import ast
import log
import logging
import astpretty 
from utils import flatten

logger = logging.getLogger(name=__name__)
class Visitor0(ast.NodeTransformer):
    def generic_visit(self, node):
        logger.debug('generic_visit() node type: ' + type(node).__name__)
        result = super().generic_visit(node)
        return result

    def visit_ClassDef(self, node):
        body = []
        for e in node.body:
            flatten(body, self.visit(e))
        cls = ast.ClassDef()
        cls.body = body
        cls.name = node.name
        return cls

    def visit_FunctionDef(self, node):
        body = []
        for e in node.body:
            flatten(body, self.visit(e))
        cls = ast.FunctionDef()
        cls.body = body
        cls.name = node.name
        return cls

    # remove if
    def visit_If(self, node):
        logger.debug('visit_If to remove it: ' + astpretty.pformat(node))
        logger.debug('removed: ' + astpretty.pformat(node.test, show_offsets=True))
        for e in node.body:
            logger.debug('removed: ' + astpretty.pformat(e))
        return [self.visit(node.test)] + [self.visit(x) for x in node.body] + [self.visit(x) for x in node.orelse]

    def visit_For(self, node):
        logger.debug('visit_For: ' + astpretty.pformat(node))
        if isinstance(node.iter, ast.List):
            return [self.visit(x) for x in node.iter.elts] + [self.visit(x) for x in node.body]
        return [node.iter] + [self.visit(x) for x in node.body]
    def visit_While(self, node):
        logger.debug('visit_While: ' + astpretty.pformat(node))
        return [self.visit(node.test)] + [self.visit(x) for x in node.body]
    def visit_BoolOp(self, node):
        logger.debug('visit_BoolOp: ' + astpretty.pformat(node))
        return [self.visit(x) for x in node.values]
    def visit_Expr(self, node):
        logger.debug('visit_Expr: ' + astpretty.pformat(node))
        return self.visit(node.value)
    def visit_Compare(self, node):
        logger.debug('visit_Expr: ' + astpretty.pformat(node))
        return [self.visit(node.left)] + [self.visit(x) for x in node.comparators]
    


        

