
var capitals = function (word) {
	// Write your code here
    let result = []
    word.split('').forEach((element,index) => {
        if(element == element.toUpperCase()){
            result.push(index);
        }
    });
    return result;
};

capitals('CodEWaRs')