class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Brute Force
        # Runtime: O(3n) Space: O(n + 27) where n is # of tiles
        # Iterate through the rows, iterate through the columns, iterate through squares
            # For each iteration, create a Hash Set to track duplicates
            # If a duplicate is found, board is invalid
        # If no duplicates, board is valid

        # Less Runtime, More Space
        # Runtime: O(n) Space: O(9 + n + n) where n is # of tiles
        # Iterate through all tiles only once, 
            # Just reset the current row hash set once you get to the end of a row.
            # Have 9 hash sets for each column.
            # Have 9 hash sets for each 3 x 3 square.

        for i in range(len(board)):
            rowSet = {}
            for j in range(len(board[i])):
                if(board[i][j] != "."):
                    if rowSet.get(board[i][j]):
                        return False
                    rowSet[board[i][j]] = 1

        for j in range(len(board[0])):
            colSet = {}
            for i in range(len(board)):
                if(board[i][j] != "."):
                    if colSet.get(board[i][j]):
                        return False
                    colSet[board[i][j]] = 1
        
        # row_start is initialized to -3, then increases by 3 for every 3 squares (including first)
        # row iterates from row_start to row_start + 3 exclusive for every square

        # col_start is intialized to -3, then increases by 3 for every square
            # Every 3 squares, col_start resets to 0
        # col iterates from col_start to col_start + 3 exclusive for every square

        square = 0
        row_start = -3
        col_start = -3

        while square < 9:
            if(square % 3 == 0):
                row_start += 3

            col_start += 3
            if(col_start == len(board[i])):
                col_start = 0

            squareSet = {}
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] != ".":
                        if squareSet.get(board[i][j]):
                            return False
                        squareSet[board[i][j]] = 1
            
            square += 1

        return True
            

         
            
