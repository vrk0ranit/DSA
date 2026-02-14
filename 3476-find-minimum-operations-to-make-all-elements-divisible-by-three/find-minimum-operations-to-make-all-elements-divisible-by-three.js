/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    let count=0;
    for(let i=0;i<nums.length;i++){
        if(nums[i]%3==1){
            count++;
        }
        else if(nums[i]%3==2){
            count++;
        }
    }
    return count;
};