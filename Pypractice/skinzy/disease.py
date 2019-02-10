import ast
from datetime import datetime

records = [
    "{'acne':10,'furuncle':8,'vitiligo':5,'eczema':3}",
    "{'furuncle':30,'eczema':23,'acne':10,'vitiligo':5}",
]

disease = {'acne':0,'vitiligo':0,'eczema':0,'furuncle':0}

for x in records:
    for y in list(ast.literal_eval(x).keys())[:3]:
        disease[y] += 1

for k,v in disease.items():print(k,v)


print(datetime.fromtimestamp(1000000000).strftime('%Y-%m-%d'))
print(datetime.fromtimestamp(1500000000).strftime('%Y-%m-%d'))
print((datetime.fromtimestamp(1500000000).year-datetime.fromtimestamp(1000000000).year))

"""
OUTPUT

acne 2
vitiligo 1
eczema 1
furuncle 2
2001-09-09
2017-07-14
16
"""
