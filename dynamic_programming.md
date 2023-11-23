# Notes

### DP Problems

DP problems have 2 characteristics:
* *Optimal substructure*: optimal solution can be derived from subproblems
* *Overlapping subproblems*: some computations are repeatedly needed by distinct subproblems and can be memoized

DP problems often solve these kinds of problems:
* *Combinatorics* e.g. how many subsets with sum `target`?
* *Optimization* e.g minimal number of coins for change

### Pattern

* Recursive formulation - solution = f(sub_solutions)
  * Problem specification: Define objective function
  * Recursive solution: bases cases + induction

* Bottom-up solution (base-cases -> input)