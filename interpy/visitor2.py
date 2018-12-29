import ast
import log
import logging
from typing import Optional
from collections import defaultdict
import astpretty
from utils import namejoin

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
        logger.info('Call node:' + astpretty.pformat(node))
        # handle self.callsomething()
        if isinstance(node.func, ast.Attribute):
            func = node.func
            method = func.attr
            inst = func.value.id if isinstance(func.value, ast.Name) else ''
            if inst == 'self':
                clssnode = self.locate_self(node)
                self.edges[node._upper._fullname].append(namejoin(clssnode._fullname, method))
                logger.debug('')
            elif len(inst) > 0:
                realname = self.getrealname(inst, node)
                # clss = self.table[realname]
            # realname = getrealname()

    def getrealname(self, name: str, node):
        pass
        # uppername = node._upper._fullname
        # return namejoin(uppername, name)

    def locate_self(self,node) -> Optional[ast.AST]:
        while hasattr(node, '_upper'):
            if isinstance(node._upper, ast.ClassDef):
                return node._upper
            else:
                node = node._upper
        return None
