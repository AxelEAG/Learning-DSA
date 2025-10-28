# === KMP Algorithm ===
# Knuth-Morris Pratt (KMP) algorithm is used to find a "Pattern" in a "Text". This algorithm compares character by character from left to right. 
# But whenever a mismatch occurs, it uses a preprocessed table called "Prefix Table" to skip characters comparison while matching. 
# Sometimes prefix table is also known as LPS Table. Here LPS stands for "Longest proper Prefix which is also Suffix".


# LPS Algo
# Keep track of previously longest Prefix found 
# When broken, try recursively checking from 2nd longest until reaching start point

def LPS(s):

    m = len(s)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        # If match, increase prefix size and save current
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            # Otherwise, check previous prefix
            if j != 0:
                j = lps[j - 1]
            # If none, restart
            else:
                lps[i] = 0
                i += 1
    return lps        

def _build_lps(t: str) -> list[int]:
    lps = [0] * len(t)
    j = 0
    for i in range(1, len(t)):
        while j > 0 and t[i] != t[j]:
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
            lps[i] = j
    return lps

# KMP Algo

def KMP(s, pat):
    lps = LPS(pat)

    n = len(s)
    m = len(pat)
    i = 0 
    j = 0
    results = []

    while i < n:
        # If match, move both pointers forward
        if s[i] == pat[j]:
            i += 1
            j += 1
            # If end of pattern, save match
            if j == m:
                results.append(i - j)
                j = lps[j - 1]
        else:
            # Else, if other prefixes, try them
            if j != 0:
                j = lps[j - 1]
            # Else, continue checking
            else:
                i += 1
    return results

if __name__ == "__main__":
    txt = "aabaacaadaaabaaba"
    pat = "aaba"
    
    res = KMP(txt, pat)
    print(res)
    for i in range(len(res)):
        print(res[i], end=" ")    
           