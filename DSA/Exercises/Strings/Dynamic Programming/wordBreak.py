# Given a string s and y a dictionary of n words dictionary, 
# check if s can be segmented into a sequence of valid words from the dictionary, separated by spaces.


# 1. Recursive
def wordBreak(s, words):
    # Check all lengths, 
    # for every valid word, check if continuing would work
    # and repeat the process
    
    m = len(s)

    def wordBreakRec(i):
        if i == m:
            return True
        
        for j in range(i, m):
            if (s[i:j + 1] in words) and wordBreakRec(j + 1):
                return True

        return False
        
    return wordBreakRec(0)

# 2. Top down - Memoization
def wordBreak2(s, words):
    # Same concept but save repeated checks

    m = len(s)
    memo = [-1] * m
    # Consider: lengths = sorted({len(w) for w in word_set})  # try only valid lengths

    def wordBreakRec(i):
        if i == m:
            return 1
        
        if memo[i] != -1:
            return memo[i]
        
        for j in range(i, m):
            if (s[i: j + 1] in words) and wordBreakRec(j + 1):
                memo[i] = 1
                return 1
        
        memo[i] = 0
        return 0
    
    return wordBreakRec(0) == 1

# 3. Bottom up - Iterative
def wordBreak3(s, words):
    # Go through word, check if curr word can be constructed from beginnning
    # and check with all words to see which others can be constructed from then

    m = len(s)
    dp = [False] * (m + 1)
    dp[0] = True

    lengths = sorted({len(w) for w in words})
    
    for i in range(1, m + 1):

        for L in lengths:
            start = i - L
            if (start >= 0) and (dp[start]) and (s[start: i] in words):
                dp[i] = True
                break
    
    return dp[-1]


if __name__ == "__main__":
    s = "ilike"

    dictionary = {"i", "like", "gfg"}

    print("true" if wordBreak3(s, dictionary) else "false")
