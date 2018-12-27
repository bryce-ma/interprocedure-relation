import ast
import log
import logging

logger = logging.getLogger(name=__name__)
class Visitor1(ast.NodeVisitor):
    def generic_visit(self, node):
        logger.debug('generic_visit() node type: ' + type(node).__name__)
        return super().generic_visit(node)