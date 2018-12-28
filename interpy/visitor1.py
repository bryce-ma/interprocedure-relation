import ast
import log
import logging

logger = logging.getLogger(name=__name__)
# add _fullname attr to node
# add _upper attr to node 
def namejoin(name0:str, name1:str):
    if name0.endswith('.'):
        return name0 + name1
    else:
        return name1 if len(name0) == 0 else name0+ '.' + name1

class Visitor1(ast.NodeVisitor):
    def __init__(self):
        self.table = dict()
    def generic_visit(self, node):
        logger.info('generic_visit() node type: ' + type(node).__name__)
        if isinstance(node, list):
            upper = self.getupper(node)
            self.visitlist(node, upper)
        else:
            super().generic_visit(node)

    def setfullname(self, node, upper):
        nodename = node.name if hasattr(node, 'name')  else ''
        if upper is None:
            fullname = nodename
        else:
            fullname = namejoin(upper._fullname, nodename)
        node._fullname = fullname
    def getupper(self, node):
        return node._upper if hasattr(node, '_upper')  else None

    def visitbody(self, node):
        for x in node.body:
            if not isinstance(x, list):
                x._upper = node
            self.visit(x)

    def visit_Module(self, node):
        upper = self.getupper(node) # must None
        self.setfullname(node, upper)
        self.visitbody(node)
        
    def visit_ClassDef(self, node):
        upper = self.getupper(node)
        self.setfullname(node, upper)
        logger.debug('ClassDef fullname:' + node._fullname)
        self.table[node._fullname] = node
        self.visitbody(node)

    def visit_FunctionDef(self, node):
        upper = self.getupper(node)
        self.setfullname(node, upper)
        logger.debug('FunctionDef fullname:' + node._fullname)
        self.table[node._fullname] = node
        self.visitbody(node)
        
    def visitlist(self, node, upper):
        for x in node:
            if not isinstance(x, list):
                x._upper = upper
            self.visit(x)




        
