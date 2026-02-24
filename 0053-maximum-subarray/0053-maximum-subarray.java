class Solution {
    public int maxSubArray(int[] arr) {
        //   int arr[]={3,-2,-2,4,1};
        int cs=0;
        int ans = Integer.MIN_VALUE;
        int n=arr.length;
        for(int i=0;i<arr.length;i++){
             cs=arr[i]+cs;
             ans=Math.max(ans,cs);
            
                    if(cs<0){
                        cs=0;
                    }
        }
                    return ans;
    }
}