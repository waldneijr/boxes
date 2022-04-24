import math

n1 = int(input('Number of manufactured items: '))
n2 = int(input('Number of items that will be packed per box: '))

boxes = math.ceil(n1 / n2)

print(f'For {n1} items, packing {n2} items in each box, you will need {boxes} boxes.')