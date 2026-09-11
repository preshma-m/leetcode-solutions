class Solution {

    public int GCD(int a, int b) {
        while(b!=0){
            int temp=b;
            b=a%b;
            a=temp;
        }
        return a;
        }

    public int findGCD(int[] nums) {

        int mini=Integer.MAX_VALUE;
        int maxi=Integer.MIN_VALUE;

        for(int i=0;i<nums.length;i++){
            mini=Math.min(mini,nums[i]);
            maxi=Math.max(maxi,nums[i]);
        }
        return GCD(mini,maxi);
    }
}