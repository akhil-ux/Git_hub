from itertools import permutations
from itertools import combinations
letters = [[""], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], [
    "m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
digits = "23"
combination_list = []
for i in zip(letters[2], letters[3]):
    combination_list.append(i)
print(combination_list)
for i in combinations(combination_list,len(digits)):
    print(i)
