from gen_nums import gen_nums  # cria a lista de numero 
from drawlib import draw  # desenha a lista no inicio
from algs import sort  # os algoritmos de ordenacao


# larguras comtem a largura das barras que representam os numeros para cada algoritmo
larguras = [76, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 3]

alg = int(input('alg? '))
modo = input('mode? ')

# estes valores sao ajustados dependendo do algoritmo para que os mais lentos demorem o mesmo que os rapidos
largura = larguras[alg]
tamanho = 384 // largura

nums = gen_nums(modo, tamanho)

draw(tamanho, nums, largura)

sort(tamanho, nums, alg)