# Given a string s, the task is to return all permutations of a given string in lexicographically sorted order.

# sort string
# create permutations



# Create permutations:
#     for each remaining letter, try every other letter and backtrack
#     for trying every other letter, use a list made up of all the chars before and after the current one

def getPermutations(s):
    permutations = []
    s = list(s)

    def backtrack(s, path):

        # Base case
        if len(s) == 0:
            permutations.append("".join(path))
            return

        # For each letter, try to make all combinations of remaining letters
        for i in range(len(s)):
            pre = s[:i]
            suff = s[i+1:]
            # Add letter to new comb, check remeaining letters
            backtrack(pre + suff, path + [s[i]])
    
    backtrack(s, [])
    
    permutations.sort()

    return permutations


if __name__ == "__main__":
    s = "ABC"
    res = getPermutations(s)
    for x in res:
        print(x, end=" ")
