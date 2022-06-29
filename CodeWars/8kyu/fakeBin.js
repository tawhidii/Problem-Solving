function fakeBin(x){
    let result = [];
    for(let val of x){
        if(parseInt(val)>=5)result.push('1');
        if(parseInt(val)<5)result.push('0');
    }

    return result.join('');

}

console.log(fakeBin('45385593107843568'))

