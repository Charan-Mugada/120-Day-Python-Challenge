nums1=list(map(int,input("Enter: ").split()))
nums2=list(map(int,input("Enter: ").split()))
result=list(set(nums1)&set(nums2))
print(result)