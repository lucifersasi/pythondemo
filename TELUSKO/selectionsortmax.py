def sort(nums):
    for i in range(6):
        maxpos=i
        for j in range(0,i):
            if nums[j]>nums[maxpos]:
                maxpos=j

        temp=nums[i]
        nums[i]=nums[maxpos]
        nums[maxpos]=temp
        print(nums)  #to see the sorting process step by step
nums=[5,3,8,6,7,2]
sort(nums)
print(nums)  # final output
