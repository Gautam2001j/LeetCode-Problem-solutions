class Solution {
    public int findNumbers(int[] nums) {
        int count =0;
        String[] array= new String[nums.length];
        for(int i=0; i<nums.length; i++){
            array[i]=String.valueOf(nums[i]);
            if(array[i].length() %2 == 0 ){
                count++;
            }
        }
        return count;
    }
}