class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)-1
        while(l<=r):
            
            m=l+(r-l)//2
            print(m,l)
            if(nums[m]==target):
                return True
            elif nums[l]<nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
                
                  
            elif nums[m]>nums[l]:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1

            else:
                if nums[l]==nums[m]:
                    l+=1
                else:
                    r-=1
                    

        return False
     