class Solution {
    public int countSeniors(String[] details) {
        int age[] = new int[details.length];
        int count = 0;
        for(int i=0; i< details.length; i++){
            String temp = details[i].substring(11, 13);
            age[i] = Integer.parseInt(temp);
            if(age[i] > 60){
                count++;
            }
        }
        
        return count;
    }
}