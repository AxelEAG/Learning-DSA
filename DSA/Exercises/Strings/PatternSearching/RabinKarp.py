# Rabin Karp Algorithm

# Rabin-Karp compares a string's hash values, rather than the strings themselves. 
# For efficiency, the hash value of the next position in the text is easily 
# computed from the hash value of the current position.

# Algorithm: 
#   Choose q, calculate hash value of pattern p,
#   Loop through substrings of same size, comparing hash values,
#   If they are the same, check if the numbers are the same

# The hash value is calculated using a rolling hash function. That is,
# by removing the contribution of the old character and adding that of the new one
# In this case, used h:
# h = 1
# for i in range(M - 1):
#         h = (h * d) % q


def RabinKarp(pat, txt):
    d = 256                 # Number of characters in the input alphabet (ASCII)
    q = 101                 # A prime number for modulo operations to reduce collisions
    M = len(pat)            # Length of pattern
    N = len(txt)            # Length of text
    p = 0                   # Hash value for pattern
    t = 0                   # Hash value for substring
    h = pow(d, M-1) % q     # High-order digit multiplier
    ans = []

    # Compute initial hash values for pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # If hash values match, check if actual text matches, save if so
        if p == t and txt[i + M] == pat:
            ans.append(i+1)

        # Calculate hash value for the next window
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t += q

    return ans

# Driver code
if __name__ == "__main__":
    txt = "birthboy"
    pat = "birth"
    res = RabinKarp(pat, txt)
    print(" ".join(map(str, res)))

