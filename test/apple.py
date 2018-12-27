class Apple:
    def __init__(self, name):
        self.name = name
    def color(self):
        lname = self.name.lower()
        if lname == 'gala' or lname == 'fuji':
            self.red(self.name)
            return 'red'
        else:
            self.green(self.name)
            return 'green'

    def red(self, rname):
        print('Are u want to eat red apples? so '+ rname + ' is red. Plz')
    def green(self, gname):
         print('Are u want to eat green apples? so '+ gname + ' is red. Plz')

def main():
    apple = Apple('fuji')
    color = apple.color()
    print('The color of this apple is: '+ color)

if __name__ == '__main__':
    main()