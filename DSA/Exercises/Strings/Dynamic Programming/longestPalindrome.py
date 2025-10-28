# Given a string s, the task is to find the longest substring which is a palindrome.
# If there are multiple answers, then return the first occurrence of the 
# longest palindromic substring from left to right.


# 1. Dynamic Programming

# Create table dp[][] that stores whether s[i:j] is palindrome.
# Fill out table by:
#   Setting true all substrings of len 1 (a character's always a palindrome)
#   Checking all substrings of len 2 (if they are the same char)
#   From then on, making a 'bigger' palindrome by comparing first and last (i + n)
#   if previous substring (s[i:j]) was a palindrome, s[i-1:j+1] is also 
#   if those last 2 chars match (s[i-1] == s[j+2]).

def longestPalindrome1(s):
    m = len(s)
    dp = [[False for _ in range(m)] for _ in range(m)]
    # dp[i][j]: i - row, j - col
    start = 0
    maxLen = 1

    # All single chars are palindromes
    for i in range(m):
        dp[i][i] = True

    # Check if pairs of chars are palindromes - i.e. the same
    for i in range(m - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True 
            if 2 > maxLen:    
                start = i
                maxLen = 2

    # Check all other lengths
    for length in range(3, m + 1):
        for i in range((m - length) + 1):
            j = (i + length) - 1
            if (s[i] == s[j]) and (dp[i + 1][j - 1]):
                dp[i][j] = True 
                if length > maxLen:
                    start = i
                    maxLen = length

    return s[start:start + maxLen]

# 2. Expansion from center
def longestPalindrome2(s):
    # Traverse string, treat char and char + next char as centers,
    # expand out to see if they are still palindromes.
    # keep track of highest

    start = 0
    maxLen = 1
    m = len(s)
    for i in range(m):

        # Check for center of 1 and 2
        for j in range(2):
            mn, mx = i, i + j 

            while mn > 0 and mx < m and s[mn] == s[mx]:
                currLen = mx - mn + 1

                if currLen > maxLen:
                    maxLen = currLen
                    start = mn
                mn -= 1
                mx += 1

    return s[start:start + maxLen]


if __name__ == "__main__":
    s = "aaaabbaa"
    print(longestPalindrome2(s))