var groupAnagrams = function(strs) {
    let map = {}
    for(let str of strs){
        let reversedStr = str.split('').sort().join('');
        if(map[reversedStr]){
            map[reversedStr].push(str);
        }else{
            map[reversedStr] = [str];
        }
    }
    return Object.values(map);
    
};


groupAnagrams(["eat","tea","tan","ate","nat","bat"])