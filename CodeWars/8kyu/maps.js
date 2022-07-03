function maps(x){
    let res = [];
    x.forEach(element => {
        res.push(element*2)
    });
    return res;
}

maps([1, 2, 3] )