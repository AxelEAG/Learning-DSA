# Atoi: ASCII To Integer - converts the numbers in string form to their integer value. 
# To put it simply, the atoi() function accepts a string (which represents an integer) 
# as a parameter and yields an integer value in return.

# Rules:
#   Skip leading whitespaces.
#   Check for sign.
#   Construct number from digits until reaching first non-digit / end of string.
#   If abs(num) > 2^31 -1, print 2^31 -1.

def atoi(s):
    
    MAX = 2**31 - 1
    MIN = -2**31
    num = 0
    i = 0
    m = len(s)
    sign = 1

    digits = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }

    # Skip whitespace
    while i < m and s[i] == ' ':
        i += 1

    # Get the sign
    if i < m and s[i] in {'-', '+'}:
        if s[i] == '-':
            sign = -1
        i += 1

    # Construct the number 
    while i < m and s[i] in digits:
        num = 10*num + digits[s[i]]
        if num > MAX:
            return sign * MAX if sign == 1 else MIN
        i += 1
        
    return sign * num

if __name__ == "__main__":
    s = " -0012g4"
    res = atoi(s)
    print(res)