from itertools import chain
array = [3, 3, 9, 9, 5]
subarrays = [[(array[x - 1:y]) for y in range(x, len(array) + 1)] for x in range(1, len(array) + 1)]
subarrays = list(chain.from_iterable(subarrays))
print(subarrays)
# print(*(x for x in subarrays), sep='\n')
