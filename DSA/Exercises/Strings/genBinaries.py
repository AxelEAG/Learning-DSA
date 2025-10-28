# Given a string containing of '0', '1' and '?' wildcard characters, 
# generate all binary strings that can be formed by replacing 
# each wildcard character by '0' or '1'. 


# Recursion
# Recursively find all combinations
# Recursive call with each option, base case when no more '?' on remaining of string

def getBinariesRec(s):
    combinations = []
    def findCombinations(i, ls):
        if i == len(ls):
            combinations.append("".join(ls))
            return

        if ls[i] != '?':
            findCombinations(i + 1, ls)
            return
        
        ls[i] = '1'
        findCombinations(i + 1, ls)
        ls[i] = '0'
        findCombinations(i + 1, ls)
        ls[i] = '?'

    findCombinations(0, list(s))
    return combinations


# Queue
from collections import deque
def getBinaries(s):
    queue = deque([list(s)])
    results = []
    while queue:
        element = queue.popleft()
        for i, char in enumerate(element):
            if char == '?':
                queue.append(element[:i] + ['0'] + element[i+1:])
                queue.append(element[:i] + ['1'] + element[i+1:])
                break
        else:
            results.append("".join(element))
    return results

if __name__ == "__main__":
    s = "1??0?101"
    print(getBinariesRec(s))
    print(getBinaries(s))