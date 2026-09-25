class Solution {
    public int findMin(int[] nums) {
        if(nums.length==1){
             return nums[0];
        }
        
        int left=0;
        int right=nums.length-1;
        
        int minimum=Integer.MAX_VALUE;
        while(left<=right){
              int mid=left+(right-left)/2;

             if(nums[left]<=nums[mid]){
                   minimum=Math.min(minimum,nums[left]);
                   left=mid+1;

             }else{
               minimum=Math.min(minimum,nums[mid]);
               right=mid-1;

             }
        }
        return minimum;
    }
}