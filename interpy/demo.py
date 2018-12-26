# the main program of this project
from .log import logging
from .ast_modifier import AstModifier

class Demo():
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
    def start(self, filename: str):
        self.log.debug('analyse file: ' + filename)
        astmodif = AstModifier(filename)
        # get origin AST
        originTree = astmodif.origin()
        # simplify the AST
        

def main():
    demo = Demo()
    demo.start('hello.py')

if __name__ == "__main__":
    main()