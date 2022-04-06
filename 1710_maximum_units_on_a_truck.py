class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda i:i[1],reverse=True)
        # print(boxTypes)
        out=0

        for i in boxTypes:
            if i[0]>truckSize:
                out+=((truckSize)*i[1])
                truckSize=0
                return out
            else:
                truckSize=truckSize-i[0]
                out+=(i[0]*i[1])
        return out