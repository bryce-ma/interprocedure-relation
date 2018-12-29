def namejoin(name0:str, name1:str):
    if name0.endswith('.'):
        return name0 + name1
    else:
        return name1 if len(name0) == 0 else name0+ '.' + name1

def flatten(origin, l):
    if isinstance(l, list):
        for sub in l:
            origin.append(sub)
    else:
        origin.append(l)