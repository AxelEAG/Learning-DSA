# Given two strings s1 and s2 of equal length, consisting only of lowercase English letters, 
# determine if they are isomorphic.


# 1. 2 HashMaps
def areIsomorphic1(s1, s2):
    # Track 1st time chars are seen.
    # If they match later, they can be switched,
    # otherwise, they aren't isomorphic

    mp1 = {}
    mp2 = {}

    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]

        # Add them if first occurrence
        if c1 not in mp1:
            mp1[c1] = i
        if c2 not in mp2:
            mp2[c2] = i
        
        # Check if they match
        if mp1[c1] != mp2[c2]:
            return False
    return True

# 2. Hashmap + seen set
def areIsomorphic2(s1, s2):

    mp1 = {}
    seen = set()

    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]

        if c1 in mp1:
            if mp1[c1] != c2:
                return False
        else:
            if c2 in seen:
                return False
            
            mp1[c1] = c2
            seen.add(c2)
    return True



if __name__ == "__main__":
    s1 = "aab"
    s2 = "xxy"

    if areIsomorphic1(s1, s2):
        print("True 1")
    else:
        print("False 1")
    
    if areIsomorphic2(s1, s2):
        print("True 2")
    else:
        print("False 2")