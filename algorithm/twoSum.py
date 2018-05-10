#方法一 暴力遍历  时间复杂度o(n^2)
def twoSum(arr,target):
    length = len(arr)
    for i in range(length):
        for j in range(i+1,length):
            if arr[i]+arr[j] == target:
                return [i,j]
    return 'no result'
# print(twoSum([2,4,5,7],9))

#方法二 巧用字典(hash表) 时间复杂度o(n)
def twoSum2(arr,target):
    length = len(arr)
    tdict = {}
    for i in range(length):
        num1 = target - arr[i]
        if num1 in tdict.keys():
            return [tdict[num1],i]
        else:
            tdict[arr[i]] = i
    return 'no result'

print(twoSum2([1,2,3,4,5,6,7,8],6))