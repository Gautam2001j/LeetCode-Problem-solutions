//Check if Array Is Sorted and Rotated
class Solution {
    public boolean check(int[] nums) {
        int count =0;
        if(nums[0]<nums[nums.length-1]) count++;
        for(int i=0; i<nums.length-1; i++){
            if(nums[i]>nums[i+1]) count++;
            if(count>1) return false;
        }
        return true;
        // int temp[] = new int[nums.length];
        // for(int i=0;i<nums.length;i++){
        //     temp[i] = nums[i];
        // }
        // Arrays.sort(temp);
        // for(int i=0;i<nums.length-1;i++){
        //     int last = temp[nums.length-1];
        //      for(int j = nums.length-1; j >0; j--){      
        //         temp[j] = temp[j-1];    
        //     } 
        //     temp[i] = last;
        //     for(int k=0;k<nums.length-1;k++){
        //         if(nums[i] == temp[i]){
        //             return true;
        //         }
        //     }
        // }
        // return false;
    }
}