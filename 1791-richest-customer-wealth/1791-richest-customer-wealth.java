class Solution {
    public int maximumWealth(int[][] accounts) {
        int wealth=0;
        for(int i=0; i<accounts.length; i++){
            int current_wealth = 0;
            for(int  j=0; j<accounts[i].length; j++){
                current_wealth = current_wealth + accounts[i][j];
            }
            wealth = Math.max(wealth , current_wealth);
        }
        return wealth;
    }
}