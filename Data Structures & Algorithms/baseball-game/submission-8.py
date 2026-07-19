class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newRecord = []
        for op in operations:
            if op == '+':
                newRecord.append(newRecord[-1] + newRecord[-2])
            elif op == 'D':
                newRecord.append(2 * newRecord[-1])
            elif op == 'C':
                newRecord.pop()
            else:
                newRecord.append(int(op))
        return sum(newRecord)
