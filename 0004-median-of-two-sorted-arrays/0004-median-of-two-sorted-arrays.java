class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] result = new int[nums1.length+nums2.length];
        double median=0;
        for(int i=0; i<nums1.length; i++){
            result[i] = nums1[i];
        }
        for(int j=0; j<nums2.length; j++){
            result[nums1.length+j] = nums2[j];
        }
        Arrays.sort(result);
        if (result.length % 2 == 0) {
            median =( (double)result[(result.length / 2) - 1] + (double)result[result.length / 2] )/2;
        } else {
            median = (double)result[result.length / 2];
        }
        
        return median;
    }
}