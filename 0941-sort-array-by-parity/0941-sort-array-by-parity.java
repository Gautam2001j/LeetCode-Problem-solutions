class Solution {
    public int[] sortArrayByParity(int[] nums) {
        /*
        int[] result=new int[nums.length];
        for(int i=0 ,j=0 , k=nums.length-1; i<nums.length; i++){
            if(nums[i]%2 == 0){
                result[j] = nums[i];
                j++;
            }else if(nums[i]%2 !=0){
                result[k]=nums[i];
                k--;
            }
        }
        return result;
        */
        int j = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] % 2 == 0){
                swap(nums, i, j++);
            }
        }
        return nums;
    }
    private void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}