function sortByLength (array) {
    // Return an array containing the same strings, ordered from shortest to longest
let result = array.sort((a,b)=>a.length - b.length)
return result;
};

sortByLength(["Beg", "Life", "I", "To"])