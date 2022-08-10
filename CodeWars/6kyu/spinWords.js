function spinWords(string){
    //TODO Have fun :)
    let result = [];
    string.split(' ').forEach(item => {
        if(item.length>=5){
            result.push(item.split('').reverse().join(''));
        }else{
            result.push(item);
        }
    });
    return result.join(' ')


}

console.log(spinWords('Hey fellow warriors'))