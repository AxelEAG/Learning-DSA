# Given a 2-D grid of characters mat[][] and a string word, 
# the task is to check if that word exist in the grid mat[][] or not. 
# A word can be matched in 4 directions at any point. 

from typing import List, Tuple
def searchWord(grid: List[List[str]], word: str) -> List[Tuple[int]]:
    # Traverse to grid, if find first letter,
    # begin DFS, continually swapping the curr letter with a
    # placeholder '#' to avoid it circling back
    # if find full match, add it to list

    # Define valid directions
    # directions = [(-1 , -1), (0  , -1), (1  ,  -1), 
    #               (-1 ,  0),            (1  ,   0), 
    #               (-1 ,  1), (0  ,  1), (1  ,   1)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    wordLen = len(word)
    length = len(grid[0]) # Horizontal
    height = len(grid)    # Vertical

    # Check if coordinate is within the grid
    def isValid(x: int, y: int) -> bool:
        return (0 <= x < length) and (0 <= y < height)
    
    coords = []
    def findWord(x: int, y: int, i: int) -> bool:
        if i == wordLen:
            return True
        
        # Check all directions to see if any lead to the word
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if isValid(nx, ny) and grid[ny][nx] == word[i]:
                c, grid[ny][nx] = grid[ny][nx], '#'
                if findWord(nx, ny, i + 1):
                    return True
                grid[ny][nx] = c
                            
        return False
    
    # Look through the whole grid
    for y in range(height):
        for x in range(length):
            c = grid[y][x]
            if c == word[0]:
                continue

            grid[y][x] = '#'
            if findWord(x, y, 1):
                coords.append((x, y))
            grid[y][x] = c
    return coords


# Given a 2D grid m*n of characters and a word, 
# the task is to find all occurrences of the given word in the grid. 
# A word can be matched in all 8 directions at any point.

# Search word but same direction
def searchWordRec(grid: List[List[str]], word: str) -> List[Tuple[int]]:
    # Pick a direction and recursively keep checking
    # if the next letter in that dir is part of the word

    # Define valid directions
    directions = [(-1 , -1), (0  , -1), (1  ,  -1), 
                  (-1 ,  0),            (1  ,   0), 
                  (-1 ,  1), (0  ,  1), (1  ,   1)]
    
    height = len(grid)
    length = len(grid[0])
    L = len(word)
    coords = []

    # Check if coordinate is within the grid
    def isValid(x: int, y: int) -> bool:
        return (0 <= x < length) and (0 <= y < height)

    # Recursively check if given coordinate has the next char in the word
    def isChar(x: int, y: int, dx: int, dy: int, i: int) -> bool:
        if i == L: return True
        
        nx, ny = x + dx, y + dy
        if isValid(nx, ny) and word[i] == grid[ny][nx]:
            return isChar(nx, ny, dx, dy, i + 1)

        return False 

    # Check if the full word is in one of the directions
    def hasWord(x: int, y: int):
        for dx, dy in directions:
            if isChar(x, y, dx, dy, 1):
                return True
        return False

    # Check every direction for every cell in grid
    for y in range(height):
        for x in range(length):
            if grid[y][x] == word[0] and hasWord(x, y):
                coords.append((x, y))

    return coords

def searchWordIter(grid: List[List[str]], word: str) -> List[Tuple[int]]:
    # Pick a direction and iteratively check if the next
    # char in that dir is in the word

    # Define valid directions
    directions = [(-1 , -1), (0  , -1), (1  ,  -1), 
                  (-1 ,  0),            (1  ,   0), 
                  (-1 ,  1), (0  ,  1), (1  ,   1)]
    
    height = len(grid)
    length = len(grid[0])
    L = len(word)
    coords = []

    # Check if coordinate is inside grid
    def isValid(x, y):
        return (0 <= x < length) and (0 <= y < height)

    # Iteratively check if the full word is in one of the directions
    def hasWord(x: int, y: int):
        for dx, dy in directions:
            nx, ny, i = x + dx, y + dy, 1
            while i < L and isValid(nx, ny) and grid[ny][nx] == word[i]:
                nx += dx
                ny += dy
                i  += 1
            if i == L:
                return True
        return False

    # Check every direction for every cell in grid
    for y in range(height):
        for x in range(length):
            if grid[y][x] == word[0] and hasWord(x, y):
                coords.append((x, y))
        
    return coords

if __name__ == "__main__":
    grid = [['a', 'b', 'a', 'b'],
            ['a', 'b', 'e', 'b'],
            ['e', 'b', 'e', 'b']]
    word = "abe"

    ans = searchWord(grid, word)
    print(ans)