from gen_nums import gen_nums  # cria a lista de numero 
from drawlib import draw  # desenha a lista no inicio
from algs import sort  # os algoritmos de ordenacao


# larguras comtem a largura das barras que representam os numeros para cada algoritmo
larguras = [64, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1]
base_shuffels = 3072

alg = int(input('alg? '))
modo = input('mode? ')

# estes valores sao ajustados dependendo do algoritmo para que os mais lentos demorem o mesmo que os rapidos
largura = larguras[alg]
tamanho = 384 // largura
shuffels = base_shuffels // largura

nums = gen_nums(modo, tamanho, shuffels)

draw(tamanho, nums, largura)

sort(alg, tamanho, nums)