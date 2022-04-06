class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        D = [0]*1001
        for i in boxTypes:
            D[i[1]]=D[i[1]]+i[0]
        # print(D[:10])
        d = 1000
        out = 0
        while(d>0):
            if D[d]!=0:
                if truckSize>D[d]:
                    out+=(D[d]*d)
                    truckSize-=D[d]
                else:
                    out+=(truckSize*d)
                    return out
            d-=1
        return out
            
        