class Solution {
    public int[] runningSum(int[] nums) {
        int sum=0;
        int[] sumnum = new int[nums.length]; 
        for(int i=0;i<nums.length;i++){
            sum= sum + nums[i];
            sumnum[i] = sum;
        }
        return sumnum;
    }
}