class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()<1) return true;
        int i=0 , j=0;
        while(i<s.length() && j<t.length()){
            if(s.charAt(i) == t.charAt(j)){
                j++;
                i++;
            }else{
                j++;
            }
            if(i == s.length()) return true;
        }
        return false;
    }
}