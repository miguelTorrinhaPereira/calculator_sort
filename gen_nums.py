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


def shuffel(tamanho, nums):
  for i in range(tamanho-1):
    a = randint(i, tamanho-1)
    nums[i],nums[a] = nums[a],nums[i]  


def gen_nums_norm(tamanho):
  nums = gen_nums_raw(tamanho)  
  shuffel(tamanho, nums) 
  return nums 


def gen_nums_rand(tamanho):
  return [randint(1,193) for i in range(tamanho)]
  

def gen_nums_invert(tamanho):
  return gen_nums_raw(tamanho)[::-1]
  
  
def gen_nums_nearly(tamanho):
  nums = gen_nums_raw(tamanho)  
  raio = max(12//(384//tamanho), 1)  # o 1 é para impedir que raio fique 0 
  for i in range(tamanho-1):
    a = min(randint(i, i+raio), tamanho-1)
    nums[i],nums[a] = nums[a],nums[i]    
  return nums
  

def gen_nums_fewuniq(tamanho):
  factor = 24 
  largura = 384 // tamanho
  if  largura > factor:  # para não dar erro com o bogo_sort
    nums =  [192, 128, 128, 64, 64]
    shuffel(tamanho, nums)
    return nums

  factor //= largura
  nums = gen_nums_raw(tamanho//factor)
  nums = nums*factor
  shuffel(tamanho, nums)
  return nums


def gen_nums(modo, tamanho):
  if modo in ('','1'):
    return gen_nums_norm(tamanho)
  elif modo == '2':
    return gen_nums_rand(tamanho)
  elif modo == '3':
    return gen_nums_invert(tamanho)
  elif modo == '4':
    return gen_nums_raw(tamanho)
  elif modo == '5':
    return gen_nums_nearly(tamanho)
  elif modo == '6':
    return gen_nums_fewuniq(tamanho)