class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        if(nums.length==0){
                return 0;
        }
        if(nums.length==1){
                return 1;
        }
        else{
            int conta=1,contamax=0;
            for(int i=0;i<nums.length-1;i++){
                if(nums[i+1]!=nums[i]){
                    if(nums[i+1]==nums[i]+1){
                        conta++;
                    }
                    else{
                        conta=1;
                    }
                }
                if(conta>contamax){
                    contamax=conta;
                }
            }
        return contamax;
        }
    }
}
