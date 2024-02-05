from casioplot import set_pixel,show_screen
from values import profundidade, tamanho_factor, alg_cutout



def draw_norm(tamanho, nums):   
  for n in range(tamanho):
    for y in range(profundidade-nums[n],profundidade):
      set_pixel(n,y)
    show_screen()    


def draw_thick(tamanho, nums):   
  for n in range(tamanho):
    n *= tamanho_factor
    for x in range(tamanho_factor):
      for y in range(profundidade-nums[n//tamanho_factor],profundidade):
        set_pixel(n+x,y)
    show_screen()    
    
    
def draw(alg_escolhido, tamanho, nums):
  if alg_escolhido <= alg_cutout:
    draw_thick(tamanho, nums)
  else:
    draw_norm(tamanho, nums)