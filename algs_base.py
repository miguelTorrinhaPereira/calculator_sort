from casioplot import set_pixel,show_screen
from values import profundidade, tamanho_factor, branco


def troca_norm(n1, n2, nums):
  for y in range(profundidade-nums[n1],profundidade-nums[n2]):
    set_pixel(n1,y,branco)
    set_pixel(n2,y)
  show_screen()
  nums[n1],nums[n2] = nums[n2],nums[n1]


def troca_thick(n1, n2, nums):
  nums[n1],nums[n2] = nums[n2],nums[n1]
  n1 *= tamanho_factor
  n2 *= tamanho_factor
  for x in range(tamanho_factor):
    for y in range(profundidade-nums[n2//tamanho_factor],profundidade-nums[n1//tamanho_factor]):
      set_pixel(n1+x,y,branco)
      set_pixel(n2+x,y)
  show_screen()


def substitui(n1, new, nums):
  if nums[n1] < new:
    for y in range(profundidade-new,profundidade-nums[n1]):
      set_pixel(n1,y)
  else:
    for y in range(profundidade-nums[n1],profundidade-new):
      set_pixel(n1,y,branco)
  show_screen()
  nums[n1] = new 


def espera(n):
  for i in range(n*100):
    i += 1