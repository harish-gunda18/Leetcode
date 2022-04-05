class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return self.mergeSort(logs)


    # same as normal merge sort
    def mergeSort(self,arr):
        if len(arr)==1:
            return arr
        mid = len(arr)//2
        a = self.mergeSort(arr[:mid])
        b = self.mergeSort(arr[mid:])
        return self.merge(a,b)


    # modified merge
    def merge(self,a,b):
        # initializing 2 arrays
        m = [] # will have lexicographically sorted letter logs
        n = [] # will have digits logs in their relative order
        i=0
        j=0

        # first we will add all the digit logs in first array to the n array and then add all the #digit logs in the second array to the n array to maintain their relative order
        while(i<len(a)):
            if ord(a[i][-1])<58:
                n.append(a[i])
            i+=1
        while(j<len(b)):
            if ord(b[j][-1])<58:
                n.append(b[j])
            j+=1

        # merge the remaining letter logs in their lexicographical order
        i=0
        j=0
        while(i<len(a) and j<len(b)):
            if ord(a[i][-1])<58:
                i+=1
                continue
            if ord(b[j][-1])<58:
                j+=1
                continue
            if self.lesser(a[i],b[j]):
                m.append(a[i])
                i+=1
            else:
                m.append(b[j])
                j+=1


        # append any left over letter logs either in a or b to the m array
        if j==len(b):
            while(i<len(a)):
                if ord(a[i][-1])<58:

                    i+=1
                else:
                    m.append(a[i])
                    i+=1
        else:
            while(j<len(b)):
                if ord(b[j][-1])<58:

                    j+=1
                else:
                    m.append(b[j])
                    j+=1
        return m+n

    # function to determine lesser of 2 letter logs
    def lesser(self,a,b):
        a_identifier = a[:a.index(' ')]
        b_identifier = b[:b.index(' ')]
        a = a[a.index(' '):]
        b = b[b.index(' '):]
        i=0
        j=0
        while(i<len(a) and j<len(b)):
            if a[i]<b[j]:
                return True
            if a[i]>b[j]:
                return False
            i+=1
            j+=1
        if len(a)==len(b):
            if a_identifier<b_identifier:
                return True
            return False
        elif len(a)<len(b):
            return True
        return False
                