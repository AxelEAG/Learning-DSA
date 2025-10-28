# Given a string S, the task is to remove all its adjacent duplicate characters recursively.

# Go through list, remove all current duplicates
# if didn't remove anything (same length), it's done
# Otherwise, check with the new string

def rutil(s, n):
    pos = 0
    trv = 0

    # Go through string, looking for duplicates
    while trv < n:
        duplicate = False

        # Mark if duplicate and skip them
        while trv + 1 < n and s[trv] == s[trv + 1]:
            duplicate = True
            trv += 1

        # Only save if not duplicate
        if not duplicate:
            s[pos] = s[trv]
            pos += 1
        trv += 1

    s = s[:pos]
    if pos != n:
        rutil(s, pos)
    
    return s

def rremove(s):
    s = list(s)

    return ''.join(rutil(s, len(s)))

if __name__ == "__main__":
    s = "abccbccba"
    print(rremove(s))
    