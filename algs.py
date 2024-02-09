from drawlib import vertical_range, troca, substitui
from drawlib import set_pixel, show_screen, branco  # alguns algoritmos precissam de desenhar de formas especificas por questoes de performance, insertino_sort
from gen_nums import shuffel  # bogo_sort


# os algoritmos mais rapidos sao atrazados
selection_espera = 10
quick_espera = 4
comb_espera = 6
cycle_espera = 20
circle_espera = 6
bitonic_espera = 10



def espera(n):
  for i in range(n*100):
    i += 1


def calc_largura(tamanho):
  return 384 // tamanho  # 384 eh o maximo de numeros que podem existir



def bogo_sort(tamanho, nums):

  def randomize():
    aux = []
    aux.extend(nums)
    shuffel(tamanho, 40, aux)
    for i in range(tamanho):
      substitui(i, aux[i], nums, largura, False)
    show_screen()

  largura = calc_largura(tamanho)
  swapped = True
  while swapped:
    swapped = False
    for i in range(tamanho-1):
      if (nums[i] > nums[i+1]):
        swapped = True
        break
    
    if swapped: 
      randomize()



def bubble_sort(tamanho, nums):
  largura = calc_largura(tamanho)
  for j in range(tamanho):
    swapped = False
    for i in range(tamanho-j-1):
      if nums[i]>nums[i+1]:
        troca(i,i+1,nums,largura)
        swapped = True

    if not swapped: break 



def cocktail_sort(tamanho, nums):
  largura = calc_largura(tamanho)
  end = tamanho-1
  for start in range (tamanho):
    swapped = False
    for i in range (start, end):
      if (nums[i] > nums[i+1]) :
        troca(i,i+1,nums,largura)
        swapped=True
  
    if not swapped: break

    swapped = False
    end -= 1
    for i in range(end-1, start-1,-1):
      if (nums[i] > nums[i+1]):
        troca(i,i+1,nums,largura)
        swapped = True

    if not swapped: break



def selection_sort(tamanho, nums):
  largura = calc_largura(tamanho)
  for i in range(tamanho-1):
    min_idx = i
    for idx in range(i + 1, tamanho):
      if nums[idx] < nums[min_idx]:
        min_idx = idx

    troca(i,min_idx,nums, largura)
    espera(selection_espera)



def insertion_sort(tamanho, nums):
  largura = calc_largura(tamanho)
  for i in range(1, tamanho):
    key = nums[i]
    j = i-1
    while nums[j] > key and j >= 0:
      if j+1 != i:
        for y in vertical_range(nums[j], nums[j+1]):
          set_pixel(j+1,y,branco)
      else:
        for y in vertical_range(key, nums[j]):
          set_pixel(i,y)
      show_screen()

      nums[j+1] = nums[j]
      j -= 1

    j += 1
    substitui(j, key, nums, largura)



def shell_sort(tamanho, nums): 
  largura = calc_largura(tamanho)
  gap = tamanho//2
  while gap > 0: 
    j = gap 
    while j < tamanho: 
      i = j - gap 
      while i >= 0: 
        if  nums[i] <= nums[i+gap]: break
        else: troca(i,i+gap,nums, largura)

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
        troca(i,j,nums, largura)
        espera(quick_espera)
    troca(i+1,high,nums, largura)

    return i + 1

  def sort(low,high):
    if low < high:
      pi = partition(low, high)
      sort(low, pi - 1)
      sort(pi + 1, high)
  
  largura = calc_largura(tamanho)
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
      substitui(n, aux[n-l], nums, largura)

  def sort(l,r):
    if r-l+1 >= 2:
      m = (l+r)//2
      sort(l,m)
      sort(m+1,r) 
      merge(l,m,r)

  largura = calc_largura(tamanho)
  sort(0,tamanho-1)



def comb_sort(tamanho, nums):
  largura = calc_largura(tamanho)
  shrink_factor = 1.3
  gap = tamanho
  swapped = True

  while gap != 1 or swapped:
    swapped = False
    gap = max(1, int(gap/shrink_factor))  # gap não pode ficar menor que 1

    for i in range(tamanho-gap):
      if nums[i] > nums[i+gap]:
        troca(i, i+gap, nums, largura)
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
      troca(largest, i, nums, largura)
      heapify(tamanho, nums, largest)
 
  largura = calc_largura(tamanho)

  for i in range(tamanho // 2, -1, -1):
    heapify(tamanho, nums, i)

  for i in range(tamanho-1, 0, -1):
    troca(0, i, nums, largura)
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
      substitui(i, aux[i], nums, largura)
 
  largura = calc_largura(tamanho)
  exp = 1
  while 192 // exp > 0:
    counting_sort(tamanho, nums, exp)
    exp *= 10



def exchange_sort(tamanho, nums):
  largura = calc_largura(tamanho)
  for i in range(tamanho-1):
    for j in range(i+1,tamanho):
      if nums[i] > nums[j]:
        troca(i, j, nums, largura)



def odd_even_sort(tamanho, nums):

  def aux_sort(start):
    swapped = False
    for i in range(start, tamanho-1, 2):
      if nums[i] > nums[i+1]:
        troca(i, i+1, nums, largura)
        swapped = True
    return swapped

  largura = calc_largura(tamanho)
  swapped = True
  while swapped:
    swapped = False
    swapped = aux_sort(0)
    swapped = aux_sort(1)



def cycle_sort(tamanho, nums):

  def cycle(start, value, check):
    pos = start

    for i in range(start+1, tamanho):
      if nums[i] < value:
        pos += 1

    if check and pos == start: 
      return pos, start

    while nums[pos] == value:
      pos += 1

    old_value = value
    value = nums[pos]
    substitui(pos, old_value, nums, largura)
    espera(cycle_espera)

    return pos, value
  
  largura = calc_largura(tamanho)
  for start in range(tamanho-1):
    pos, value = cycle(start, nums[start], True)
    while pos != start:
      pos, value = cycle(start, value, False)

    

 
def circle_sort(tamanho, nums):

  def circle(low, high):
    if (low == high):
      return False

    swapped = False
    i, j = low, high

    while (i < j):
      if (nums[i] > nums[j]):
        troca(i, j, nums, largura)
        espera(circle_espera)
        swapped = True
      i += 1
      j -= 1

    if (i == j and nums[i] > nums[j + 1]):  # se tamanho for impar
      troca(i, j+1, nums, largura)
      espera(circle_espera)
      swapped = True

    mid = (high - low) // 2
    first_half = circle(low, low+mid)
    second_half = circle(low+mid+1, high)
    return swapped or first_half or second_half

  largura = calc_largura(tamanho)
  while (circle(0, tamanho-1)):
    pass



def bitonic_sort(tamanho, nums):
  
  def merge(low, cnt, dire):
    if cnt <= 1: return 

    k = cnt//2
    for i in range(low , low+k):
      if dire == 1 and nums[i] > nums[i+k]:
        troca(i,i+k,nums,largura)
        espera(bitonic_espera)
      elif dire == 0 and nums[i] < nums[i+k]:
        troca(i+k,i,nums,largura)
        espera(bitonic_espera)

    merge(low, k, dire)
    merge(low+k, k, dire)
  
  def sort(low, cnt,dire):
    if cnt <= 1: return

    k = cnt//2
    sort(low, k, 1)
    sort(low+k, k, 0)
    merge(low, cnt, dire)
 
  largura = calc_largura(tamanho)
  sort(0, tamanho, 1)


# def gravity_sort(tamanho, nums):
# def pairwise_sort(tamanho, nums)
# def odd_even_merge_sort(tamanho, nums):

sorting_algs = [bogo_sort, bubble_sort, cocktail_sort,
                selection_sort, insertion_sort, shell_sort, 
                quick_sort, merge_sort, comb_sort, 
                heap_sort, radix_sort, exchange_sort,
                odd_even_sort, cycle_sort, circle_sort,
                bitonic_sort]

def sort(alg, tamanho, nums):
  sorting_alg = sorting_algs[alg]
  sorting_alg(tamanho, nums)