class NumMatrix:
    matrix = []

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    # Brute Force
    # Iterate through each row and col of the square, adding each individual val together
    # Return value
    # Runtime: O(n) Space: O(n)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output_sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                output_sum += self.matrix[i][j]
        
        return output_sum


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)