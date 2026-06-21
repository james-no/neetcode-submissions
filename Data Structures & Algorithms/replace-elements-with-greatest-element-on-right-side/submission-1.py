class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, temp)
        return arr
