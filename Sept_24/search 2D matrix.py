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

        def bi_search_col(row):
            start, end = 0, n - 1
            while start <= end:
                mid = (start + end) // 2
                if matrix[row][mid] == target:
                    return True
                elif target < matrix[row][mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return False

        row, found = bi_search_row()
        if not found:
            return bi_search_col(row)
        return found