from values import  base_tamanho, tamanho_factor, base_shuffels, shuffel_factor, alg_cutout
from gen_nums import gen_nums  # cria a lista de numero 
from draw import draw  # desenha a lista no inicio
from sorting_algs import sort  # os algoritmos de ordenacao



# input
alg = int(input('alg? '))
modo = input('modo? ')


# estes valores sao ajustados dependendo do algoritmo para que os mais lentos demorem o mesmo que os rapidos
tamanho = base_tamanho
shuffels = base_shuffels
if alg > alg_cutout: 
  tamanho *= tamanho_factor
  shuffels *= shuffel_factor


# gera a lista de numeros
nums = gen_nums(modo, tamanho, shuffels)


# desenha a lista de numeros
draw(alg, tamanho, nums)


# ordena 
sort(alg, tamanho, nums)