/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let X=0;
    for(let i=0;i<operations.length;i++){
        if(operations[i]=='--X'){
            X=X-1;
        }else if(operations[i]=='X--'){
            X=X-1;
        }else if(operations[i]=='++X'){
             X=X+1;
        }else{
             X=1+X;
        }
    }
    return X;
};