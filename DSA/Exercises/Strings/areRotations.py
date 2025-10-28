# Given two string s1 and s2 of same length, the task is to check whether s2 is a rotation of s1.

# Append s1 to itself to get a circular continuation
# check if s2 is substring of it, if so, it's a rotation

def areRotations(s1, s2):
    full = s1 + s1

    M = len(full)
    N = len(s2)
    i = 0
    for i in range(M):
        for j in range(N):
            k = j + 1
            if full[i+j] != s2[j]:
                break
        if k == M:
            return True
        
    return False


if __name__ == "__main__":
    s1 = "aab" 
    s2 = "aba"
    
    print("true" if areRotations(s1, s2) else "false")


