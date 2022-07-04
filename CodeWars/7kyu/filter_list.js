function filter_list(l) {
    // Return a new array with the strings filtered out
    return l.filter(item=>item !== item.toString())
}

console.log(filter_list([1,2,'a','b']))