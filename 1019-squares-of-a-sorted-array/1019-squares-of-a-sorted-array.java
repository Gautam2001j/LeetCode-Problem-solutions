class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        for(int i=0; i<nums.length; i++){
            result[i] = nums[i] * nums[i] ;
        }
        for(int j=1; j<result.length; j++){
            
            int key = result[j];
            int k = j - 1;
            while (k >= 0 && result[k] > key) {
                result[k + 1] = result[k];
                k = k - 1;
            }
            result[k + 1] = key;
            
        }
        return result;
    }
}