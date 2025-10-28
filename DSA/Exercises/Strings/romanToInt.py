# Given a string s representing a Roman numeral, find it's corresponding integer value.

#  I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000

# Iterate through string,
# If next char bigger than curr,
# Substract big from small and add it,
# Otherwise, add directly

def RomanToInt(s):

    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000 }
    
    ln = len(s)
    tot = 0
    i = 0
    while i < ln:
        c1 = s[i]
        v1 = vals(c1)

        if i + 1 < ln and v1 < vals(s[i + 1]):
            tot += (vals(s[i + 1]) - v1)
            i += 1
        else:
            tot += v1
        i += 1

    return tot