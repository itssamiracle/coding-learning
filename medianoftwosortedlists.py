def findMedianSortedArrays(nums1, nums2):
	print(nums1 , nums2)
	if len(nums1) ==0:
		return onemedian(nums2)
	if len(nums2) == 0:
		return onemedian(nums1)
	if len(nums1)+len(nums2) == 2:
		return (nums1[0]+nums2[0])/2
	if nums1[0]<=nums2[0]:
		nums1.remove(nums1[0])
	else:
		nums2.remove(nums2[0])
		
	if nums1[-1]>=nums2[-1]:
		nums1.remove(nums1[-1])
	else:
		nums2.remove(nums2[-1])
	return findMedianSortedArrays(nums1, nums2)



def onemedian(thelist):
	while len(thelist)>2:
		thelist.remove(thelist[0])
		thelist.remove(thelist[-1])
	if len(thelist) ==2:
		return (thelist[0]+thelist[1])/2
	if len(thelist) ==1:
		return thelist[0]
	
if __name__ == "__main__":
	print(findMedianSortedArrays([1,2,3,4], [5,6,7]))