import ast
import log
import logging

logger = logging.getLogger(name=__name__)
class Visitor0(ast.NodeTransformer):
    def generic_visit(self, node):
        logger.debug('generic_visit() node type: ' + type(node).__name__)
        return super().generic_visit(node)

    # remove if
    def visit_If(self, node):
        logger.debug('visit_If to remove it: ' + ast.dump(node))
        logger.debug('removed: ' + ast.dump(node.test))
        for e in node.body:
            logger.debug('removed: ' + ast.dump(e))
        return [self.visit(node.test)] + [self.visit(x) for x in node.body]

    def visit_For(self, node):
        logger.debug('visit_For: ' + ast.dump(node))
        if isinstance(node.iter, ast.List):
            return [self.visit(x) for x in node.iter.elts] + [self.visit(x) for x in node.body]
        return [node.iter] + [self.visit(x) for x in node.body]
    def visit_While(self, node):
        logger.debug('visit_While: ' + ast.dump(node))
        return [self.visit(node.test)] + [self.visit(x) for x in node.body]
    def visit_BoolOp(self, node):
        logger.debug('visit_BoolOp: ' + ast.dump(node))
        return [self.visit(x) for x in node.values]
    def visit_Expr(self, node):
        logger.debug('visit_Expr: ' + ast.dump(node))
        return self.visit(node.value)
    def visit_Compare(self, node):
        logger.debug('visit_Expr: ' + ast.dump(node))
        return [self.visit(node.left)] + [self.visit(x) for x in node.comparators]


        

