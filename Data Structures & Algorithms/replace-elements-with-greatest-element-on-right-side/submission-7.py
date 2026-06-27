class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestElement = -1
        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = greatestElement
            greatestElement = max(greatestElement, temp)
        return arr
