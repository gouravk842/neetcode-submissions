class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] newnums = new int[nums.length*2];
        for(int i=0;i<newnums.length;i++){
            if(i<nums.length)
                newnums[i]=nums[i];
            else
                newnums[i]=nums[i%nums.length];
        }
        return newnums;
    }
}