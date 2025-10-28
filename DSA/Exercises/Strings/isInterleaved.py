# Give three strings s1, s2 and s3, determine if s3 is formed by interleaving s1 and s2.


# Check if s1[i] matches s3[k], if so, check next one
# Check if s2[j] matches s3[k], if so, check next one
# If neither, return False
# Otherwise, if k = len(s3), return true (you are done),
# else, return False

# 1. Recursive - Inefficient, O(2^(m+n)) W(m+n)
def isInterleaved1(s1, s2, s3):
    def isILRec(i, j):
        k = i + j

        if k == len(s3):
            return True
        
        match1 = False
        match2 = False

        if (i < len(s1)) and (s1[i] == s3[k]):
            match1 = isILRec(i + 1, j)
        
        if (j < len(s2)) and (s2[j] == s3[k]):
            match2 = isILRec(i, j + 1)
        
        return match1 or match2
    
    if len(s1) + len(s2) != len(s3):
        return False
    
    return isILRec(0, 0)

# 2. Top-Down (Memoization) DP - O(m*n), W(m*n)
# Save repeated / already calculated positions
def isInterleaved2(s1, s2, s3):
    m = len(s1)
    n = len(s2)

    if m + n != len(s3):
        return False
    
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]


    def isILRec(i, j):
        k = i + j

        if k == len(s3):
            return True
        
        if memo[i][j] != -1:
            return memo[i][j] == 1
        
        match1 = False
        match2 = False

        if (i < len(s1)) and (s1[i] == s3[k]):
            match1 = isILRec(i + 1, j)
        
        if (j < len(s2)) and (s2[j] == s3[k]):
            match2 = isILRec(i, j + 1)

        memo[i][j] = 1 if match1 or match2 else 0
        return match1 or match2
    
    
    return isILRec(0, 0)


# 3. Bottom-up (Tabulation) DP - O(m*n), W(m*n)
# Build up valid solutions from the beginning
def isInterleaved3(s1, s2, s3):
    m = len(s1)
    n = len(s2)

    if m + n != len(s3):
        return False
    
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

    # Check base case
    dp[0][0] = True

    # Check first col
    for i in range(m):
        dp[i + 1][0] = (s1[i] == s3[i]) and (dp[i][0])
    
    # Check first row
    for j in range(n):
        dp[0][j + 1] = (s2[j] == s3[j]) and (dp[0][j])
    
    # Check the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            k = i + j
            dp[i][j] = (((s1[i - 1] == s3[k - 1]) and dp[i - 1][j]) or
                        ((s2[j - 1] == s3[k - 1]) and dp[i][j - 1]))
    
    return dp[m][n]

# 4. Bottom-up Memory Optimized DP - O(m*n), W(m)
# Don't need to store the whole, just the previous row
def isInterleaved4(s1, s2, s3):
    m = len(s1)
    n = len(s2)

    if m + n != len(s3):
        return False
    
    prev = [False] * (m + 1)
    curr = [False] * (n + 1)

    # Check base case
    prev[0] = True
    
    # Check first row
    for j in range(n):
        prev[j + 1] = (s2[j] == s3[j] and prev[j])

    # Check the rest of the table
    for i in range(1, m + 1):
        curr[0] = ((s1[i - 1] == s3[i - 1]) and prev[0])
        for j in range(1, n + 1):
            k = i + j
            curr[i] = (((s1[i - 1] == s3[k - 1]) and prev[j]) or
                        ((s2[j - 1] == s3[k - 1]) and curr[j - 1]))
        
        prev = curr[:]
    
    return curr[m]


if __name__ == "__main__":

    s1 = "ABA"
    s2 = "AAC"
    s3 = "AAABCA"
    print("true" if isInterleaved4(s1, s2, s3) else "false")