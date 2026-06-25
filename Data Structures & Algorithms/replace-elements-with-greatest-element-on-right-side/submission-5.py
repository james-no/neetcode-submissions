class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        gMax = -1
        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = gMax
            gMax = max(temp, gMax)
        return arr
        