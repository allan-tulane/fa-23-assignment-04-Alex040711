# CMPS 2200 Assignment 4

## Answers

Name:  ________Alex Li________

Place all written answers from `assignment-04.md` here for easier grading.


Part 1


a)

1. Start with the amount N.
2. Find the largest power of 2 that is less than or equal to N. Let this value be 2^k.
3. Use one coin of denomination 2^k.
4. Subtract 2^k from N.
5. Repeat steps 2-4 until N becomes 0.



b)

Greedy-choice property: The greedy-choice property means making the best immediate choice at each step. In this case, it's always taking the highest denomination coin available. Since our denominations are powers of 2, you can never use fewer smaller coins than a single larger coin. For example, you can't use two 2^(k-1) coins instead of one 2^k coin because that would be the same amount but more coins.

Optimal substructure property: The optimal substructure property means that an optimal solution to a problem contains optimal solutions to its subproblems. Here, after taking a coin of 2^k, you're left with N-2^k, which is a smaller version of the original problem. The greedy algorithm will also give the best solution for this remaining amount. Since this applies at every step, the final solution is optimal.

In short, using the largest coin doesn't block us from finding the best solution for the rest of the money. Since this is true at every step, the greedy algorithm must give us the best overall solution.


c)

W(n)=O(log n)

S(n)=O(log n)



Part 2

a) 

The greedy algorithm may not always yield the fewest coins for arbitrary denominations. A counterexample is the set of denominations {1,3,4} for the amount 6. The greedy algorithm would choose two coins of 1 and one coin of 4, but the optimal solution is to use two coins of 3.


b)

Optimal substructure means that the optimal solution to a problem can be constructed from the optimal solutions of its subproblems. For the coin-changing problem, this means that if you have an optimal solution for N dollars, then for any amount less than N, the solution included for that smaller amount must also be optimal.

If the solution for the smaller amount wasn't optimal, then replacing it with an optimal solution for the smaller amount would yield a better solution for N, contradicting our assumption that we had an optimal solution for N.

c)

1. Initialize an array dp of length N+1, representing the minimum number of coins needed for each amount from 0 to N. Set dp[0] to 0 since no coins are needed to make 0 dollars.
2. For each amount i from 1 to N:
   a. For each coin denomination D[ j ]:
   * If D[ j ] is less than or equal to i, set dp[i] to the minimum of dp[i] and dp[ i -D[ j ]+1]
3. The value at dp[N] gives the minimum number of coins needed to make `N` dollars.

W=O(nk)

S=O(n)
