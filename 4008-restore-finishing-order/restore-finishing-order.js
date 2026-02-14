/**
 * @param {number[]} order
 * @param {number[]} friends
 * @return {number[]}
 */
var recoverOrder = function(order, friends) {
    const ans=[];
    for(let i=0;i<order.length;i++){
        if(friends.includes(order[i])){
            ans.push(order[i]);
        }
    }
    return ans;
};