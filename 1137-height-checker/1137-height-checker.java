class Solution {
    public int heightChecker(int[] heights) {
        int[] expected= new int[heights.length];
        int i=0,count=0;
        for(i=0; i<heights.length; i++){
            expected[i] = heights[i];
        }
        Arrays.sort(expected);
        for(i=0; i<heights.length; i++){
            if(heights[i] != expected[i]){
                count++;
            }
        }
        return count++;
    }
}