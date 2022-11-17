import json

d = {
    "a": 1,
    "b": 2,
    "c": 3
}


f = open('.../file.json')
d = json.load(f)
f.close()

chaves = []
valores = []


def dicionario_para_listas(d):
    for k in d.keys():
        chaves.append(k)
    print(chaves)

    for v in d.values():
        valores.append(v)
    print(valores)


dicionario_para_listas(d)
