var finalValueAfterOperations = function (operations) {
    let value = 0;
    for (let op of operations) {
        if (op === 'X++') {
            value++
        }
        if (op === '++X') {
            value++
        }
        if (op === '--X') {
            value--
        }
        if (op === 'X--') {
            value--
        }
    }
    return value
};

