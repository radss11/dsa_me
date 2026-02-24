class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tGas=0;
        int tAmount=0;
        for(int i=0;i<gas.length;i++){
            tAmount+=cost[i];
            tGas+=gas[i];
        }
     if(tAmount>tGas)
        return -1;
        int bachaHuaTel=0;
        int surwat=0;
        for(int i=0;i<cost.length;i++){
            bachaHuaTel+=(gas[i]-cost[i]);
            if(bachaHuaTel<0){
                bachaHuaTel=0;
                surwat=i+1;
            }
        }
    return surwat;}
}