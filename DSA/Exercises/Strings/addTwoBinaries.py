# Given two binary strings s1 and s2, the task is to return their sum.
# The input strings may contain leading zeros but the output string should not have any leading zeros.

def trimZeroes(b):
    i = 0
    while b[i] == '0':
        i += 1
    return b[i:]

def addTwoBinaries(s1, s2):
    # Traverse right to left,
    # result = (c + c1 + c2) % 2,
    # Carry (c) = (c + c1 + c2) // 2


    m = len(s1)
    n = len(s2)
    if n > m:
        s1, s2 = s2, s1
        n, m = m, n

    j = n - 1
    carry = 0
    res = []
    for i in range(m - 1, -1, -1):
        bit1 = int(s1[i])
        bitSum = carry + bit1
        if j >= 0:
            bit2 = int(s2[j])
            bitSum += bit2
            j -= 1

        bit = bitSum % 2
        carry = bitSum // 2

        res.append(str(bit))
        i -= 1
    
    if carry:
        res.append(str(carry))
    
    rev = res[::-1]
    trimmed = trimZeroes(rev)
    ans = "".join(trimmed)
    return ans

# Given n binary strings, the task is to find their sum which is also a binary string.
def addBinaries(binaries):
    res = "0"
    for bin in binaries:
        res = addTwoBinaries(res, bin)
    return res


if __name__ == "__main__":
    s1 = "1101"
    s2 = "111"
    print(addTwoBinaries(s1, s2))

    arr = ["1", "10", "11"];
    print(addBinaries(arr));
