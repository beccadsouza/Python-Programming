from collections import Counter
from itertools import chain
from practice import series
fact = []
temp = [fact[-1] for x in range(1,1000) if not fact.append(x*fact[-1] if fact else 1)]
t = int(input())
for i in range(t):
    str = input()
    vec = []
    string = [x for x in str]
    substrings = [[(string[x - 1:y]) for y in range(x, len(string) + 1)] for x in range(1, len(string) + 1)]
    substrings = list(chain.from_iterable(substrings))
    temp = [vec.append("".join(sorted(x))) for x in substrings]
    freq = Counter(vec)
    s = set(vec)
    answer = sum([1 for x in s if freq[x] is 2])
    answer += sum([int(fact[freq[x]-1]/(fact[freq[x]-3]*fact[1])) for x in s if freq[x] > 2])
    print(answer)

print(series.armstrong_numbers(1000))
