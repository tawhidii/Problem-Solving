Array.prototype.count = function(value){
    let count = 0;
    this.forEach(element => {
        if(element === value){
            count++;
        }
    });
    return count;
}

function isValidWalk(walk) {
    //insert brilliant code here

    if(walk.length !== 10){
        return false;
    }
    if((walk.count('n') === walk.count('s')) && (walk.count('e') === walk.count('w'))){
        return true;
    }else{
        return false;
    }
    

  }

console.log(isValidWalk(['n','s','n','s','n','s','n','s','n','s']))