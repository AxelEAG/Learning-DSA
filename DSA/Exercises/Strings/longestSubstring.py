# Longest substring between any pair of occurrences of similar characters

# Loop through string,
# save first encounter of every character
# if character already seen, check if space longer than current biggest
# save if so and continue

def longestSubstring(s):
    
    maxLen = 0
    firstIndex = {}
    
    for i in range(len(s)):
        char = s[i]
        if char not in firstIndex:
            firstIndex[char] = i
        maxLen = max(maxLen, i - firstIndex[char])
    
    return maxLen

if __name__ == "__main__":
    s = "accabbacc"
    print(longestSubstring(s))