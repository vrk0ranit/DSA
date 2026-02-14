/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    const newArray=[...nums,...nums];
    return newArray;
};