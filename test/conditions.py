def isgood():
    return True
def isbad():
    return True

if isgood() and 4 > 5:
    print('good')

if isgood() is isbad():
    print(0)