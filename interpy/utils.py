def namejoin(name0:str, name1:str):
    if name0.endswith('.'):
        return name0 + name1
    else:
        return name1 if len(name0) == 0 else name0+ '.' + name1

flatten = lambda l: [item for sublist in l for item in sublist]