def sort(nums):
    for i in range(len(nums)-1,0,-1):  # we are decreasing vals from last to first index number
        for j in range(i): # since the last element is highest we sort upto i in incrwasing order
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums = [5,3,8,1,9,4,7,2]
sort(nums)
print(nums)

                