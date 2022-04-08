import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        for i in words:
            if dic.get(i,-1)!=-1:
                dic[i]+=1
            else:
                dic[i]=1
        return heapq.nsmallest(k,dic,key=lambda x:(-dic[x],x))
