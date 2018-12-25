class A:
    def method0(self, name):
        print(name)
        if 2 > 1:
            print('2 > 1')
            self.m1()
        else:
            print('something wrong')
            self.m2()
        self.m2()

    def m1(self):
        pass
    def m2(self):
        pass
def main():
    a = A()
    a.method0('hello')
if __name__ == '__main__':
    main()