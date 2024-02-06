from casioplot import set_pixel,show_screen
from values import profundidade



def draw_norm(tamanho, nums):   
  for n in range(tamanho):
    for y in range(profundidade-nums[n],profundidade):
      set_pixel(n,y)
    show_screen()    


def draw_thick(tamanho, nums, largura):   
  for n in range(tamanho):
    n *= largura 
    for x in range(largura):
      for y in range(profundidade-nums[n//largura],profundidade):
        set_pixel(n+x,y)
    show_screen()    
    
    
def draw(tamanho, nums, largura):
  if largura == 1:
    draw_norm(tamanho, nums)
  else:
    draw_thick(tamanho, nums, largura)