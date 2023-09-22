class Solution {
    public void moveZeroes(int[] nums) {
        int i=0 , count=0;
        while(i<nums.length){
            if(nums[i] == 0){
                count++;
            }else if(count>0){
                int temp = nums[i];
                nums[i]=0;
                nums[i-count] = temp;
            }
            i++;
        }
    }
}