# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray(object):

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        return self.arr[index]

    def length(self):
        return len(self.arr)


class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        l, r = 0, mountainArr.length() - 1

        def findPeak(l, r):
            best = -1
            while l < r:
                mid = l + ((r - l) // 2)
                one, two = mountainArr.get(mid), mountainArr.get(mid + 1)
                if one > two:
                    best = mid
                    r = mid
                else:
                    l = mid + 1
            return best

        def binary_search(l, r, asc):
            while l < r:
                mid = l + ((r - l) // 2)
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    if asc:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if asc:
                        l = mid + 1
                    else:
                        r = mid - 1
            return -1

        peak = findPeak(l, r)
        found = binary_search(l, peak, True)
        if found == -1:
            return binary_search(peak + 1, r, False)
        return found


a = [1,2,3,4,5,3,1]
mount = MountainArray(a)
print(Solution().findInMountainArray(2, mount))