def mergeSort(ind_array,user,website,time):
    if len(ind_array)==1:
        return ind_array
    mid=len(ind_array)//2
    a = mergeSort(ind_array[:mid],user,website,time)
    b = mergeSort(ind_array[mid:],user,website,time)
    return merge(a,b,user,time)


def merge(a,b,user,time):
    i=0
    j=0
    m=[]
    while i<len(a) and j<len(b):
        if lesser(a[i],b[j],user,time):
            m.append(a[i])
            i+=1
        else:
            m.append(b[j])
            j+=1
    if i==len(a):
        while j<len(b):
           m.append(b[j])
           j+=1
    else:
        while i<len(a):
            m.append(a[i])
            i+=1
    return m


def lesser(a,b,user,time):
    if user[a]<user[b]:
        return True
    elif user[a]>user[b]:
        return False
    else:
        if time[a]<time[b]:
            return True
        else:
            return False


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
a=[]
for i in range(len(timestamp)):
    a.append(i)

s = mergeSort(a,username,website,timestamp)

w = [website[i] for i in s]
print(w)

g = []
prev = s[0]
count=0
for i in s[1:]:
    if i!=prev:
        g.append()
    count+=1