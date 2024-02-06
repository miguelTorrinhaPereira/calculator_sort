from casioplot import set_pixel, show_screen



profundidade = 192
branco = (255,255,255)


def vertical_range(baixo, cima):
  return range(profundidade - cima, profundidade - baixo)



def draw_norm(tamanho, nums):   
  for n in range(tamanho):
    for y in vertical_range(0, nums[n]):
      set_pixel(n,y)
    show_screen()    


def draw_thick(tamanho, nums, largura):   
  for n in range(tamanho):
    n *= largura 
    for x in range(largura):
      for y in vertical_range(0,nums[n//largura]):
        set_pixel(n+x,y)
    show_screen()    
    
    
def draw(tamanho, nums, largura):
  if largura == 1:
    draw_norm(tamanho, nums)
  else:
    draw_thick(tamanho, nums, largura)



def troca_norm(n1, n2, nums):
  for y in vertical_range(nums[n2], nums[n1]):
    set_pixel(n1,y,branco)
    set_pixel(n2,y)
  show_screen()
  nums[n1],nums[n2] = nums[n2],nums[n1]


def troca_thick(n1, n2, nums, largura):
  nums[n1],nums[n2] = nums[n2],nums[n1]
  n1 *= largura
  n2 *= largura
  for x in range(largura):
    for y in vertical_range(nums[n1//largura], nums[n2//largura]):
      set_pixel(n1+x,y,branco)
      set_pixel(n2+x,y)
  show_screen()


def substitui_norm(n, new, nums):
  if nums[n] < new:
    for y in vertical_range(nums[n], new):
      set_pixel(n,y)
  else:
    for y in vertical_range(new, nums[n]):
      set_pixel(n,y,branco)
  show_screen()
  nums[n] = new 
  

def substitui_thick(n, new, nums, largura, show = True):
  old = nums[n]
  nums[n] = new
  n *= largura
  if old < new:
    for y in vertical_range(old, new):
      for x in range(largura):
        set_pixel(n+x,y)
  else:
    for y in vertical_range(new, old):
      for x in range(largura):
        set_pixel(n+x,y,branco)
        
  if show:
    show_screen()