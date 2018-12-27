# the main program of this project
import log
import logging
import os
from ast_modifier import AstModifier
from analyzer import Analyzer

class Demo():
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
    def start(self, filename: str):
        self.log.debug('analyse file: ' + filename)
        astmodif = AstModifier(filename)
        # get origin AST
        originTree = astmodif.origin()
        self.log.info('origin: ' + astmodif.dump(originTree))
        # simplify the AST
        astmodif.simplify()
        self.log.info('simplified: ' + astmodif.dump(astmodif.simpast))

        # analyse
        analyzer = Analyzer()
        analyzer.analyze(astmodif.simpast)

def main(args):
    demo = Demo()
    defaultfile = './test/apple.py'
    if len(args) > 1:
        defaultfile = args[1]
    demo.start(os.path.abspath(defaultfile))

if __name__ == "__main__":
    import sys
    main(sys.argv)