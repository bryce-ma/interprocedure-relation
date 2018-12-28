import ast
import log
import logging
from typing import Optional
from collections import defaultdict

logger = logging.getLogger(name=__name__)

class Visitor2(ast.NodeVisitor):
    def __init__(self, tbl):
        self.table = tbl
        self.edges = defaultdict(list)

    def generic_visit(self, node):
        logger.info('generic_visit() node type: ' + type(node).__name__)
        if isinstance(node, list):
            self.visitlist(node)
        else:
            super().generic_visit(node)

    def visitlist(self, node):
        for x in node:
            self.visit(x)

    def visit_Call(self, node):
        logger.debug('Call fullname:')
        logger.info('Call node:' + ast.dump(node))
        self.edges['Apple.color'].append('Apple.red')

    def locate_self(self,node) -> Optional[ast.AST]:
        while hasattr(node, '_upper'):
            if isinstance(node._upper, ast.ClassDef):
                return node._upper
            else:
                node = node._upper
        return None
