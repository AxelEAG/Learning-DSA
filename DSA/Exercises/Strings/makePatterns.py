# Prompt: Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them. 

# Loop through string
# Recursively go through 2 options, one with a space, one without, for the next combination
# Once at the end of the string, print / save array and continue

def makePatterns(s):
    combinations = []

    def makePattern(s, i):
        if i == len(s) - 1:
            combinations.append(s)
            return
        
        makePattern(s, i + 1)
        makePattern(s[:i + 1] + " " + s[i + 1:], i + 2)
    
    makePattern(s, 0)
    return combinations

if __name__ == "__main__":
    s = "ABC"
    combs = makePatterns(s)
    print(combs)

            

# ["ABC", "AB C"
#  "A BC", "A B C"]


