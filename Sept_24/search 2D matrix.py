class Solution:
    def searchMatrix(self, matrix, target: int):
        m, n = len(matrix), len(matrix[0])

        def bi_search_row():
            start, end = 0, m - 1
            while start <= end:
                mid = (start + end)//2
                if matrix[mid][0] == target:
                    return mid, True
                elif target < matrix[mid][0]:
                    end = mid - 1
                else:
                    start = mid
            return start - 1, False

        row, found = bi_search_row()
        return bi_search_col(row)
