# Given a string str of length n (1 <= n <= 106) and a number k, 
# the task is to find the kth non-repeating character in the string.

def kNonRepeating(string, k):
    # Loop through string, counting freqs of each letter
    # Loop again, keeping track of which are non-repeating, 
    # stop and return at kth one

    freqs = {}
    for c in string:
        freqs[c] = freqs.get(c, 0) + 1
    
    count = 0
    for c in string:
        if freqs[c] == 1:
            count += 1
            if count == k:
                return c
    return None

if __name__ == "__main__":
    string = "geeksforgeeks"
    k = 2

    result = kNonRepeating(string, k)

    if result is None:
        print("There is no kth non-repeating character in the string.")
    else:
        print(f"The {k}th non-repeating character in the string is {result}.")
