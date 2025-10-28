

# Given two numbers as strings s1 and s2, calculate their product.

# Helper func to remove leading zeroes
def trimZeroes(s):
    i = 0
    while i < len(s) and s[i] == '0':
        i += 1
    return s[i:]

# Helper func to add two strings together
def addStrings(s1, s2):

    m = len(s1)
    n = len(s2)

    # Swap to have smaller string as s2
    if n > m:
        s1, s2 = s2, s1
        m, n = n, m
    
    j = n - 1
    carry = 0
    res = []
    for i in range(m - 1, -1, -1):
        d1 = int(s1[i])
        dSum = carry + d1

        if j >= 0:
            d2 = int(s2[j])
            dSum += d2
            j -= 1
        
        d = dSum % 10
        carry = dSum // 10
        res.append(str(d))
    
    # Add extra carry as necessary
    if carry:
        res.append(str(carry))
    
    # Format and return
    rev = res[::-1]
    trimmed = trimZeroes(rev)
    ans = "".join(trimmed)
    return ans

def multStrings(s1, s2):
    # Trim extra zeroes, traverse right to left
    # multiply each digit, keeping the carry and residue,
    # add carry to each result and then multiply next digits

    s1 = trimZeroes(s1)
    s2 = trimZeroes(s2)

    m = len(s1)
    n = len(s2)

    # Handle edge case of one of them being 0
    if m == 0 or n == 0:
        return "0"
    
    # Get relevant sign
    negative = False

    if s1[0] == "-":
        negative = not negative
        s1 = s1[1:]
    
    if s2[0] == "-":
        negative = not negative
        s2 = s2[1:]

    # Swap to have smaller string as s2
    if n > m:
        s1, s2 = s2, s1
        m, n = n, m
    
    # Make all summands
    carry = 0
    summands = []
    for j in range(n - 1, -1, -1):
        d1 = int(s2[j])

        # Make new summand
        summand = []
        for i in range(m - 1, -1, -1):
            d2 = int(s1[i])
            mult = d1 * d2 + carry
            
            d = mult % 10
            carry = mult // 10

            summand.append(str(d))
        
        # Add last carry as necessary
        if carry:
            summand.append(str(carry))

        # Append extra 0's and save
        summand = summand[::-1]
        for _ in range(n - j - 1):
            summand.append('0')

        summands.append(summand)

    # Add all the summands
    res = "0"
    for summand in summands:
        res = addStrings(res, summand)
    return res

