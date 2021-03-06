import networkx as nx
from local_properties import *
from global_properties import *
import math

def is_independent(G, S):
    for v in S:
        N = neighbors(G, v)
        if list(set(N) & set(S)) != []:
            return False
    return True


def is_clique(G, s):
    for i in range(len(s)):
        N = neighbors(G, s[i])
        for j in range(i + 1, len(s)):
            if s[1 + j] not in N:
                return False
    return True

def is_dominationing_set(G, S):
    S_complement = list(set(V(G)) - set(S))
    for v in S_complement:
        N = neighbors(G, V)
        if list(set(N) & set (S)) == []:
            return Falsea
    return True

def is_matching(G):
    for k in range(math.floor(n(G)/2), 1, -1):
        for M in combinations (E(G), k):
            if is_matching(list(M)) == True:
              return False
    return True
    
