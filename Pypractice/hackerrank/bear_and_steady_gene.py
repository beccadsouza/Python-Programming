n = int(input())
gene = input()
freq = {'A':gene.count('A'),'C':gene.count('C'),'G':gene.count('G'),'T':gene.count('T')}
left = right = 0
ans = n+1
while right < len(gene)-1:
    freq[gene[right]] -= 1
    right += 1
    while sum(list(filter(lambda x:x > n//4,freq.values()))) == 0:
        ans = right - left if ans > right - left else ans
        freq[gene[left]] += 1
        left += 1
print(ans)



# n = int(input())
# gene = input()
# G = n//4
# A = n//4
# C = n//4
# T = n//4
# a = gene.count('A')
# g = gene.count('G')
# c = gene.count('C')
# t = gene.count('T')
#
# # print(A,a)
# # print(C,c)
# # print(G,g)
# # print(T,t)
#
# freq = {}
#
# if A-a < 0:
#     freq['A'] = a - A
# if C-c < 0:
#     freq['C'] = c - C
# if G-g < 0:
#     freq['G'] = g - G
# if T-t < 0:
#     freq['T'] = t - T
#
# # print(freq)
#
# start = sum(freq.values())
# # print(start)
# cont = True
# while cont:
#     for i in range(0,len(gene)-start+1):
#         sub = gene[i:i+start]
#         temp = 0
#         for k in freq.keys():
#             temp += freq[k] - sub.count(k)
#             # print(sub,freq[k],sub.count(k),temp)
#         if temp == 0:
#             cont = False
#             break
#
#     if cont:
#        start += 1
# print(start)


"""
8  
GAAATAAA
"""

# ACTTCCGAAAAA
