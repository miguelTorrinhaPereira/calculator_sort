from random import randint



def gen_nums_raw(tamanho):
  largura = 384 // tamanho
  if largura % 2 == 0:
    spacing = largura // 2
    return list(range(spacing, 193, spacing))
  else:
    nums = []
    for n in range(largura, 193, largura):
      nums += [n,n]
    return nums


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
  
  
def gen_nums_nearly(tamanho, shuffels):
  nums = gen_nums_raw(tamanho)  
  raio = 6
  for i in range(shuffels):
    a = randint(0, tamanho-1)
    b = randint(a-raio, a+raio)
    if b >= tamanho: 
      b = tamanho-1
    elif b < 0: 
      b = 0    
    nums[a],nums[b] = nums[b],nums[a]    
  return nums
  

def gen_nums_fewuniq(tamanho, shuffels):
  factor = 24 
  largura = 384 // tamanho
  if  largura > factor:  # para não dar erro com o bogo_sort
    nums =  [192, 128, 128, 64, 64]
    shuffel(tamanho, shuffels, nums)
    return nums

  factor //= largura
  nums = gen_nums_raw(tamanho//factor)
  nums = nums*factor
  shuffel(tamanho, shuffels, nums)
  return nums


def gen_nums(modo, tamanho, shuffels):
  if modo in ('','1'):
    return gen_nums_norm(tamanho, shuffels)
  elif modo == '2':
    return gen_nums_rand(tamanho)
  elif modo == '3':
    return gen_nums_invert(tamanho)
  elif modo == '4':
    return gen_nums_raw(tamanho)
  elif modo == '5':
    return gen_nums_nearly(tamanho, shuffels)
  elif modo == '6':
    return gen_nums_fewuniq(tamanho, shuffels)