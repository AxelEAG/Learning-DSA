# Given a positive integer n, the task is to count all possible distinct 
# binary strings of length n such that there are no consecutive 1's.

# 1. Recursive

# For every i, can add either 1 or 0. 
# Add valid ones and continue recursively until reaching desired length

def countBinaries1(n):
    binaries = []

    def countRecur(path):
        # Base case
        if len(path) == n:
            binaries.append("".join(path))
            return

        # Only check the path with a '1' if valid
        if len(path) == 0 or path[-1] == '0':
            countRecur(path + ['1'])
        
        countRecur(path + ['0'])
    
    countRecur([])
    return binaries


def countBinaries2(n):
    def countRecur(i, n):
  
        # Base case
        if i >= n:
            return 1

        # If we take 1 at ith index, 
        # we cannot have 1 at (i-1)
        take = countRecur(i + 2, n)

        # If we skip 1, we can consider
        # 1 at i-1.
        noTake = countRecur(i + 1, n)

        return take + noTake
    
    return countRecur(0, n)

# 2. Top-Down DP (Memoization)
def countBinaries3(n):
    memo = [-1]*n
    def countRecur(i, n):
        # base case
        if i >= n:
            return 1
        
        # Check if answer's been seen before
        if memo[i] != -1:
            return memo[i]
        
        take = countRecur(i + 2, n)
        noTake = countRecur(i + 1, n)

        memo[i] = take + noTake
        return memo[i]
    
    return countRecur(0, n)

# 3. Bottom-Up (Tabulization)
def countBinaries4(n):
    dp = [0] * n
    dp[0] = 2
    dp[1] = 3

    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    
    return dp[-1]

# 4. Optmized Bottom-Up (Tabulization)
def countBinaries4(n):
    dp = [0] * n
    dp[0] = 2
    dp[1] = 3
    prev = 2
    curr = 3

    for _ in range(2, n):
        tmp = prev
        prev = curr
        curr = prev + tmp

    
    return curr

if __name__ == "__main__":
    n = 5
    res = countBinaries4(n)
    print(res, " ")

    
