var countBits = function(n) {
    // Program Me
    let count = 0;
    n.toString(2).split('').forEach(item => {
        if(item==='1'){
            count++;
        }
    });
    return count;

};
console.log(countBits(1234))