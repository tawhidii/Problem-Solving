var number=function(array){
    const result = [];
    array.forEach((value,index)=>{
        result.push(`${index+1}: ${value}`);
    })
    return result
}

number(["a", "b", "c"])

