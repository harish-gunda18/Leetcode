#code
def func(arr,inp):
    for i in inp:
        # print(i[0])
        arr[i[0]]+=i[2]
        arr[i[1]+1]-=i[2]

    for i in range(1,len(arr)):
        arr[i]+=arr[i-1]

    return arr


# test case1
arr = [0,0,0,0]
inp = [(0,1,5),(1,2,5)]
print(func(arr,inp))