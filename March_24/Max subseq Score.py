import heapq
class Solution:
    def maxScore(self, nums1, nums2, k):
        maximum, curr, nums2Sorted = 0, 0, []

        for i in range(len(nums2)):
            nums2Sorted.append((nums1[i], nums2[i]))

        i, minheap = 0, []
        nums2Sorted.sort(reverse=True, key=lambda tup: tup[1])

        while i < k:
            minheap.append(nums2Sorted[i][0])
            curr += nums2Sorted[i][0]
            i += 1

        heapq.heapify(minheap)
        maximum = curr * nums2Sorted[k - 1][1]
        while i < len(nums2):
            curr -= heapq.heappop(minheap)
            heapq.heappush(minheap, nums2Sorted[i][0])
            curr += nums2Sorted[i][0]
            if curr * nums2Sorted[i][1] > maximum:
                maximum = curr * nums2Sorted[i][1]
            i += 1

        return maximum

print(Solution().maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))






