from random import randint



def gen_nums_raw(tamanho):
  if tamanho == 384:
    nums = []
    for i in range(1,193):
      nums += [i,i]
    return nums
  else:
    largura = 384 // tamanho
    return list(range(largura//2, 193, largura//2))


def shuffel(tamanho, shuffels, nums):
  for i in range(shuffels):
    a = randint(0, tamanho-1)
    b = randint(0, tamanho-1)
    while b == a: # evita trocar um elemento por si mesmo, o que n  o faz nada
      b = randint(0, tamanho-1)
    nums[a],nums[b] = nums[b],nums[a]  


def gen_nums_norm(tamanho, shuffels):
  nums = gen_nums_raw(tamanho)  
  shuffel(tamanho, shuffels, nums) 
  return nums 


def gen_nums_rand(tamanho):
  return [randint(1,193) for i in range(tamanho)]
  

def gen_nums_invert(tamanho):
  return gen_nums_raw(tamanho)[::-1]


def gen_nums(modo, tamanho, shuffels):
  if modo in ('','1'):
    return gen_nums_norm(tamanho, shuffels)
  elif modo == '2':
    return gen_nums_rand(tamanho)
  elif modo == '3':
    return gen_nums_invert(tamanho)
  elif modo == '4':
    return gen_nums_raw(tamanho)