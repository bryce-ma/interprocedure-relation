import ast
import log
import logging
from typing import Optional
from collections import defaultdict
import astpretty
from utils import namejoin

logger = logging.getLogger(name=__name__)

class Visitor2(ast.NodeTransformer):
    def __init__(self, tbl):
        self.table = tbl
        self.edges = defaultdict(list)

    def generic_visit(self, node):
        logger.info('generic_visit() node type: ' + type(node).__name__)
        if isinstance(node, list):
            return self.visitlist(node)
        else:
            return super().generic_visit(node)

    def visitlist(self, node):
        result = []
        for x in node:
            result.append(self.visit(x))
        return result

    def visit_Assign(self, node):
        right = self.visit(node.value)
        if right is None: return
        lefts = node.targets
        for lname in lefts:
            if isinstance(lname, ast.Name):
                fullname = self.getrealname(lname.id, node)
                self.table[fullname] = right

    def visit_Call(self, node):
        logger.debug('Call fullname:')
        logger.info('Call node:' + astpretty.pformat(node))
        # handle callsomething
        if isinstance(node.func, ast.Name):
            funcname = node.func.id
            # get ClassDef if there have one
            clssdef = self.table[funcname] if funcname in self.table.keys() else None
            if not clssdef is None:
                logger.debug('class def get from global name binding: '+ clssdef.name)
                return clssdef

        # handle self.callsomething()
        elif isinstance(node.func, ast.Attribute):
            func = node.func
            method = func.attr
            inst = func.value.id if isinstance(func.value, ast.Name) else ''
            if inst == 'self':
                clssnode = self.locate_self(node)
                self.edges[node._upper._fullname].append(namejoin(clssnode._fullname, method+'()'))
                logger.debug('')
            elif len(inst) > 0:
                realname = self.getrealname(inst, node)
                clss = self.table[realname]
                if isinstance(clss, ast.ClassDef):
                    # invoke the __init__() of class
                    self.edges[node._upper._fullname].append(namejoin(clss.name, '__init__()'))

    def getrealname(self, name: str, node):
        uppername = node._upper._fullname
        return namejoin(uppername, name)

    def locate_self(self,node) -> Optional[ast.AST]:
        while hasattr(node, '_upper'):
            if isinstance(node._upper, ast.ClassDef):
                return node._upper
            else:
                node = node._upper
        return None
