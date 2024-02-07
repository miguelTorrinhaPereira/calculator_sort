from casioplot import set_pixel, show_screen



profundidade = 192
branco = (255,255,255)



def vertical_range(baixo, cima):
  return range(profundidade - cima, profundidade - baixo)


def draw(tamanho, nums, largura):   
  for n in range(tamanho):
    n *= largura 
    for x in range(largura):
      for y in vertical_range(0,nums[n//largura]):
        set_pixel(n+x,y)
    show_screen()    


def troca(n1, n2, nums, largura = 1):
  nums[n1],nums[n2] = nums[n2],nums[n1]
  n1 *= largura
  n2 *= largura
  for x in range(largura):
    for y in vertical_range(nums[n1//largura], nums[n2//largura]):
      set_pixel(n1+x,y,branco)
      set_pixel(n2+x,y)
  show_screen()
  

def substitui(n, new, nums, largura = 1, show = True):  # bogo_sort looks better with show = False
  old = nums[n]
  nums[n] = new
  n *= largura
  if old < new:
    for x in range(largura):
      for y in vertical_range(old, new):
        set_pixel(n+x,y)
  else:
    for y in vertical_range(new, old):
      for x in range(largura):
        set_pixel(n+x,y,branco)
        
  if show:
    show_screen()