from values import larguras, base_shuffels
from gen_nums import gen_nums  # cria a lista de numero 
from drawlib import draw  # desenha a lista no inicio
from sorting_algs import sort  # os algoritmos de ordenacao



# input
alg = int(input('alg? '))
modo = input('mode? ')

# estes valores sao ajustados dependendo do algoritmo para que os mais lentos demorem o mesmo que os rapidos
largura = larguras[alg]
tamanho = 384 // largura
shuffels = base_shuffels // largura

# gera a lista de numeros
nums = gen_nums(modo, tamanho, shuffels)

# desenha a lista de numeros
draw(tamanho, nums, largura)

# ordena 
sort(alg, tamanho, nums)