class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int count =0;
        int temp = x;
        while(temp != 0){
            int a = temp%10;
            count = count*10+a;
            temp /= 10;
        }
        return (count == x);
    }
}