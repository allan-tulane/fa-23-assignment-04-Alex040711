import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, memo=None):
    # Initialize memo on the first call
    if memo is None:
        memo = {}
    # If we have already solved this subproblem, return the answer.
    if (len(S), len(T)) in memo:
        return memo[(len(S), len(T))]
    # Base cases
    if S == "":
        memo[(len(S), len(T))] = len(T)
        return len(T)
    elif T == "":
        memo[(len(S), len(T))] = len(S)
        return len(S)
    # Recursive cases
    if S[0] == T[0]:
        # Characters are the same, move to the next character in both strings
        memo[(len(S), len(T))] = fast_MED(S[1:], T[1:], memo)
    else:
        # Characters are different, consider all operations
        insert_cost = fast_MED(S, T[1:], memo)
        delete_cost = fast_MED(S[1:], T, memo)
        replace_cost = fast_MED(S[1:], T[1:], memo)
        memo[(len(S), len(T))] = 1 + min(insert_cost, delete_cost, replace_cost)
    return memo[(len(S), len(T))]

def fast_align_MED(S, T, memo=None):
    # Initialization of memo on the first call
    if memo is None:
        memo = {}
    # Check if we have already solved this subproblem and have the alignment
    if (len(S), len(T)) in memo:
        return memo[(len(S), len(T))]
    # Base cases with alignments
    if S == "":
        memo[(len(S), len(T))] = (len(T), T, "-"*len(T))
        return len(T), T, "-"*len(T)
    elif T == "":
        memo[(len(S), len(T))] = (len(S), "-"*len(S), S)
        return len(S), "-"*len(S), S
    # Recursive cases
    if S[0] == T[0]:
        cost, alignS, alignT = fast_align_MED(S[1:], T[1:], memo)
        memo[(len(S), len(T))] = (cost, S[0] + alignS, T[0] + alignT)
        return cost, S[0] + alignS, T[0] + alignT
    else:
        insert_cost, insert_alignS, insert_alignT = fast_align_MED(S, T[1:], memo)
        delete_cost, delete_alignS, delete_alignT = fast_align_MED(S[1:], T, memo)
        replace_cost, replace_alignS, replace_alignT = fast_align_MED(S[1:], T[1:], memo)
        # Choose the operation with the minimum cost
        min_cost = min(insert_cost, delete_cost, replace_cost)
        if min_cost == insert_cost:
            memo[(len(S), len(T))] = (1 + insert_cost, "-" + insert_alignS, T[0] + insert_alignT)
        elif min_cost == delete_cost:
            memo[(len(S), len(T))] = (1 + delete_cost, S[0] + delete_alignS, "-" + delete_alignT)
        else:
            memo[(len(S), len(T))] = (1 + replace_cost, S[0] + replace_alignS, T[0] + replace_alignT)
        return memo[(len(S), len(T))]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
