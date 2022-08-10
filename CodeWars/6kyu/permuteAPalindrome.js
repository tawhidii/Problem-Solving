function permuteAPalindrome (input) {
    let mySet = new Set();
    input.split('').forEach(item=>{
        if(mySet.has(item)){
            mySet.delete(item);
        }else{
            mySet.add(item);
        }
    })
    return mySet.size<=1;
}






