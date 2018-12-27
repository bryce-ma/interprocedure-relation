def m0(s):
    print(s)
def listm(s):
    return [s]

for s in [listm('hello'), 'world','1234']:
    m0(s)
for s in listm('s'):
    m0(s)
while 4 > 5 and 5 > 6:
    m0(4)