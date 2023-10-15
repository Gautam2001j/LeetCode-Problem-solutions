class Solution {
    public int[] plusOne(int[] digits) {
        // int number =0;
        // int n = digits.length;
        // for(int i=0; i<n; i++){
        //     number = digits[i] + number *10;
        // }
        // number = number+1;
        // System.out.println(number);
        // String s= String.valueOf(number);
        // int []result = new int[s.length()];

        // for(int j=0; j<result.length; j++){
        //     char c = s.charAt(j);
        //     result[j] = Character.getNumericValue(c);
        // }
        // return result;
        for (int i = digits.length - 1; i >= 0; i--) {
	        if (digits[i] < 9) {
		        digits[i]++;
		        return digits;
	        }
	        digits[i] = 0;
        }

        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}