# the main program of this project
from .log import logging

class Demo():
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
    def start(self, filename: str):
        self.log.debug('analysis file: ' + filename)
        

def main():
    demo = Demo()
    demo.start('hello.py')

if __name__ == "__main__":
    main()