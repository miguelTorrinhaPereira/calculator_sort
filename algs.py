from drawlib import vertical_range, troca_norm, troca_thick, substitui_norm, substitui_thick
from drawlib import set_pixel, show_screen, branco  # alguns algoritmos precissam de desenhar de formas especificas por questões de performance
from gen_nums import shuffel  # bogo_sort


selection_espera = 10
quick_espera = 6
comb_espera = 6



def espera(n):
  for i in range(n*100):
    i += 1



def bogo_sort(tamanho, nums):

  def randomize():
    aux = []
    aux.extend(nums)
    shuffel(tamanho, 40, aux)
    for i in range(tamanho):
      substitui_thick(i, aux[i], nums, largura, False)

  largura = 384 // tamanho  
  swapped = True
  while swapped:
    swapped = False
    for i in range(tamanho-1):
      if (nums[i] > nums[i+1]):
        swapped = True
        break
    
    if not swapped: break
    else: randomize()



def bubble_sort(tamanho, nums):
  largura = 384 // tamanho
  for j in range(tamanho):
    swapped = False
    for i in range(tamanho-j-1):
      if nums[i]>nums[i+1]:
        troca_thick(i,i+1,nums,largura)
        swapped = True

    if not swapped: break 



def cocktail_sort(tamanho, nums):
  largura = 384 // tamanho
  end = tamanho-1
  for start in range (tamanho):
    swapped = False
    for i in range (start, end):
      if (nums[i] > nums[i+1]) :
        troca_thick(i,i+1,nums,largura)
        swapped=True
  
    if not swapped: break

    swapped = False
    end -= 1
    for i in range(end-1, start-1,-1):
      if (nums[i] > nums[i+1]):
        troca_thick(i,i+1,nums,largura)
        swapped = True

    if not swapped: break



def selection_sort(tamanho, nums):
  for i in range(tamanho-1):
    min_idx = i
    for idx in range(i + 1, tamanho):
      if nums[idx] < nums[min_idx]:
        min_idx = idx

    troca_norm(i,min_idx,nums)
    espera(selection_espera)



def insertion_sort(tamanho, nums):
  for i in range(1, tamanho):
    key = nums[i]
    j = i-1
    while nums[j] > key and j >= 0:
      if j+1 != i:
        for y in vertical_range(nums[j], nums[j+1]):
          set_pixel(j+1,y,branco)
      else:
        for y in vertical_range(key, nums[i]):
          set_pixel(i,y)
      show_screen()

      nums[j+1] = nums[j]
      j -= 1

    j += 1
    for y in vertical_range(key, nums[j]):
      set_pixel(j,y,branco)
    show_screen()
    nums[j] = key



def shell_sort(tamanho, nums): 
  gap = tamanho//2
  while gap > 0: 
    j = gap 
    while j < tamanho: 
      i = j - gap 
      while i >= 0: 
        if  nums[i] <= nums[i+gap]: break
        else: troca_norm(i,i+gap,nums)

        i -= gap  
      j += 1
    gap //= 2


 
def quick_sort(tamanho, nums):

  def partition(low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
          i += 1
          troca_norm(i,j,nums)
          espera(quick_espera)
    troca_norm(i+1,high,nums)

    return i + 1

  def sort(low,high):
    if low < high:
      pi = partition(low, high)
      sort(low, pi - 1)
      sort(pi + 1, high)
  
  sort(0,tamanho-1)



def merge_sort(tamanho, nums):

  def merge(l,m,r):
    aux = []
    i ,j = l, m+1
    while i <= m or j <= r:
      if (i <= m) and (j > r or nums[i] <= nums[j]):
        aux += [nums[i]]
        i += 1
      else:
        aux += [nums[j]]
        j += 1
    
    for n in range(l,r+1):
      substitui_norm(n, aux[n-l], nums)

  def sort(l,r):
    if r-l+1 >= 2:
      m = (l+r)//2
      sort(l,m)
      sort(m+1,r) 
      merge(l,m,r)

  sort(0,tamanho-1)



def comb_sort(tamanho, nums):
  shrink_factor = 1.3
  gap = tamanho
  swapped = True

  while gap != 1 or swapped:
    swapped = False
    gap = max(1, int(gap/shrink_factor))  # gap não pode ficar menor que 1

    for i in range(tamanho-gap):
      if nums[i] > nums[i+gap]:
        troca_norm(i, i+gap, nums)
        swapped = True
        espera(comb_espera)



def heap_sort(tamanho, nums):

  def heapify(tamanho, nums, i):
    largest = i  
    left = 2*i + 1 
    right = 2*i + 2 

    if left < tamanho and nums[largest] < nums[left]:
      largest = left
    if right < tamanho and nums[largest] < nums[right]:
      largest = right

    if largest != i:
      troca_norm(largest, i, nums)
      heapify(tamanho, nums, largest)
 

  for i in range(tamanho // 2, -1, -1):
    heapify(tamanho, nums, i)

  for i in range(tamanho-1, 0, -1):
    troca_norm(0, i, nums)
    heapify(i, nums, 0)



def radix_sort(tamanho, nums):
  
  def counting_sort(tamanho, nums, exp): 
    aux = [0]* tamanho
    count = [0]*10 

    for i in range(0, tamanho): 
      index = int((nums[i] / exp) % 10)
      count[index] += 1
   
    carry = count [0]
    count[0] = 0
    for i in range(1,10): 
      carry += count[i]
      count[i] = carry - count[i]
   
    for i in range(tamanho):
      index = int((nums[i] / exp) % 10) 
      aux[count[index]] = nums[i] 
      count[index] += 1
   
    for i in range(0,tamanho): 
      substitui_norm(i, aux[i], nums)
 

  exp = 1
  while 192 // exp > 0:
    counting_sort(tamanho, nums, exp)
    exp *= 10


def exchange_sort(tamanho, nums):
  for i in range(tamanho-1):
    for j in range(i+1,tamanho):
      if nums[i] > nums[j]:
        troca_norm(i, j, nums)


# def odd_even_sort(tamanho, nums):
# def bitonic_sort(tamanho, nums):

sorting_algs = [bogo_sort, bubble_sort, cocktail_sort,
                selection_sort, insertion_sort, shell_sort, 
                quick_sort, merge_sort, comb_sort, 
                heap_sort, radix_sort, exchange_sort]

def sort(alg, tamanho, nums):
  sorting_alg = sorting_algs[alg]
  sorting_alg(tamanho, nums)