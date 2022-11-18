from matplotlib import pyplot as plt
from operator import itemgetter
import json

f = open('python/aula7/words.json')
d = json.load(f)
f.close()

chaves = []
valores = []


def ordena_dic(d):
    return dict(sorted(d.items(), key=itemgetter(1), reverse=True))


d = ordena_dic(d)

for k in d.keys():
    chaves.append(k)
    chaves = chaves[0:10]

for v in d.values():
    valores.append(v)
    valores = valores[0:10]

escolha = int(input('Escolha o tipo de gráfico: \n'
                    '1' + '.' + ' ' + 'Gráfico de Barras \n'
                    '2' + '.' + ' ' + 'Gráfico Circular \n'))


def escolha_grafico(d):
    def desenha_grafico_de_barras(d):
        x = chaves
        y = valores

        plt.bar(x, y)
        plt.show()

    def desenha_grafico_circular(d):
        labels = chaves
        valor = valores

        plt.pie(valor, labels=labels, autopct='%1.1f%%')
        plt.show()

    if escolha == 1:
        print(desenha_grafico_de_barras(d))
    elif escolha == 2:
        desenha_grafico_circular(d)
    else:
        print('Você não escolheu nenhuma opção.')
    print('Até logo!')


escolha_grafico(d)
